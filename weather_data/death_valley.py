import csv
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

path = Path('weather_data/death_valley_2021_simple.csv')

lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)

header_row = next(reader)

dates, highs2, lows2 = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        low = int(row[4])
        high = int(row[3])
    except ValueError:
        print(f"Dati mancanti per {current_date}")
    else:
        highs2.append(high)
        dates.append(current_date)
        lows2.append(low)

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

titolo = "Le temperature piu alte della death valley nel 2021"

ax.plot(dates, highs2, color="red", alpha=0.5) #l'argomento alpha controlla la trasparenza
ax.plot(dates, lows2, color='blue', alpha=0.5)
ax.fill_between(dates, highs2, lows2, facecolor='blue', alpha=0.1) #colora lo spazio tra i punti
ax.set_title(titolo, fontsize=22)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #mette le date nel grafico
ax.set_ylabel('Temperatura (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()