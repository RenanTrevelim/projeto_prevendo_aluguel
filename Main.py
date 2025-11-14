import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title='Preço Aluguel Hospedagem', layout='centered')

st.title('Previsão de Preço de Aluguel para Hospedagem')

with st.expander("Como funciona a previsão de preço?"):
    st.write("""
    O sistema utiliza técnicas de **Machine Learning** para estimar o valor do aluguel da hospedagem 
    para 2 diárias de até 4 pessoas. A base de dados contém as seguintes informações:

    - **valor**: preço do aluguel (variável que queremos prever);
    - **area**: área da hospedagem em metros quadrados;
    - **dist_praia**: distância até a praia mais próxima, em quilômetros;
    - **dist_mercado**: distância até o mercado mais próximo, em quilômetros;
    - **piscina**: indica se a hospedagem possui piscina (1 = sim, 0 = não).

    O processo de previsão é dividido em três etapas principais:

    1. **Preparação dos Dados**: 
       As variáveis são analisadas para verificar quais realmente têm relação com o preço do aluguel.
       Em seguida, algumas colunas numéricas, como área e distâncias, passam por uma transformação 
       utilizando o **logaritmo**, o que ajuda o modelo de regressão a lidar melhor com valores muito 
       altos ou muito baixos e torna a relação com o preço mais estável.

    2. **Treinamento do Modelo (XGBoost Regressor)**:
       Utilizamos o **XGBoost**, um modelo de regressão baseado em várias árvores de decisão que 
       aprendem em conjunto. Ele estuda como o preço varia de acordo com área, distâncias e presença 
       de piscina, ajustando seus parâmetros para minimizar o erro de previsão.

    3. **Previsão do Preço de Aluguel**:
       Quando o usuário informa os dados de uma nova hospedagem, essas informações passam pelas 
       mesmas transformações usadas no treinamento (incluindo o log das variáveis numéricas) e são 
       enviadas para o modelo XGBoost. 
       O modelo então retorna o valor estimado do aluguel em reais para aquela combinação de atributos.

    Dessa forma, o sistema consegue fornecer uma estimativa de preço consistente, baseada em padrões 
    observados em diversas hospedagens reais.
    """)

modelo_xgb = joblib.load('modelo.pkl')

area = st.number_input('Área da hospedagem (m²):', min_value=1, step=1, format="%d")
dist_praia = st.number_input('Distância até a praia mais próxima (km):', min_value=0.0, format="%.2f")
dist_mercado = st.number_input('Distância até o mercado mais próximo (km):', min_value=0.0, format="%.2f")
piscina = st.selectbox('A hospedagem possui piscina?', options=['Sim', 'Não'])
piscina = 1 if piscina == 'Sim' else 0

enviar = st.button('Prever Preço de Aluguel')

if enviar:
    if area == '' or dist_praia == '' or dist_mercado == '':
        st.warning('Por favor, preencha todos os campos antes de enviar.')
    else:
        entrada = [[np.log(area), np.log(dist_praia + 1),piscina ]]

        st.write(f'Valor previsto do Aluguel : R$ {np.exp(modelo_xgb.predict(entrada)[0]):.2f}')