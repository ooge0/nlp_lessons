import numpy as np

# Lesson: 1-2 - "Персептрон - возможности классификации образов, задача XOR"
# Example: 1-2 Простейший персептрон для задачи классификации двух классов образов. НС без скрытого слоя нейронов, с одной разделяющей гиперплоскости, без смещения.
# Source: https://proproprogs.ru/neural_network/perseptron-vozmozhnosti-klassifikacii-obrazov-zadacha-xor
# YouTube: https://www.youtube.com/watch?v=t9QfcFNkG58&list=PLA0M1Bcd0w8yv0XGiF1wjerjSZVSrYbjh
# Comments: В примере рассмотрена НС без скрытого слоя нейронов, с одной разделяющей гиперплоскости, без смещения.

import numpy as np
import matplotlib.pyplot as plt

N = 5
b = 3

x1 = np.random.random(N)
x2 = x1 + [np.random.randint(10)/10 for i in range(N)] + b
C1 = [x1, x2]

x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10)/10 for i in range(N)] - 0.1 + b
C2 = [x1, x2]

f = [0+b, 1+b]

w2 = 0.5
w3 = -b*w2
w = np.array([-w2, w2, w3])
for i in range(N):
    x = np.array([C1[0][i], C1[1][i], 1])
    y = np.dot(w, x)
    if y >= 0:
        print("Класс C1")
    else:
        print("Класс C2")

plt.scatter(C1[0][:], C1[1][:], s=10, c='red')
plt.scatter(C2[0][:], C2[1][:], s=10, c='blue')
plt.plot(f)
plt.grid(True)
plt.show()