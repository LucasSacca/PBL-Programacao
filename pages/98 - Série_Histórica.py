import pandas as pd
import streamlit as st

# Carregamento de dados
db = pd.read_csv('dados-dengue.csv', sep=';')

# Header
st.header("Painel de Monitoramento de Dengue no Brasil")

# Subheader
st.subheader('Série Histórica', divider='rainbow')

# Criando um filtro de dados
estado = st.selectbox(
    "Estado: ",
    ['Todos'] + list(db["UF de notificação"].unique())
)

if estado == 'Todos':

    db_filt = db
    paleta_cor = "UF de notificação"

else:

    db_filt = db[db["UF de notificação"] == estado]
    paleta_cor = None

# Mostrando o gráfico para o usuário
st.line_chart(
    data = db_filt,
    x = "Ano", 
    y = "Casos Prováveis", 
    color = paleta_cor
)

# Fazendo a pivot table (para obter a soma para todos os estados)
db_pivot = pd.pivot_table(
    data = db,
    index = 'Ano',
    values = 'Casos Prováveis',
    aggfunc = sum
).reset_index(drop=False)

# mostrando a tabela na tela do usuário
st.text('Dados agregados para o Brasil:')
st.bar_chart(
    data = db_pivot,
    x = 'Ano',
    y = 'Casos Prováveis'
)