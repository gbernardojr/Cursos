import streamlit as st
import json
import os
import datetime

# Nome do arquivo JSON
ARQUIVO_DADOS = "pacientes.json"

# Funções para manipulação do arquivo JSON
def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def criar_paciente(cpf, nome, data_nascimento, sexo, endereco, telefone, email, historico_medico=None):
    return {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "historico_medico": historico_medico or [],
        "data_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "data_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

# Funções CRUD
def cadastrar_paciente():
    st.subheader("Cadastrar Novo Paciente")
    
    with st.form(key="form_cadastro"):
        col1, col2 = st.columns(2)
        
        with col1:
            cpf = st.text_input("CPF (somente números)", max_chars=11)
            nome = st.text_input("Nome Completo")
            data_nascimento = st.date_input("Data de Nascimento", min_value=datetime(1900, 1, 1))
            sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        
        with col2:
            endereco = st.text_input("Endereço")
            telefone = st.text_input("Telefone")
            email = st.text_input("E-mail")
            historico_medico = st.text_area("Histórico Médico (opcional)")
        
        submit_button = st.form_submit_button("Cadastrar Paciente")
    
    if submit_button:
        if not cpf or not nome:
            st.error("CPF e Nome são campos obrigatórios!")
            return
        
        dados = carregar_dados()
        
        if cpf in dados:
            st.error("Paciente com este CPF já cadastrado!")
            return
        
        paciente = criar_paciente(
            cpf=cpf,
            nome=nome,
            data_nascimento=data_nascimento.strftime("%d/%m/%Y"),
            sexo=sexo,
            endereco=endereco,
            telefone=telefone,
            email=email,
            historico_medico=historico_medico.split("\n") if historico_medico else []
        )
        
        dados[cpf] = paciente
        salvar_dados(dados)
        
        st.success("Paciente cadastrado com sucesso!")
        st.balloons()

def listar_pacientes():
    st.subheader("Lista de Pacientes Cadastrados")
    
    dados = carregar_dados()
    
    if not dados:
        st.info("Nenhum paciente cadastrado ainda.")
        return
    
    # Filtro por nome
    filtro_nome = st.text_input("Filtrar por nome:")
    
    pacientes_filtrados = []
    for cpf, paciente in dados.items():
        if filtro_nome.lower() in paciente["nome"].lower():
            pacientes_filtrados.append((cpf, paciente))
    
    if not pacientes_filtrados:
        st.warning("Nenhum paciente encontrado com o filtro aplicado.")
        return
    
    for cpf, paciente in pacientes_filtrados:
        with st.expander(f"{paciente['nome']} - CPF: {cpf}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Data de Nascimento:** {paciente['data_nascimento']}")
                st.write(f"**Sexo:** {paciente['sexo']}")
                st.write(f"**Endereço:** {paciente['endereco']}")
            
            with col2:
                st.write(f"**Telefone:** {paciente['telefone']}")
                st.write(f"**E-mail:** {paciente['email']}")
                st.write(f"**Cadastrado em:** {paciente['data_cadastro']}")
            
            if paciente["historico_medico"]:
                st.write("**Histórico Médico:**")
                for item in paciente["historico_medico"]:
                    st.write(f"- {item}")

def editar_paciente():
    st.subheader("Editar Paciente")
    
    dados = carregar_dados()
    
    if not dados:
        st.info("Nenhum paciente cadastrado para editar.")
        return
    
    cpf_selecionado = st.selectbox(
        "Selecione o paciente pelo CPF",
        options=list(dados.keys()),
        format_func=lambda x: f"{dados[x]['nome']} - {x}"
    )
    
    paciente = dados[cpf_selecionado]
    
    with st.form(key="form_edicao"):
        col1, col2 = st.columns(2)
        
        with col1:
            novo_cpf = st.text_input("CPF (somente números)", value=paciente["cpf"], max_chars=11)
            nome = st.text_input("Nome Completo", value=paciente["nome"])
            data_nascimento = st.text_input("Data de Nascimento", value=paciente["data_nascimento"])
            sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"], index=["Masculino", "Feminino", "Outro"].index(paciente["sexo"]))
        
        with col2:
            endereco = st.text_input("Endereço", value=paciente["endereco"])
            telefone = st.text_input("Telefone", value=paciente["telefone"])
            email = st.text_input("E-mail", value=paciente["email"])
            historico_medico = st.text_area("Histórico Médico", value="\n".join(paciente["historico_medico"]))
        
        submit_button = st.form_submit_button("Atualizar Paciente")
    
    if submit_button:
        if not novo_cpf or not nome:
            st.error("CPF e Nome são campos obrigatórios!")
            return
        
        # Se o CPF foi alterado, precisamos verificar se o novo CPF já existe (e não é o mesmo paciente)
        if novo_cpf != cpf_selecionado and novo_cpf in dados:
            st.error("Já existe um paciente com este novo CPF!")
            return
        
        # Remove o paciente antigo se o CPF foi alterado
        if novo_cpf != cpf_selecionado:
            dados.pop(cpf_selecionado)
        
        # Atualiza os dados do paciente
        paciente_atualizado = {
            "cpf": novo_cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "sexo": sexo,
            "endereco": endereco,
            "telefone": telefone,
            "email": email,
            "historico_medico": historico_medico.split("\n") if historico_medico else [],
            "data_cadastro": paciente["data_cadastro"],
            "data_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        
        dados[novo_cpf] = paciente_atualizado
        salvar_dados(dados)
        
        st.success("Paciente atualizado com sucesso!")

def excluir_paciente():
    st.subheader("Excluir Paciente")
    
    dados = carregar_dados()
    
    if not dados:
        st.info("Nenhum paciente cadastrado para excluir.")
        return
    
    cpf_selecionado = st.selectbox(
        "Selecione o paciente pelo CPF para excluir",
        options=list(dados.keys()),
        format_func=lambda x: f"{dados[x]['nome']} - {x}"
    )
    
    paciente = dados[cpf_selecionado]
    
    st.warning("Você está prestes a excluir o seguinte paciente:")
    st.json(paciente)
    
    if st.button("Confirmar Exclusão"):
        dados.pop(cpf_selecionado)
        salvar_dados(dados)
        st.success("Paciente excluído com sucesso!")

# Menu lateral
st.sidebar.title("Menu")
opcao = st.sidebar.radio(
    "Selecione uma opção:",
    ("Cadastrar Paciente","Listar Pacientes", 
     "Editar Paciente", "Excluir Paciente")
)

# Navegação entre páginas
if opcao == "Cadastrar Paciente":
    cadastrar_paciente()
elif opcao == "Listar Pacientes":
    listar_pacientes()
elif opcao == "Editar Paciente":
    editar_paciente()
elif opcao == "Excluir Paciente":
    excluir_paciente()

# Rodapé
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por Gilberto")
st.sidebar.markdown(f"Total de pacientes: ")   #{len(carregar_dados())}
