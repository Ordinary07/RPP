import os  # Импорт модуля для работы с операционной системой
import os.path  # Импорт модуля для работы с путями к файлам
import csv  # Импорт модуля для работы с CSV файлами

def parse_csv(path):
    """
    Функция для парсинга данных из CSV файла.

    Args:
        path (str): Путь к CSV файлу.

    Returns:
        dict: Словарь с данными из CSV файла.
    """
    got_data = {}
    with open(path, "r", encoding='cp1251') as raw_csv:
        csv_reader = csv.reader(raw_csv)
        for idx, row in enumerate(csv_reader, start=1):
            if len(row) == 5:
                number, dateTime, plateNumber, carModel = row
                got_data[idx] = {"number": int(number), "dateTime": dateTime, "plateNumber": plateNumber, "carModel": carModel}
            else:
                print(f"Некорректные данные в строке {idx}")
    return got_data

def sorted_by_carModel(d):
    """
    Функция для сортировки данных по марке автомобиля.

    Args:
        d (dict): Словарь с данными.

    Returns:
        dict: Отсортированный словарь по марке автомобиля.
    """
    return dict(sorted(d.items(), key=lambda item: item[1]["carModel"]))

def sorted_by_number(d):
    """
    Функция для сортировки данных по номеру.

    Args:
        d (dict): Словарь с данными.

    Returns:
        dict: Отсортированный словарь по номеру.
    """
    return dict(sorted(d.items(), key=lambda item: item[1]["number"]))

def select_more_than(d, value):
    """
    Функция для выбора данных с номером автомобиля больше указанного значения.

    Args:
        d (dict): Словарь с данными.
        value (int): Значение для сравнения.

    Returns:
        dict: Словарь с данными, удовлетворяющими условию.
    """
    return {k: v for k, v in d.items() if v["number"] > value}

def print_data(data):
    """
    Функция для вывода данных на экран.

    Args:
        data (dict): Словарь с данными.
    """
    for k, v in data.items():
        print(
            f"Запись №{k}: номер = {v['number']}, дата и время = {v['dateTime']}, номерной знак = {v['plateNumber']}, марка автомобиля = {v['carModel']}")

def add_new_data(path, d, number, dateTime, plateNumber, carModel):
    """
    Функция для добавления новых данных в CSV файл и словарь.

    Args:
        path (str): Путь к CSV файлу.
        d (dict): Словарь, куда добавляются данные.
        number (int): Номер автомобиля.
        dateTime (str): Дата и время.
        plateNumber (str): Номерной знак.
        carModel (str): Марка автомобиля.
    """
    with open(path, "a", encoding='utf-8') as f:
        idx = len(d) + 1
        f.write(f"{idx},{number},{dateTime},{plateNumber},{carModel}\n")
        d[idx] = {"number": number, "dateTime": dateTime, "plateNumber": plateNumber, "carModel": carModel}

def get_files_count_in_directory(path):
    """
    Функция для подсчета количества файлов в директории.

    Args:
        path (str): Путь к директории.

    Returns:
        int: Количество файлов в указанной директории.
    """
    if not os.path.exists(path):
        print(f"Директория '{path}' не существует.")
        return 0
    _, _, files = next(os.walk(path), (None, None, []))
    return len(files)

dir_path = input("Введите путь к директории: ")  # Получаем путь к директории от пользователя
print(f"Количество файлов в папке: {get_files_count_in_directory(dir_path)}")  # Выводим количество файлов в указанной директории

data = parse_csv(os.path.join(dir_path, "data.csv"))  # Получаем данные из CSV файла
print("\nОтсортировано по марке автомобиля:")  # Выводим сообщение о сортировке по марке автомобиля
print_data(sorted_by_carModel(data))  # Выводим отсортированные данные по марке автомобиля
print("\nОтсортировано по номеру:")  # Выводим сообщение о сортировке по номеру
print_data(sorted_by_number(data))  # Выводим отсортированные данные по номеру
print("\nТолько строки с номером автомобиля больше 500:")  # Выводим сообщение о выборе строк с номером автомобиля больше 500
print_data(select_more_than(data, 500))  # Выводим отфильтрованные данные

# Пример добавления новых данных
add_new_data(os.path.join(dir_path, "data1.csv"), data, 12341, "15.05.2021", "#43424", "Камаз")  # Добавляем новые данные
add_new_data(os.path.join(dir_path, "data.csv"), data, 423, "21.11.2023", "#4321", "УАЗ")  # Добавляем новые данные
add_new_data(os.path.join(dir_path, "data.csv"), data, 231, "11.02.2023", "#4241", "Ниссан")  # Добавляем новые данные
