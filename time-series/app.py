#Importação das bibliotecas
import streamlit as st 
import pandas as pd
import joblib
from joblib import load
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import timedelta
from prophet import Prophet
from matplotlib import dates

#carrega dados de prod
file = 'https://raw.githubusercontent.com/mayke-ilzu/portfolio/20eb0a93b4b6a5770b21ac6b7e5b1e554b3ff4e1/time-series/prod_data/oil_price_hist.csv'
oil = pd.read_csv(file,parse_dates=['ds'],names=['ds','y'],header=None,skiprows=1)

#setando estilo do gráfico
sns.set_style("darkgrid")


############################# Streamlit ############################
st.markdown('<style>div[role="listbox"] ul{background-color: #6e42ad}; </style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; '> Previsão do preço do barril de petróleo Brent</h1>", unsafe_allow_html = True)

st.markdown("Preço por barril do petróleo bruto tipo Brent. Produzido no Mar do Norte (Europa), Brent é uma classe de petróleo bruto que serve como benchmark para o preço internacional de diferentes tipos de petróleo.Neste caso, é valorado no chamado preço FOB (free on board), que não inclui despesa de frete e seguro no preço.")
st.markdown("Mais informações: https://www.eia.gov/dnav/pet/TblDefs/pet_pri_spt_tbldef2.asp")
st.markdown("Fonte dos dados: http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view")

              
#gerando gráfico com preço histórico
st.markdown("## Preço histórico")

fig = plt.figure(figsize=(16,8))
plt.plot(oil.ds, oil.y)
plt.title('Preço do barril de petróleo Brent por dia',fontsize=30)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Data',fontsize=20)
plt.ylabel('Preço do barril de petróleo',fontsize=20)
st.pyplot(fig)

#st.warning('Preencha o formulário com todos os seus dados pessoais e clique no botão **ENVIAR** no final da página.')

st.markdown("## Previsão do preço")

st.write('### Quantidade de dias')
days_to_predict = float(st.slider('Informe a quantidade de dias úteis que gostaria de prever', 1, 10))


#Predições 
if st.button('Enviar'):
    #recuperando proximos x dias uteis
    last_date = oil.ds.max()
    future_dates = []
    total_days = 0
    iterator = 1

    while total_days < days_to_predict:
        next_day = last_date + timedelta(days = iterator)
        if next_day.weekday() not in [5,6]:
            future_dates.append(next_day)
        iterator = iterator + 1
        total_days = len(future_dates)

    future_dates = pd.DataFrame(future_dates,columns=['ds'])

    #carregando modelo
    model = joblib.load('prophet_time_series.joblib')

    #realizando previsão
    forecast = model.predict(future_dates)

    #gerando gráfico com preço histórico
    st.markdown("### Preços previstos")

    fig = plt.figure(figsize=(20,8))
    ax = sns.lineplot(data=forecast,x='ds',y='yhat',marker="o")
    ax.set(xticks=forecast.ds.values)
    ax.xaxis.set_major_formatter(dates.DateFormatter("%d-%m-%y"))
    plt.title('Previsão do preço do barril de petróleo Brent por dia',fontsize=30)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=20)
    plt.xlabel('Data',fontsize=20)
    plt.ylabel('Previsão do preço do barril de petróleo',fontsize=20)
    st.pyplot(fig)

    #gerando gráfico com preço histórico
    st.markdown("**Obs**: previsões realizadas com base na última data disponível na base de dados que é " + str(last_date.strftime('%d/%m/%Y')))
