# Example: 2_2  Простейший персептрон для задачи классификации двух классов образов.
import numpy as np
import matplotlib.pyplot as plt

N = 5 # задаем кол-во образов для каждого класса
b = 3 # задаем смещение

x1 = np.random.random(N) # генерируем произвольный набор значений Х1, класса С1
x2 = x1 + [np.random.randint(10)/10 for i in range(N)] + b # вычисляем Х2 значения с учетом случайно сгенерированного отклонения от точки Х1, класса С1
C1 = [x1, x2] # формируем массив точек из Х1 и Х2 для класса С1

x1 = np.random.random(N)  # генерируем произвольный набор значений Х1, класса С2
x2 = x1 - [np.random.randint(10)/10 for i in range(N)] - 0.1 + b # вычисляем Х2 значения с учетом случайно сгенерированного отклонения от точки Х1, класса С2
C2 = [x1, x2] # формируем массив точек из Х1 и Х2 для класса С2

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