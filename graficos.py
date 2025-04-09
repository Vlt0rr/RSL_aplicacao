import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_gsheets import GSheetsConnection

from data_loader import carregar_dados

# Estabelecendo a conexão com o Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Pegando os dados existentes da planilha/banco
existing_data = conn.read(worksheet="Dados", usecols=list(range(7)), ttl=5)
existing_data = existing_data.dropna(how="all")

base = existing_data

# Verificar e corrigir valores inválidos nas colunas de hora
base['Hr_inicio'] = pd.to_datetime(base['Hr_inicio'], format='%H:%M:%S', errors='coerce')
base['Hr_final'] = pd.to_datetime(base['Hr_final'], format='%H:%M:%S', errors='coerce')
base = base.dropna(subset=['Hr_inicio', 'Hr_final'])

# Converter a coluna 'Data' para o formato datetime
base['Data'] = pd.to_datetime(base['Data'], errors='coerce')

# Calcular o total de horas trabalhadas para cada entrada
base['Horas_trabalhadas'] = (base['Hr_final'] - base['Hr_inicio']).dt.total_seconds() / 3600

# Seleção de projeto pelo usuário
projeto_selecionado = st.selectbox("Selecione o projeto", base['Projeto'].unique())

# Filtrar os dados pelo projeto selecionado
filtro_projeto = base[base['Projeto'] == projeto_selecionado]

df_projeto_ordenado = filtro_projeto.sort_values(by='Data')

data_inicial_projeto = df_projeto_ordenado.iloc[0,5]
df_filtro_dt_termino = existing_data[
    (existing_data['Projeto'] == projeto_selecionado) &
    (existing_data['Data_termino'].notna())
]

if not df_filtro_dt_termino.empty:
    data_final_projeto = df_filtro_dt_termino.iloc[0,6]
else:
    data_final_projeto = 'Não finalizado.'

# Seleção de intervalo de datas pelo usuário
intervalo_datas = st.date_input("Selecione o intervalo de datas", [])

# Verificar se o usuário selecionou duas datas
if len(intervalo_datas) == 2:
    data_inicio, data_fim = intervalo_datas
    # Aplicar o filtro de data
    filtro_projeto = filtro_projeto[(filtro_projeto['Data'] >= pd.to_datetime(data_inicio)) &
                                    (filtro_projeto['Data'] <= pd.to_datetime(data_fim))]

# Calcular o total de horas trabalhadas por área para o projeto e período selecionados
horas_por_area = filtro_projeto.groupby('Area')['Horas_trabalhadas'].sum().reset_index()

# Criar o gráfico com todas as áreas para o projeto e período selecionados
fig = px.bar(horas_por_area, x='Area', y='Horas_trabalhadas', title="Total de Horas Trabalhadas por Área")
st.plotly_chart(fig)

st.info(f"Data de inicio: {data_inicial_projeto}")
st.info(f"Data de término: {data_final_projeto}")