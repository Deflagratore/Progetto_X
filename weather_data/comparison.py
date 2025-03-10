import matplotlib.pyplot as plt
from sitka import highs1, lows1, dates
from death_valley import highs2, lows2

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

t_p_s = highs1
t_pb_s = lows1
c_dates = dates
t_p_dv = highs2
t_pb_dv = lows2

titolo = "Comparazione temperature della\ndeath valley e sitka, 2021"

ax.plot(dates, t_p_s, color="red", alpha=0.5)
ax.plot(dates, t_p_dv, color="m", alpha=0.5)

ax.fill_between(dates, t_p_s, t_p_dv, facecolor="y", alpha=0.1)

ax.plot(dates, t_pb_s, color='b', alpha=0.5)
ax.plot(dates, t_pb_dv, color='c', alpha=0.5)

ax.fill_between(dates, t_pb_s, t_pb_dv, facecolor="g", alpha=0.1)

ax.set_title(titolo, fontsize=24)

ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperatura (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()