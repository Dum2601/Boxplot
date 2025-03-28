import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
  numero_aleatorio = random.randint(0, 10)
  vetor.append(numero_aleatorio)

graph_name = 'boxplot'

plt.boxplot(vetor)
plt.title(graph_name)
plt.show()
