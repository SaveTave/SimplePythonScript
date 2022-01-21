"""Programma per il calcolo delle Exponential Moving Average (SMA),
output del grafico in uscita con l'importazione dei dati tramite Yahoo Finance
mediante l'inserimento di inputa da parte dell'utente"""

#Librerie richieste
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Limite massimo righe output
pd.options.display.max_rows = 5000

#Input dell'utente

Coin = input("Inserisci la coin scelta, es: BTC-USD:")

periodo = input("Inserisci il periodo tra quelli visualizzati: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd:")

intervallo = input("Inserisci il timeFrame tra quelli visualizzati: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo:")

#Importazione dei dati

data = yf.download(
    tickers= Coin,

#Periodo scelto (5d = 5 giorni)   
period= periodo,

#TimeFrame
interval = intervallo,

#Setta tutto OHLC automatico
auto_adjust = True,
)

#Colonna PrevClose (chiusure del giorno prima) 
data ["PrevClose"] = data.Close.shift(1)
data.head(10)


#EMA 60
data['EMA60'] = data['Close'].ewm(span=60).mean()

#EMA 223

data['EMA223'] = data['Close'].ewm(span=223).mean()

data.tail()

print(data)


plt.figure(figsize=(12.2,4.5), dpi=100)
plt.plot(data.Close, color='green',linewidth=1.6)
#plt.plot(data.EMA5, color='red', linewidth=0.5)
#plt.plot(data.EMA10, color='yellow', linewidth=0.5)
plt.plot(data.EMA60, color='blue', linewidth=0.8)
plt.plot(data.EMA223, color='purple', linewidth=0.8)
plt.xlabel("Tempo", fontsize = 15)
plt.ylabel("Prezzi", fontsize = 15)
plt.title(Coin, fontsize = 15)
plt.grid(True)
plt.show()