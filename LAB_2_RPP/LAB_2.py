#Выполнить обработку элементов прямоугольной матрицы A,
#имеющей N строк и M столбцов. Найти сумму элементов всей матрицы.
#Определить, какую долю в этой сумме составляет сумма элементов
#каждого столбца. Результат оформить в виде матрицы из N + 1 строки M столбцов.

import numpy as np

# Функция сохранения матрицы в файл
def saveMatrix(a, M, N, f):
    for y in range(N):
        for x in range(M):
            f.write(str(a[y][x]) + " ")
        f.write('\n')

error = True
while error:
    try:
        M = int(input("Введите ширину таблицы: "))  # Количество столбцов матрицы
        N = int(input("Введите высоту таблицы: "))  # Количество строк матрицы
        error = False
    except ValueError:
        print("Ошибка: введите целые числа для ширины и высоты.")
        error = True

try:
    with open("text.txt", "w", encoding="utf-8") as f:  # Создание файла text.txt для записи
        a = np.random.randint(100, 999, size=(N, M))  # Матрица, заполненная случайными числами от 100 до 999

        f.write("Входная матрица: \n")
        saveMatrix(a, M, N, f)

        total_sum = np.sum(a.flatten())  # Сумма всех элементов матрицы

        # Массив, в котором будет храниться последняя строка матрицы с долями столбцов
        p = np.zeros(M)

        # Нахождение доли для каждого из столбцов
        for x in range(M):
            col_sum = np.sum(a[:, x])  # Сумма элементов столбца
            p[x] = round(col_sum / total_sum, 1)

        # Вставление строки в матрицу
        a = np.vstack([a, p])

        f.write('\n')
        f.write("Обработанная матрица: \n")
        saveMatrix(a, M, N + 1, f)

        print("Матрица успешно сохранена в файл text.txt")
except IOError:
    print("Ошибка при открытии/записи в файл.")
