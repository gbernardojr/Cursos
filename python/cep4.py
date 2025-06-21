import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Consulta de CEP", page_icon="📌")

# Título e descrição
st.title("🌍 Buscador de Endereço por CEP")
st.markdown("""
Digite um CEP (apenas números) para consultar o endereço correspondente.  
Dados fornecidos pela [ViaCEP API](https://viacep.com.br/).
""")

# Input do usuário
cep = st.text_input("CEP (ex: 01001000):", max_chars=8, placeholder="Digite 8 dígitos").strip()

# Validação e consulta à API
if cep:
    if not cep.isdigit() or len(cep) != 8:
        st.error("⚠️ O CEP deve conter exatamente 8 dígitos numéricos!")
    else:
        with st.spinner("Buscando endereço..."):
            try:
                # Requisição à API
                url = f"https://viacep.com.br/ws/{cep}/json/"
                response = requests.get(url)
                dados = response.json()

                if "erro" in dados:
                    st.error("CEP não encontrado. Verifique o número e tente novamente.")
                else:
                    # Exibição dos dados
                    st.success("Endereço encontrado!")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("📌 Dados do CEP")
                        st.markdown(f"""
                        - **Logradouro:** {dados.get('logradouro', 'N/A')}  
                        - **Bairro:** {dados.get('bairro', 'N/A')}  
                        - **Cidade:** {dados.get('localidade', 'N/A')}  
                        """)
                    with col2:
                        st.subheader("📝 Complemento")
                        st.markdown(f"""
                        - **UF:** {dados.get('uf', 'N/A')}  
                        - **DDD:** {dados.get('ddd', 'N/A')}  
                        - **CEP Formatado:** {dados.get('cep', 'N/A')}  
                        """)

                    # Mapa (opcional)
                    st.subheader("🗺️ Localização Aproximada")
                    st.write(f"*Visualização aproximada do CEP {dados['cep']}*")
                    st.map(  # Usa a latitude/longitude aproximada (API não retorna coordenadas exatas)
                        pd.DataFrame({"lat": [float(dados.get('lat', -23.5505))], "lon": [float(dados.get('lon', -46.6333))]}),
                        zoom=12
                    )

            except requests.exceptions.RequestException:
                st.error("Falha na conexão com a API. Tente novamente mais tarde.")
