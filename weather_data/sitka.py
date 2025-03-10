import csv
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_simple.csv')

lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)

header_row = next(reader)

dates, highs1, lows1 = [], [], []

for row in reader:
    low = int(row[5])
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    highs1.append(high)
    dates.append(current_date)
    lows1.append(low)

plt.style.use('seaborn-v0_8')

fig, ax =plt.subplots()

ax.plot(dates, highs1, color="red", alpha=0.5) #l'argomento alpha controlla la trasparenza
ax.plot(dates, lows1, color='blue', alpha=0.5)
ax.fill_between(dates, highs1, lows1, facecolor='blue', alpha=0.1) #colora lo spazio tra i punti
ax.set_title("Le temperature piu alte del 2021 a sitka", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #mette le date nel grafico
ax.set_ylabel('Temperatura (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()