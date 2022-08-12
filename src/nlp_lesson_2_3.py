import numpy as np
import matplotlib.pyplot as plt

# Lesson: 1-3 - "Персептрон - возможности классификации образов, задача XOR"
# Example: 1-3 Решение задачи XOR с одним скрытым слоем нейронов, с двумя разделяющими гиперплоскостями, со смещением. Простейший персептрон для задачи классификации двух классов образов
# Source: https://proproprogs.ru/neural_network/perseptron-vozmozhnosti-klassifikacii-obrazov-zadacha-xor
# YouTube: https://www.youtube.com/watch?v=t9QfcFNkG58&list=PLA0M1Bcd0w8yv0XGiF1wjerjSZVSrYbjh
# Comments: В примере рассмотрено решение задачи XOR с одним скрытым слоем нейронов, с двумя разделяющими гиперплоскостями, со смещением.

def act(x):
    return 0 if x <= 0 else 1

def go(C):
    x = np.array([C[0], C[1], 1])
    w1 = [1, 1, -1.5]
    w2 = [1, 1, -0.5]
    w_hidden = np.array([w1, w2])
    w_out = np.array([-1, 1, -0.5])

    sum = np.dot(w_hidden, x)
    out = [act(x) for x in sum]
    out.append(1)
    out = np.array(out)

    sum = np.dot(w_out, out)
    y = act(sum)
    return y

C1 = [(1,0), (0,1)]
C2 = [(0,0), (1,1)]

print( go(C1[0]), go(C1[1]) )
print( go(C2[0]), go(C2[1]) )