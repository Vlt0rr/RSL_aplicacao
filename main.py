import streamlit as st

#pegando senhas do arquivo: "secrets"
senha_ronaldo = st.secrets["credenciais"]["senha_ronaldo"]
senha_felipe = st.secrets["credenciais"]["senha_felipe"]

# Dicionário com usuários, senhas e tipo
usuarios = {
    "Ronaldo": {"senha": senha_ronaldo, "tipo": "admin"},
    "Felipe": {"senha": senha_felipe, "tipo": "normal"}
}

# Função de autenticação
def autenticar(usuario, senha):
    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        return usuarios[usuario]["tipo"]
    return None

# Página de logout
def logout():
    st.title("Você saiu da conta.")
    st.session_state.autenticado = False
    st.session_state.usuario = ""
    st.session_state.tipo = ""
    st.info("Sessão encerrada. Atualize a página para voltar ao login.")

# Estado inicial
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
    st.session_state.usuario = ""
    st.session_state.tipo = ""

# Página de login
if not st.session_state.autenticado:
    st.title("Login")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        tipo = autenticar(usuario, senha)
        if tipo:
            st.session_state.autenticado = True
            st.session_state.usuario = usuario
            st.session_state.tipo = tipo
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")

# Após login, definir menu com base no tipo de usuário
else:
    if st.session_state.tipo == "admin":
        pg = st.navigation({
            "Home": [st.Page("homepage.py", title="Formulário")],
            "Análises": [
                st.Page("tabela.py", title="Base de dados"),
                st.Page("indicadores.py", title="Indicadores"),
                st.Page("graficos.py", title="Distribuição de horas por área"),
                st.Page("planejadoxreal.py", title="Planejado x Real")
            ],
            "Conta": [
                st.Page(logout, title="Sair")
            ]
        })
    else:
        pg = st.navigation({
            "Home": [st.Page("homepage.py", title="Formulário")],
            "Conta": [st.Page(logout, title="Sair")]
        })

    # Executar a navegação
    pg.run()
