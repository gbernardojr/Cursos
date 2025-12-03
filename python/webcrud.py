import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Sistema de Agendamento PET", layout="wide")

st.title('🐾 Sistema de Agendamento PET - CRUD Completo')

# Inicializar variáveis de sessão
if 'agendamentos' not in st.session_state:
    st.session_state.agendamentos = []
if 'editar_index' not in st.session_state:
    st.session_state.editar_index = None
if 'modo_edicao' not in st.session_state:
    st.session_state.modo_edicao = False

# Funções auxiliares
def carregar_agendamentos():
    """Carrega os agendamentos do arquivo JSON"""
    arquivo_json = 'agendamentos.json'
    if os.path.exists(arquivo_json):
        try:
            with open(arquivo_json, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def salvar_agendamentos(agendamentos):
    """Salva os agendamentos no arquivo JSON"""
    arquivo_json = 'agendamentos.json'
    try:
        with open(arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(agendamentos, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        st.error(f'Erro ao salvar: {e}')
        return False

def formatar_data(data_str):
    """Formata data para exibição"""
    try:
        data_obj = datetime.strptime(data_str, '%Y-%m-%d')
        return data_obj.strftime('%d/%m/%Y')
    except:
        return data_str

# Carregar agendamentos do arquivo
st.session_state.agendamentos = carregar_agendamentos()

# Sidebar para navegação
st.sidebar.title("Navegação")
opcao = st.sidebar.radio(
    "Selecione uma opção:",
    ["📋 Listar Todos", "🔍 Pesquisar", "➕ Novo Agendamento", "✏️ Editar", "🗑️ Excluir"]
)

# FUNÇÃO: LISTAR TODOS OS AGENDAMENTOS
if opcao == "📋 Listar Todos":
    st.header("📋 Todos os Agendamentos")
    
    if st.session_state.agendamentos:
        # Converter para DataFrame para melhor visualização
        df = pd.DataFrame(st.session_state.agendamentos)
        
        # Formatar data para exibição
        if 'data' in df.columns:
            df['data_formatada'] = df['data'].apply(formatar_data)
        
        # Mostrar estatísticas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Agendamentos", len(st.session_state.agendamentos))
        with col2:
            st.metric("Pets Únicos", df['pet'].nunique() if 'pet' in df.columns else 0)
        with col3:
            st.metric("Tutores Únicos", df['tutor'].nunique() if 'tutor' in df.columns else 0)
        
        # Mostrar tabela
        st.dataframe(
            df[['tutor', 'pet', 'data_formatada', 'hora']] if 'data_formatada' in df.columns else df,
            use_container_width=True,
            column_config={
                "tutor": "Tutor",
                "pet": "Pet",
                "data_formatada": "Data",
                "hora": "Hora"
            }
        )
    else:
        st.info("📭 Nenhum agendamento cadastrado ainda.")

# FUNÇÃO: PESQUISAR POR NOME
elif opcao == "🔍 Pesquisar":
    st.header("🔍 Pesquisar Agendamentos")
    
    col1, col2 = st.columns(2)
    with col1:
        tipo_pesquisa = st.radio(
            "Pesquisar por:",
            ["Tutor", "Pet"]
        )
    
    with col2:
        termo_pesquisa = st.text_input(f"Digite o nome do {tipo_pesquisa.lower()}:")
    
    if termo_pesquisa:
        resultados = []
        for agendamento in st.session_state.agendamentos:
            if tipo_pesquisa == "Tutor":
                if termo_pesquisa.lower() in agendamento['tutor'].lower():
                    resultados.append(agendamento)
            else:
                if termo_pesquisa.lower() in agendamento['pet'].lower():
                    resultados.append(agendamento)
        
        if resultados:
            st.success(f"✅ Encontrados {len(resultados)} resultado(s)")
            
            for i, agendamento in enumerate(resultados, 1):
                with st.expander(f"Agendamento {i}: {agendamento['pet']} - {formatar_data(agendamento['data'])}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Tutor:** {agendamento['tutor']}")
                        st.write(f"**Data:** {formatar_data(agendamento['data'])}")
                    with col2:
                        st.write(f"**Pet:** {agendamento['pet']}")
                        st.write(f"**Hora:** {agendamento['hora']}")
        else:
            st.warning(f"⚠️ Nenhum agendamento encontrado para '{termo_pesquisa}'")

# FUNÇÃO: CRIAR NOVO AGENDAMENTO
elif opcao == "➕ Novo Agendamento":
    st.header("➕ Novo Agendamento")
    
    with st.form("form_novo_agendamento"):
        col1, col2 = st.columns(2)
        
        with col1:
            tutor = st.text_input("Nome do Tutor:*", key="novo_tutor")
            pet = st.text_input("Nome do Pet:*", key="novo_pet")
        
        with col2:
            data = st.date_input("Data do Agendamento:*", key="novo_data")
            hora = st.time_input("Hora do Agendamento:*", key="novo_hora")
        
        st.caption("* Campos obrigatórios")
        
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            submitted = st.form_submit_button("💾 Salvar Agendamento", type="primary")
        
        if submitted:
            if not tutor or not pet:
                st.error("⚠️ Por favor, preencha todos os campos obrigatórios!")
            else:
                novo_agendamento = {
                    'id': len(st.session_state.agendamentos) + 1,
                    'tutor': tutor,
                    'pet': pet,
                    'data': data.strftime('%Y-%m-%d'),
                    'hora': hora.strftime('%H:%M')
                }
                
                st.session_state.agendamentos.append(novo_agendamento)
                if salvar_agendamentos(st.session_state.agendamentos):
                    st.balloons()
                    st.success(f"✅ Agendamento para {pet} salvo com sucesso!")
                    st.rerun()
                else:
                    st.error("❌ Erro ao salvar agendamento!")

# FUNÇÃO: EDITAR AGENDAMENTO
elif opcao == "✏️ Editar":
    st.header("✏️ Editar Agendamento")
    
    if not st.session_state.agendamentos:
        st.info("📭 Nenhum agendamento para editar.")
    else:
        # Listar agendamentos para seleção
        opcoes = [f"{ag['pet']} - {formatar_data(ag['data'])} {ag['hora']} (Tutor: {ag['tutor']})" 
                 for ag in st.session_state.agendamentos]
        
        selecionado = st.selectbox(
            "Selecione o agendamento para editar:",
            opcoes,
            index=None,
            placeholder="Escolha um agendamento..."
        )
        
        if selecionado:
            index_selecionado = opcoes.index(selecionado)
            agendamento_editar = st.session_state.agendamentos[index_selecionado]
            
            with st.form("form_editar_agendamento"):
                col1, col2 = st.columns(2)
                
                with col1:
                    tutor_edit = st.text_input(
                        "Nome do Tutor:", 
                        value=agendamento_editar['tutor'],
                        key="editar_tutor"
                    )
                    pet_edit = st.text_input(
                        "Nome do Pet:", 
                        value=agendamento_editar['pet'],
                        key="editar_pet"
                    )
                
                with col2:
                    # Converter string para datetime
                    data_original = datetime.strptime(agendamento_editar['data'], '%Y-%m-%d')
                    hora_original = datetime.strptime(agendamento_editar['hora'], '%H:%M').time()
                    
                    data_edit = st.date_input(
                        "Data do Agendamento:", 
                        value=data_original,
                        key="editar_data"
                    )
                    hora_edit = st.time_input(
                        "Hora do Agendamento:", 
                        value=hora_original,
                        key="editar_hora"
                    )
                
                col1, col2, col3 = st.columns([1, 1, 2])
                with col1:
                    submitted_edit = st.form_submit_button("💾 Salvar Alterações", type="primary")
                with col2:
                    cancelar = st.form_submit_button("❌ Cancelar")
                
                if submitted_edit:
                    if not tutor_edit or not pet_edit:
                        st.error("⚠️ Por favor, preencha todos os campos!")
                    else:
                        # Atualizar agendamento
                        st.session_state.agendamentos[index_selecionado] = {
                            'id': agendamento_editar.get('id', index_selecionado + 1),
                            'tutor': tutor_edit,
                            'pet': pet_edit,
                            'data': data_edit.strftime('%Y-%m-%d'),
                            'hora': hora_edit.strftime('%H:%M')
                        }
                        
                        if salvar_agendamentos(st.session_state.agendamentos):
                            st.success("✅ Agendamento atualizado com sucesso!")
                            st.rerun()
                        else:
                            st.error("❌ Erro ao atualizar agendamento!")

# FUNÇÃO: EXCLUIR AGENDAMENTO
elif opcao == "🗑️ Excluir":
    st.header("🗑️ Excluir Agendamento")
    
    if not st.session_state.agendamentos:
        st.info("📭 Nenhum agendamento para excluir.")
    else:
        # Listar agendamentos para seleção
        opcoes = [f"{ag['pet']} - {formatar_data(ag['data'])} {ag['hora']} (Tutor: {ag['tutor']})" 
                 for ag in st.session_state.agendamentos]
        
        selecionado = st.selectbox(
            "Selecione o agendamento para excluir:",
            opcoes,
            index=None,
            placeholder="Escolha um agendamento..."
        )
        
        if selecionado:
            index_selecionado = opcoes.index(selecionado)
            agendamento_excluir = st.session_state.agendamentos[index_selecionado]
            
            # Mostrar detalhes do agendamento selecionado
            st.warning("⚠️ Você está prestes a excluir o seguinte agendamento:")
            
            col1, col2 = st.columns(2)
            with col1:
                st.info(f"**Tutor:** {agendamento_excluir['tutor']}")
                st.info(f"**Data:** {formatar_data(agendamento_excluir['data'])}")
            with col2:
                st.info(f"**Pet:** {agendamento_excluir['pet']}")
                st.info(f"**Hora:** {agendamento_excluir['hora']}")
            
            # Confirmação de exclusão
            col1, col2, col3 = st.columns(3)
            with col1:
                confirmar = st.button("✅ Confirmar Exclusão", type="primary")
            with col2:
                cancelar = st.button("❌ Cancelar")
            
            if confirmar:
                # Remover agendamento
                agendamento_removido = st.session_state.agendamentos.pop(index_selecionado)
                
                if salvar_agendamentos(st.session_state.agendamentos):
                    st.error(f"🗑️ Agendamento de {agendamento_removido['pet']} excluído com sucesso!")
                    st.rerun()
                else:
                    st.error("❌ Erro ao excluir agendamento!")

# Rodapé com informações
st.sidebar.markdown("---")
st.sidebar.info("""
**Sistema CRUD de Agendamentos PET**
- 📋 **Listar**: Visualize todos os agendamentos
- 🔍 **Pesquisar**: Encontre por nome do tutor ou pet
- ➕ **Criar**: Adicione novos agendamentos
- ✏️ **Editar**: Modifique agendamentos existentes
- 🗑️ **Excluir**: Remova agendamentos

Todos os dados são salvos em `agendamentos.json`
""")

# Mostrar estatísticas na sidebar
if st.session_state.agendamentos:
    st.sidebar.markdown("### 📊 Estatísticas")
    total = len(st.session_state.agendamentos)
    st.sidebar.metric("Agendamentos Totais", total)
