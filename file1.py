import math
import numpy

t=[0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]

def f(x):
  return math.exp(-x/5) - 1

def g(x):
  return - 200 + math.exp(-x/5) * 200

a = [f(x) for x in t]
b = [g(x) for x in t]

a = []
for x in t:
  y = f(x)
  a.append(y)

b = []
for x in t:
  z = g(x)
  b.append(z)


print(f"Esta é a lista de tempo usado para referência nos resultados: {t}\n")
print(f"Esta é a aceleração do corpo através do tempo (em m/s²): {a}\n")
print(f"Esta é a posição do corpo através do tempo (em m): {b}")
