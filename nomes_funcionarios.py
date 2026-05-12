import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1utRX7L53jEKEMUut4etgksRNf4Xadojf0kw4otIp4tw/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

df_nomes = conn.read(spreadsheet=url, worksheet="Funcionarios")

lista_nomes = sorted(df_nomes["Nome"].dropna().tolist())

nome_usuario = st.selectbox(
    "Nome",
    [""] + lista_nomes
)
