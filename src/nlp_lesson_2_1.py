import numpy as np

# Lesson-2 - "Структура и принцип работы полносвязных нейронных сетей (со ступенчатой активационной функцией)"
# Example-2 Полносвязная сеть прямого распространения / Fully meshed feedforward network
# Source: https://proproprogs.ru/neural_network/struktura-i-princip-raboty-polnosvyaznyh-neyronnyh-setey
# Comments: В примере рассмотрена НС с одним скрытым слоем нейронов, с одной разделяющей гиперплоскости, без смещения.

def act(x): # << функция активации
    return 0 if x < 0.5 else 1


def go(house, rock, attr):
    x = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weight1 = np.array([w11, w12])  # матрица 2x3
    weight2 = np.array([-1, 1])  # вектор 1х3

    sum_hidden = np.dot(weight1, x)  # вычисляем сумму на входах нейронов скрытого слоя
    print("Значения сумм на нейронах скрытого слоя: " + str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print("Значения на выходах нейронов скрытого слоя: " + str(out_hidden))

    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)
    print("Выходное значение НС: " + str(y))

    return y


house = 1
rock = 0
attr = 1

res = go(house, rock, attr)
if res == 1:
    print("Ты мне нравишься")
else:
    print("Созвонимся")
