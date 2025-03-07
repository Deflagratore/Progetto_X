import plotly.express as px
from dadi import Dado

dado = Dado()

risultati = []

for rollata in range(1_000_000):
    risultato = dado.roll()
    risultati.append(risultato)

frequenze = []

poss_result = range(1, dado.num_sides + 1)

for value in poss_result:
    frequenza = risultati.count(value)
    frequenze.append(frequenza)

titolo = "Risultati di 1 milione di lanci di dadi" #aggiunge il titolo al grafico
labels = {"x": "Risultato", "y": "Frequenza del risultato"} #questo codice aggiunge all'asse x e y dei titoli

fig = px.bar(x=poss_result, y=frequenze, title=titolo, labels=labels) #implementa i cambiamenti fatti sopra

fig.show()