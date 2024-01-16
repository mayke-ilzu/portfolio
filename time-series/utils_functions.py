import pandas as pd
import numpy as np

#função para transformar os dados
def transform_data(df):
    #renomeando as colunas e removendo primeira linha que era o header original
    df_clean = df.copy()
    df_clean.columns = ['date','oil_price']
    df_clean.drop(df_clean.index[0],inplace=True)
    #altera tipo de dados e corrige decimal
    df_clean['date'] = pd.to_datetime(df_clean["date"], format="%d/%m/%Y")
    df_clean['oil_price'] = df_clean['oil_price'].astype('float64')
    df_clean['oil_price'] = df_clean['oil_price'] / 100
    return df_clean

#função para carga incremental
def incremental_ipea_data(html_link):
    #importa os dados
    stage_ipea = pd.read_html(html_link,encoding='UTF-8')
    #cria dataframe
    df_stage_ipea = stage_ipea[2].copy()
    #transforma os dados
    df_stage_ipea_clean = transform_data(df_stage_ipea)
    #carrega dados de produção (se não existirem faz processo full)
    try:
        prod_ipea = pd.read_csv('C:/Users/mayke/Documents/Cursos/Fiap/fiap/tech-challenge/fase-4/ipea/prod_data/oil_price_hist.csv',parse_dates=['date'])
        #recupera maior data na base de prod
        prod_last_date = prod_ipea['date'].max()
        #filtra em stage apenas dados que ainda não foram carregados em prod
        stage_ipea_final = df_stage_ipea_clean[df_stage_ipea_clean['date'] > prod_last_date]
        #reordena pela data
        stage_ipea_final = stage_ipea_final.sort_values(by='date')
        #grava os dados em prod
        stage_ipea_final.to_csv('C:/Users/mayke/Documents/Cursos/Fiap/fiap/tech-challenge/fase-4/ipea/prod_data/oil_price_hist.csv',index=False,mode='a',header=False)
        #printa volumetria carregada
        print('*****Carga incremental*****\nDados carregados: {}'.format(stage_ipea_final.count()['date']))
    except:
        #carga full caso não consiga fazer incremental
        df_stage_ipea_clean = df_stage_ipea_clean.sort_values(by='date')
        df_stage_ipea_clean.to_csv('C:/Users/mayke/Documents/Cursos/Fiap/fiap/tech-challenge/fase-4/ipea/prod_data/oil_price_hist.csv',index=False)
        print('*****Carga full*****\nDados carregados: {}'.format(df_stage_ipea_clean.count()['date']))