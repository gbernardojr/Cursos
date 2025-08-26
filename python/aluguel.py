import streamlit as st
import pandas as pd
import numpy as np

# Apenas para o exemplo, crie alguns dados de casas
data = {
    'Bairro': ['Centro', 'Jardim Amélia', 'Vila Nova', 'Centro', 'Vila Nova', 'Jardim Amélia'],
    'Quartos': [2, 3, 1, 4, 2, 3],
    'Banheiros': [1, 2, 1, 3, 1, 2],
    'Preço (R$)': [1500, 2200, 1000, 3500, 1800, 2500],
    'Área (m²)': [70, 120, 50, 180, 85, 130]
}

df = pd.DataFrame(data)

st.set_page_config(
    page_title="Encontre sua Casa para Alugar",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Encontre sua Casa para Alugar")
st.markdown("Use os filtros abaixo para encontrar a casa perfeita para você!")

st.markdown("---")

# Opções de filtro na barra lateral
st.sidebar.header("Filtros de Pesquisa")

# Filtro de Bairro
bairro_selecionado = st.sidebar.selectbox(
    "Escolha o Bairro:",
    options=['Todos'] + list(df['Bairro'].unique()),
    index=0
)

# Filtro de Quartos
min_quartos = int(df['Quartos'].min())
max_quartos = int(df['Quartos'].max())
quartos_selecionados = st.sidebar.slider(
    "Número de Quartos:",
    min_value=min_quartos,
    max_value=max_quartos,
    value=(min_quartos, max_quartos)
)

# Filtro de Banheiros
min_banheiros = int(df['Banheiros'].min())
max_banheiros = int(df['Banheiros'].max())
banheiros_selecionados = st.sidebar.slider(
    "Número de Banheiros:",
    min_value=min_banheiros,
    max_value=max_banheiros,
    value=(min_banheiros, max_banheiros)
)

# Filtro de Preço
min_preco = int(df['Preço (R$)'].min())
max_preco = int(df['Preço (R$)'].max())
preco_selecionado = st.sidebar.slider(
    "Faixa de Preço (R$):",
    min_value=min_preco,
    max_value=max_preco,
    value=(min_preco, max_preco)
)

# Aplicar os filtros
df_filtrado = df.copy()

if bairro_selecionado != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Bairro'] == bairro_selecionado]

df_filtrado = df_filtrado[
    (df_filtrado['Quartos'] >= quartos_selecionados[0]) &
    (df_filtrado['Quartos'] <= quartos_selecionados[1])
]

df_filtrado = df_filtrado[
    (df_filtrado['Banheiros'] >= banheiros_selecionados[0]) &
    (df_filtrado['Banheiros'] <= banheiros_selecionados[1])
]

df_filtrado = df_filtrado[
    (df_filtrado['Preço (R$)'] >= preco_selecionado[0]) &
    (df_filtrado['Preço (R$)'] <= preco_selecionado[1])
]

# Exibir os resultados
st.subheader("Resultados Encontrados")

if df_filtrado.empty:
    st.warning("Nenhuma casa encontrada com os filtros selecionados. Tente ajustar suas opções.")
else:
    st.info(f"Mostrando {len(df_filtrado)} casa(s) encontrada(s).")
    for index, row in df_filtrado.iterrows():
        st.markdown(f"""
        ### Casa no Bairro: **{row['Bairro']}**
        - **Quartos:** {row['Quartos']}
        - **Banheiros:** {row['Banheiros']}
        - **Área:** {row['Área (m²)']} m²
        - **Preço:** R$ {row['Preço (R$)']:,}
        """)
        st.markdown("---")

st.markdown("""
<style>
.st-emotion-cache-1c7er83.e1f1d6gn0 {
    font-size: 1.25rem;
    font-weight: bold;
    color: #4CAF50;
}
.st-emotion-cache-1c7er83.e1f1d6gn0:hover {
    color: #388E3C;
}
</style>
""", unsafe_allow_html=True)
