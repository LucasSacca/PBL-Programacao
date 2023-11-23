import numpy as np
import pandas as pd
import streamlit as st

# Carregamento de dados
db = pd.read_csv('dados-dengue.csv', sep=';')

# Header
st.header("Painel de Monitoramento de Dengue no Brasil")

# Subheader
st.subheader('Mapa', divider='rainbow')

# Fintrando dados (apenas um teste aqui)
db_filt = db.dropna().query('Ano == 2015')

db_filt = db_filt.astype({'Latitude':float, 'Longitude':float})

# Mostrando mapa para o usuário
st.map(
    data = db_filt,
    latitude = 'Latitude',
    longitude = 'Longitude'
)
