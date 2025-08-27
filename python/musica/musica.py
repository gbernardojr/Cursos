import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.io import wavfile
import librosa
import soundfile as sf
import tempfile
import matplotlib.pyplot as plt
import os

# --- Configurações da Página ---
st.set_page_config(
    page_title="Visualizador de Música Interativo",
    page_icon="🎶",
    layout="wide"
)

st.title("🎶 Visualizador de Música Interativo")
st.markdown("Faça o upload de um arquivo de áudio para visualizar a estrutura da música, a frequência das notas e a progressão dos acordes.")

st.markdown("---")

# --- Carregamento do Arquivo de Áudio ---
audio_file = st.file_uploader(
    "Carregar Arquivo de Áudio (.wav, .mp3, .flac)",
    type=["wav", "mp3", "flac"]
)

if audio_file is not None:
    # --- Salvar o arquivo temporariamente para processamento ---
    try:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(audio_file.read())
        audio_path = tfile.name
        tfile.close()

        # Carregar o arquivo com librosa para compatibilidade
        # librosa é melhor para análise, pois faz o resampling automaticamente
        y, sr = librosa.load(audio_path, sr=None)

        # Exibir o player de áudio
        st.subheader("Player de Áudio")
        st.audio(audio_path, format=f'audio/{audio_file.type.split("/")[-1]}')

        # --- Processamento do Áudio ---
        st.subheader("Análise da Estrutura Musical")
        st.info("Processando o arquivo, por favor aguarde...")

        # Detecção de batidas (tempo)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)
        st.markdown(f"**Tempo (BPM):** `{tempo:.2f}`")

        # Detecção de frequência fundamental (pitch)
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        times = librosa.times_like(pitches, sr=sr)
        
        # Encontrar o pitch mais provável em cada quadro de tempo
        pitches_out = []
        for t in range(pitches.shape[1]):
            # Encontra a nota com maior magnitude
            index = magnitudes[:, t].argmax()
            pitches_out.append(pitches[index, t])

        # --- Visualização com Plotly ---
        st.markdown("---")
        st.subheader("Visualização Interativa")
        
        # Gráfico da forma de onda
        st.markdown("#### Forma de Onda")
        fig_waveform = go.Figure()
        fig_waveform.add_trace(go.Scatter(y=y, mode='lines', name='Forma de Onda', line=dict(color='#1E90FF')))
        fig_waveform.update_layout(
            title="Forma de Onda de Áudio",
            xaxis_title="Amostras",
            yaxis_title="Amplitude",
            height=300
        )
        st.plotly_chart(fig_waveform, use_container_width=True)
        
        # Gráfico de Pitch (Frequência Fundamental)
        st.markdown("#### Frequência Fundamental (Pitch)")
        fig_pitch = go.Figure()
        fig_pitch.add_trace(go.Scatter(x=times, y=pitches_out, mode='lines', name='Pitch', line=dict(color='#FF4500')))
        fig_pitch.update_layout(
            title="Frequência Fundamental ao Longo do Tempo",
            xaxis_title="Tempo (s)",
            yaxis_title="Frequência (Hz)",
            height=300
        )
        st.plotly_chart(fig_pitch, use_container_width=True)

        # Gráfico de Espectrograma (Frequências ao longo do tempo)
        st.markdown("#### Espectrograma")
        st.warning("O espectrograma pode demorar um pouco para renderizar em arquivos maiores.")
        S = np.abs(librosa.stft(y))
        S_db = librosa.amplitude_to_db(S, ref=np.max)
        
        fig_spec = go.Figure(
            data=go.Heatmap(
                z=S_db,
                x=librosa.times_like(S),
                y=librosa.fft_frequencies(sr=sr),
                colorscale='Viridis'
            )
        )
        fig_spec.update_layout(
            title="Espectrograma",
            xaxis_title="Tempo (s)",
            yaxis_title="Frequência (Hz)",
            height=500
        )
        st.plotly_chart(fig_spec, use_container_width=True)
        
    except Exception as e:
        st.error(f"Ocorreu um erro ao processar o arquivo: {e}")
    finally:
        # Remover o arquivo temporário
        if 'audio_path' in locals() and os.path.exists(audio_path):
            os.remove(audio_path)

st.markdown("---")
st.markdown("Construído com ❤️ e Python por Gemini. Use os pacotes `streamlit`, `numpy`, `librosa`, `soundfile` e `plotly`.")
