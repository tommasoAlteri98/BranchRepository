import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

giorni = 305
mediaVisitatori = 1200
deviazioneStd = 900
trendDecrescente = np.linspace(0, 600, giorni)

date_range = pd.date_range(start='2002-02-18', periods = giorni, freq='D')

np.random.seed(42)

visitatori = np.random.normal(loc = mediaVisitatori, scale = deviazioneStd, size = giorni)

visitatori = visitatori - trendDecrescente
visitatori = np.maximum(visitatori, 0)  #no negativi

patologie = np.random.choice(['ossa', 'cuore', 'testa'], size=giorni)

df = pd.DataFrame({'Visitatori': visitatori, 'Patologia': patologie}, index=date_range)
df.head()

plt.figure(figsize=(12, 6))
plt.plot(df['Visitatori'], label='Visitatori giornalieri', color='b')
plt.xlabel('Data')
plt.ylabel('Numero di Visitatori')
plt.title('Grafico del numero di visitatori giornalieri in ospedale')
plt.legend()
plt.grid()
plt.show()
