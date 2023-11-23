import pandas as pd
import streamlit as st
from PIL import Image



opcoes = ['Selecione uma opção', 'Camaleão', 'Cruzadas','Bactéria 1', 'Bactéria 2']

texto = st.selectbox('Escolha uma opção',opcoes)


img = Image.open('camaleao.png')

# Verifica o texto digitado pelo usuário e exibe o resultado correspondente
if texto.lower() == 'camaleão':
    st.image(img)
    
elif texto.lower() == 'cruzadas':
    st.write('As Cruzadas foram uma série de expedições militares de caráter religioso organizadas pelos cristãos da Europa Ocidental com o objetivo de conquistar Jerusalém e os lugares sagrados do Cristianismo no Oriente Médio.')

elif texto.lower() == 'bactéria 1':
    img = Image.open('dashboard_bacteria1.png')
    st.image(img)

elif texto.lower() == 'bactéria 2':
    img = Image.open('dashboard_bacteria2.png')
    st.image(img)




