"""Programma per il calcolo delle Simple Moving Average (SMA),
output del grafico in uscita con l'importazione dei dati tramite Yahoo Finance"""

#Librerie richieste
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


#Limite massimo righe output
pd.options.display.max_rows = 5000


#Importazione dei dati

#data = yf.download("BTC-USD", start="2018-01-01", end="2022-01-02", interval= "1d")


data = yf.download(
    tickers="DOT-USD",

#Periodo scelto (es: 5d = 5 giorni)   
period= "1y",

#TimeFrame
interval = "1d",

#Setta tutto OHLC automatico
auto_adjust = True,
)

#Colonna PrevClose (chiusure del giorno prima) per il calcolo della SMA
data ["PrevClose"] = data.Close.shift(1)
data.head(10)

#SMA 5
data["SMA5"] = data.Close.rolling(5).mean()

#SMA 10
data["SMA10"] = data.Close.rolling(10).mean()

#SMA 60
data["SMA60"] = data.Close.rolling(60).mean()

#SMA 223
data["SMA223"] = data.Close.rolling(223).mean()

data.tail()

print(data)


plt.figure(figsize=(12.2,4.5), dpi=100)
plt.plot(data.Close, color='green',linewidth=1.6)
plt.plot(data.SMA5, color='red', linewidth=0.5)
plt.plot(data.SMA10, color='yellow', linewidth=0.5)
plt.plot(data.SMA60, color='blue', linewidth=0.8)
plt.plot(data.SMA223, color='purple', linewidth=0.8)
plt.xlabel("Tempo", fontsize = 15)
plt.ylabel("Prezzi", fontsize = 15)
plt.title("BTC_USD SMA 5", fontsize = 15)
plt.grid(True)
plt.show()
