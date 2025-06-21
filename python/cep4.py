# pip install streamlit requests pandas geopy
import streamlit as st
import requests
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Configuração da página
st.set_page_config(page_title="Busca CEP + Mapa", page_icon="📍")

# Título e descrição
st.title("🌍 Busca de Endereço por CEP com Mapa")
st.markdown("""
Digite um CEP brasileiro (apenas números) para consultar o endereço e sua localização no mapa.
""")

# Input do usuário
cep = st.text_input("CEP (ex: 01001000):", max_chars=8, placeholder="Digite 8 dígitos").strip()

# Inicializa o geocodificador
geolocator = Nominatim(user_agent="streamlit_cep_app")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

if cep:
    if not cep.isdigit() or len(cep) != 8:
        st.error("⚠️ O CEP deve conter exatamente 8 dígitos numéricos!")
    else:
        with st.spinner("Buscando endereço e localização..."):
            try:
                # Consulta ViaCEP
                viacep_url = f"https://viacep.com.br/ws/{cep}/json/"
                response = requests.get(viacep_url)
                dados_cep = response.json()

                if "erro" in dados_cep:
                    st.error("CEP não encontrado. Verifique o número e tente novamente.")
                else:
                    # Formata o endereço para busca no OpenStreetMap
                    endereco_completo = (
                        f"{dados_cep.get('logradouro', '')}, "
                        f"{dados_cep.get('bairro', '')}, "
                        f"{dados_cep.get('localidade', '')}, "
                        f"{dados_cep.get('uf', '')}, "
                        "Brasil"
                    )

                    # Busca coordenadas no OpenStreetMap
                    location = geocode(endereco_completo)
                    
                    if location:
                        # Exibe os dados do CEP
                        st.success("Endereço encontrado!")
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.subheader("📌 Dados do CEP")
                            st.markdown(f"""
                            - **CEP:** {dados_cep.get('cep', 'N/A')}
                            - **Logradouro:** {dados_cep.get('logradouro', 'N/A')}
                            - **Bairro:** {dados_cep.get('bairro', 'N/A')}
                            """)
                        
                        with col2:
                            st.subheader("🏙️ Cidade/Estado")
                            st.markdown(f"""
                            - **Cidade:** {dados_cep.get('localidade', 'N/A')}
                            - **UF:** {dados_cep.get('uf', 'N/A')}
                            - **DDD:** {dados_cep.get('ddd', 'N/A')}
                            """)

                        # Exibe o mapa
                        st.subheader("🗺️ Localização Aproximada")
                        st.write(f"Endereço: {endereco_completo}")
                        
                        # Cria DataFrame com as coordenadas
                        mapa_df = pd.DataFrame({
                            "lat": [location.latitude],
                            "lon": [location.longitude]
                        })
                        
                        # Exibe o mapa com zoom apropriado
                        st.map(mapa_df, zoom=15)
                        
                        # Mostra coordenadas
                        st.markdown(f"""
                        **Coordenadas Geográficas:**
                        - Latitude: {location.latitude:.6f}
                        - Longitude: {location.longitude:.6f}
                        """)
                    else:
                        st.warning("Endereço encontrado, mas não foi possível determinar a localização exata no mapa.")
                        st.json(dados_cep)

            except requests.exceptions.RequestException:
                st.error("Falha na conexão com a API. Tente novamente mais tarde.")
            except Exception as e:
                st.error(f"Ocorreu um erro: {str(e)}")

# Rodapé
st.markdown("---")
st.caption("Dados de CEP fornecidos pela [ViaCEP](https://viacep.com.br). Localizações por [OpenStreetMap](https://www.openstreetmap.org).")
