#import das libs
import pandas as pd
import numpy as np
from prophet import Prophet
from datetime import timedelta
import joblib
import warnings
warnings.filterwarnings("ignore")

#carrega dados de prod
file = 'C:\\Users\\mayke\\Documents\\Cursos\\Fiap\\fiap\\tech-challenge\\fase-4\\ipea\\prod_data\\oil_price_hist.csv'
oil = pd.read_csv(file,parse_dates=['ds'],names=['ds','y'],header=None,skiprows=1)

#recuperando proximos 10 dias uteis
last_date = oil.ds.max()
future_dates = []
total_days = 0
iterator = 1

while total_days < 10:
    next_day = last_date + timedelta(days = iterator)
    if next_day.weekday() not in [5,6]:
        future_dates.append(next_day)
    iterator = iterator + 1
    total_days = len(future_dates)

future_dates = pd.DataFrame(future_dates,columns=['ds'])

#carregando modelo
model = joblib.load('C:\\Users\\mayke\\Documents\\Cursos\\Fiap\\fiap\\tech-challenge\\fase-4\\ipea\\prophet_time_series.joblib')

#realizando previsão
forecast = model.predict(future_dates)

#exporta forecast
forecast.to_csv('C:/Users/mayke/Documents/Cursos/Fiap/fiap/tech-challenge/fase-4/ipea/prod_data/oil_price_forecast_10d.csv',index=False)