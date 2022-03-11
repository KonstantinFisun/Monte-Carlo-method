import random
import numpy as np
import math

# Вычисленние приближенного значение pi
from matplotlib import pyplot as plt


def fun(N, R):
    zPoints = np.random.uniform(0, 2 * R, 2 * N)
    # print(zPoints.mean()) # Среднее значение
    # print(zPoints.var()) # Дисперсия

    xPoints = np.array([])

    for i in range(0, N):
        xPoints = np.append(xPoints, zPoints[i])

    yPoints = np.array([])

    for i in range(N, 2 * N):
        yPoints = np.append(yPoints, zPoints[i])

    M = 0

    for i in range(0, N):
        if((pow((xPoints[i] - R), 2) + pow((yPoints[i] - R), 2)) < R * R):
            M += 1

    # Вычисляем площадь
    S = (M / N) * pow((2 * R), 2)
    pi = S/(R * R)


    show(N, R, xPoints, yPoints, pi)  # Функция вызова графика

# Отрисовка графика
def show(N, R, xPoints, yPoints, pi):

    fig, ax = plt.subplots()

    x = np.linspace(0, 2 * np.pi, num = 150)

    # Вычисление точек круга заданных параметрических
    xG = np.array([])
    yG = np.array([])

    for i in range(len(x)):
        xG = np.append(xG, R + R * np.cos(x[i]))
        yG = np.append(yG, R + R * np.sin(x[i]))

    ax.plot(xG, yG)

    for i in range(0 , N):
        if ((pow((xPoints[i] - R), 2) + pow((yPoints[i] - R), 2)) < R * R):
            plt.scatter(xPoints[i], yPoints[i], s=10, color="red")
        else:
            plt.scatter(xPoints[i], yPoints[i], s=10, color="black")

    ax.legend(fontsize=12,
              ncol=1,  # Количество столбцов
              facecolor='oldlace',  # Цвет области
              edgecolor='blue',  # Цвет крайней линии
              title=f'Всего сгенерировано точек: {N} \n'
                    f'Приближённо значение pi: {pi}',
              title_fontsize='12',  # Размер шрифта
              loc="lower left"
              )

    fig.tight_layout()

    plt.ylim([0, R * 2])
    plt.xlim([0, R * 2])

    

    plt.show()

def main():
    N = 400 # Количество случайных точек
    R = 33 # Радиус
    fun(N, R)




if __name__ == '__main__':
    main()