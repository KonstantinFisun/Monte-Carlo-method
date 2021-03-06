import math
import random
import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return math.sqrt(11 - 4 * pow(math.sin(x), 2))

# Построение графика и вычисление интеграла
def plotttingTriangle(N):
    b = 3.5
    a = 5
    e = 0.01

    # Массивы случайных точек
    # xPoints = [random.uniform(0, a) for i in range(N)]
    # yPoints = [random.uniform(0, b) for i in range(N)]

    xPoints = np.random.uniform(0, a, N)
    while (xPoints.mean() - a / 2 >= e) or (xPoints.var() - a * a / 12 >= e):
        xPoints = np.random.uniform(0, a, N)

    yPoints = np.random.uniform(0, b, N)
    while (yPoints.mean() - b / 2 >= e) or (yPoints.var() - b * b / 12 >= e):
        yPoints = np.random.uniform(0, b, N)

    # Массив x-ов
    x = np.arange(0, 5, step=0.125)

    # Вычисление функции
    y = np.array([])
    for i in range(len(x)):
        y = np.append(y, function(x[i]))

    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Размер окна
    fig.set_figwidth(8)
    fig.set_figheight(8)

    # Удалить лишние пробелы
    fig.tight_layout()

    M = 0
    for i in range(N):
        if yPoints[i] < function(xPoints[i]):
            M += 1
            plt.scatter(xPoints[i], yPoints[i], s=10, color='red')
        else:
            plt.scatter(xPoints[i], yPoints[i], s=10, color='black')

    # Приближённая площадь
    S = round(M / N * a * b, 2)
    print(f"Интеграл по 1 формуле: {S}")

    # Ещё точнее
    S1 = 0
    for i in range(N):
        S1 += function(xPoints[i])
    S1 *= a / N
    S1 = round(S1, 4)
    print(f"Интеграл по 2 формуле: {S1}")

    ax.legend(fontsize=12,
              ncol=1,  # Количество столбцов
              facecolor='oldlace',  # Цвет области
              edgecolor='blue',  # Цвет крайней линии
              title=f'Всего генерируемых точек: {N} \n'
                    f'Приближённо интеграл равен: {S} \n'
                    f'Точное значение: 14.8598',
              title_fontsize='12',  # Размер шрифта
              loc="lower left"
              )
    # Границы оси Y
    plt.ylim([0, 3.5])

    plt.show()

def main():
    N = 2000 # Количество случайных точек
    plotttingTriangle(N) # Вызов функции



if __name__ == '__main__':
    main()