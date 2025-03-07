import plotly.express as px
from dadi import Dado

dado = Dado()
dado2 = Dado(10)

risultati = []

for rollata in range(1_000_000): #calcola i risultati del lancio dei dadi
    risultato = dado.roll() + dado2.roll()
    risultati.append(risultato)

frequenze = []

risultato_massimo = dado.num_sides + dado2.num_sides

poss_result = range(2, risultato_massimo + 1)

for value in poss_result: #calcola la frequenza dei risultati
    frequenza = risultati.count(value)
    frequenze.append(frequenza)

titolo = "Risultati di 1 milione di lanci da 2 dadi (1=D6, 2=D10)" #aggiunge il titolo al grafico
labels = {"x": "Risultato", "y": "Frequenza del risultato"} #questo codice aggiunge all'asse x e y dei titoli

fig = px.bar(x=poss_result, y=frequenze, title=titolo, labels=labels) #implementa i cambiamenti fatti sopra

fig.update_layout(xaxis_dtick=1) #sistema il layout per far si che si vedano tutti i numeri dell'asse x

domanda = input("Vuoi salvare il grafico? ")

if domanda == "si":
    fig.write_html("grafico_lancio_dati.html") #salva la figura
else:
    fig.show() #mostra la figura