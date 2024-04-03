#Библиотека, отвечающая за рандом
import random

#Выполняет задачу удаления из первого массива чётных цепочек, в которых нет ни одного элемента второго массива
#Этот метод работает следующим образом:
#Сначала находятся 2 точки цепочки - начало цепочки и её конец.
#Во время прохода по циклу индекс первой точки записывается в переменную point, а вторая определяется по условию
#того, что предыдущий элемент нечётный, а следующий чётный.
#Как только отрезок найден, проверяется, есть ли в нём элемент из списка B, если есть, то он удалется с помощью del
#После того, как удаление завершено, цикл запускается заново, тк индексы в массиве сбились. Это продолжается до тех пор, пока
#x не дойдёт до конца массива
def task(A, B):
    point = -1 #Указывает на первую точку цепочки
    loop = True

    while loop:
        for x in range(len(A)):
            if x > 0 and A[x] % 2 == 1 and A[x - 1] % 2 == 0:
                h = False
                for y in range(point + 1, x):
                    for z in range(len(B)):
                        if not h:
                            h = A[y] == B[z]
                if h:
                    del A[point + 1:x]
                    loop = True
                    break

            if A[x] % 2 == 1:
                point = x
            loop = False

def taskWithSet(A, B):
    S = set(B) #Множество
    P = set() #Множество
    point = -1  # Указывает на первую точку цепочки
    loop = True

    while loop:
        for x in range(len(A)):
            if x > 0 and A[x] % 2 == 1 and A[x - 1] % 2 == 0:
                P.clear()
                for y in range(point + 1, x):
                    P.add(A[y])
                if not S.isdisjoint(P): #Фунцкия isdisjoint() возвращает true, если в множествах нет одинаковых элементов
                    del A[point + 1:x]
                    loop = True
                    break

            if A[x] % 2 == 1:
                point = x
            loop = False

#Принимает два массива A и B от пользователя, проверяет корректность ввода данных,
#а затем выводит массив A, обработанный методом task(A, B)
def withInput(std):
    A = list()
    B = list()
    noCorrect = True
    while noCorrect:
        #try првоеряет на корректность ввода данных
        try:
            #Метод split разбивает строку на массив строк через пробелы. Метод map преобразует строки в int.
            A = list(map(int, input("Введите массив A: ").split()))
            B = list(map(int, input("Введите массив B: ").split()))
            noCorrect = False
        except:
            print("Некорректно введены входные данные.")
            noCorrect = True

    if std:
        taskWithSet(A, B)
    else:
        task(A, B)
    print("Массив A после обработки: ", A)

#Создаёт 2 массива случайной длины и со случайными значениями, а затем обрабатывает массив A с помощью функции task()
def withRandom(std):
    countA = random.randint(10, 15)
    countB = random.randint(10, 15)
    A = [random.randint(0, 100) for x in range(countA)]
    B = [random.randint(0, 100) for x in range(countB)]

    print("Массив A: ", A)
    print("Массив B: ", B)
    if std:
        taskWithSet(A, B)
    else:
        task(A, B)
    print("Массив A после обработки: ", A)

withInput(True)