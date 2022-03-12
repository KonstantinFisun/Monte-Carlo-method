import random
import numpy as np
import math
from matplotlib import pyplot as plt


# Функция заданная в полярных координатах
def polar(x):
    return np.sqrt(3 * pow(np.cos(x), 2) + 7 * pow(np.sin(x), 2))


# Отрисовка графика
def show(N):
    fig, ax = plt.subplots()

    x = np.linspace(0, 2 * np.pi, num=300)

    # Вычисление точек
    xG = np.array([])
    yG = np.array([])

    for i in range(len(x)):
        xG = np.append(xG, polar(x) * np.cos(x))
        yG = np.append(yG, polar(x) * np.sin(x))

    ax.plot(xG, yG)

    fig.tight_layout()

    a = 3
    b = 3

    xPoints = np.random.uniform(0, 2 * a, N) - a
    yPoints = np.random.uniform(0, 2 * b, N) - b

    M = 0


    for i in range(0, N):
        if (pp(xPoints[i], yPoints[i]) < polar(ff(xPoints[i], yPoints[i]))):
            plt.scatter(xPoints[i], yPoints[i], s=10, color="red")
            M += 1
        else:
            plt.scatter(xPoints[i], yPoints[i], s=10, color="black")

    S = M/N * (a * b * 4)

    ax.legend(fontsize=12,
              ncol=1,  # Количество столбцов
              edgecolor='blue',  # Цвет крайней линии
              title=f'Всего сгенерировано точек: {N} \n'
                    f'Приближённая площадь фигуры: {S}',
              title_fontsize='12',  # Размер шрифта
              loc="lower left"
              )

    plt.show()


def ff(x, y):
    if (x > 0):
        return math.atan(y / x)
    elif (x < 0):
        return math.atan(y / x) + math.pi
    elif (y > 0):
        return math.pi / 2
    else:
        return math.pi * 3 / 2

def pp(x, y):
    return math.sqrt((x * x) + (y * y))

def main():
    N = 179  # Количество генерируемых точек
    show(N)


if __name__ == '__main__':
    main()
