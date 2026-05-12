import streamlit as st
import datetime
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from nomes_funcionarios import carregar_funcionarios

secao_usuario = st.session_state

coluna_esquerda, coluna_direita = st.columns([0.5, 1])

coluna_esquerda.image("imagem/logo.jpeg", width=250)
st.markdown(f"# 🌟Olá, Bem-vindo.")
st.subheader("Registro de atividades")

# Estabelecendo a conexão com o Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)



#pegando os dados existentes da planilha/banco e transformando em um dataframe
existing_data = conn.read(worksheet="Dados", usecols=list(range(7)), ttl=5)
existing_data = existing_data.dropna(how="all")


nome_usuario = carregar_funcionarios()

lista_projetos = ['', 'CDS', 'VDS', 'ODS', 'TDS', 'BDS', 'TELM', 'TOT', 'Fabrica', 'Logistica', 'Externo', 'Manutenção', 'Visita a cliente']

# Campo 'Área' com lista suspensa
area = st.selectbox(
    'Área',
    ['', 'Marcenaria estrutural', 'Acabamentos Geral', 'Marcenaria móveis', 'Outros', 'Elétrica', 'Piso', 'Hidráulica']
)

# Campo 'Projeto' convertido em lista suspensa com os itens fornecidos
projeto = st.selectbox(
    'Projeto',
    lista_projetos
)

# Novo campo 'Número do projeto' abaixo de 'Projeto'
numero_projeto = st.text_input('Número do projeto')

# Campos de horário de início e término da atividade
hora_inicio = st.time_input('Horário de início da atividade', datetime.time(8, 0))
hora_termino = st.time_input('Horário de término da atividade', datetime.time(17, 0))
st.warning("Caso você tenha almoçado e não preecheu o formulário, desconte a quantidade de tempo gasta durante o almoço no preenchimento.")

# Campo de data travado na data atual
data_atual = datetime.date.today()
st.write(f"**Data:** {data_atual.strftime('%d/%m/%Y')}")

data_termino = ''

# Botão para enviar o relatório
if st.button('Enviar'):
    if not area or not projeto or not numero_projeto or not hora_inicio or not hora_termino or area == '' or projeto == '':
        st.warning("Todos os campos devem ser preenchidos")
        st.stop()
    else:
        # cria uma nova linha na tabela
        dados_forms = pd.DataFrame(
            [
                {
                    "Usuario": nome_usuario,
                    "Area": area,
                    "Projeto": projeto + '-' + numero_projeto,
                    "Hr_inicio": hora_inicio,
                    "Hr_final": hora_termino,
                    "Data": data_atual.strftime("%Y-%m-%d"),
                    "Data_termino": data_termino
                }
            ]
        )
        # Add the new data to the existing data
        updated_df = pd.concat([existing_data, dados_forms], ignore_index=True)

        # Update Google Sheets with the new vendor data
        conn.update(worksheet="Dados", data=updated_df)

        st.success("Formulário preenchido com sucesso!")

if nome_usuario == "Ronaldo" or nome_usuario == "Vitor":
    data_termino = st.date_input("Informe a data de finalização do projeto")

    if st.button("Submeter data"):
        if not projeto or not numero_projeto or projeto == '':
            st.warning("Informe o projeto, número e data de término.")
            st.stop()
        else:
            # cria uma nova linha na tabela
            dados_forms = pd.DataFrame(
                [
                    {
                        "Usuario": nome_usuario,
                        "Projeto": projeto + '-' + numero_projeto,
                        "Data": data_atual.strftime("%Y-%m-%d"),
                        "Data_termino": data_termino
                    }
                ]
            )
            # Add the new data to the existing data
            updated_df = pd.concat([existing_data, dados_forms], ignore_index=True)

            # Update Google Sheets with the new vendor data
            conn.update(worksheet="Dados", data=updated_df)

            st.success("Data de término submetida com sucesso")

