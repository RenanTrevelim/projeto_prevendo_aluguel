🏡 Previsão de Preço de Aluguel de Hospedagens

Usando Machine Learning (XGBoost) + Streamlit

Este projeto tem como objetivo prever o valor de aluguel de hospedagens com base em características como área, distância da praia, distância do mercado e presença de piscina.
O modelo utiliza XGBoost, um algoritmo poderoso para tarefas de regressão.

A aplicação foi desenvolvida em Python e disponibilizada via Streamlit, permitindo que o usuário insira os atributos da hospedagem e receba uma previsão instantânea.

🚀 Funcionalidades

Previsão automática do preço do aluguel.

Interface interativa construída com Streamlit.

Pré-processamento inteligente dos dados (log-transform para estabilizar variáveis).

Modelo XGBoost treinado com colunas selecionadas.

Carregamento do modelo via Joblib.

Entrada de dados simples e clara pelo usuário.

🧠 Como o modelo funciona?

O processo é dividido em etapas:

1. Pré-processamento

Remoção de colunas irrelevantes.

Transformação logarítmica em variáveis que possuem grande variação (como área e distâncias).

2. Treinamento

Uso do algoritmo XGBoost Regressor, conhecido por alta performance.

Ajuste dos hiperparâmetros.

Avaliação com métricas de regressão.

3. Deploy com Streamlit

Interface simples para coletar:

Área da hospedagem

Distância da praia

Distância do mercado

Piscina (sim/não)

Aplicação da mesma transformação usada no treino antes da previsão.

Retorno do valor previsto em reais.
