import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=10)

ax.set_title("Numeri al quadrato", fontsize=25)
ax.set_xlabel("Numero", fontsize=14)
ax.set_ylabel("Numero al quadrato", fontsize=14)
ax.tick_params(labelsize=20)

plt.savefig("Numeriq.png", bbox_inches="tight")

plt.show()