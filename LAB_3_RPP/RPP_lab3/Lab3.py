from pathlib import Path
import csv


def filecount():
    folder_name = "venv"
    folder = Path(folder_name)
    folder_count = 0
    if folder.is_dir():
        folder_count = len([1 for file in folder.iterdir()])
    print(f"В папке {folder_name} есть {folder_count} объектов")
    print("Открываем файл data.csv...")


def write_csv():
    print('Добавление нового студента: ')
    key_inp = input('Введите id: ')
    fullname_inp = input('Введите ФИО: ')
    email_inp = input('Введите почту: ')
    group_inp = input('Введите группу: ')
    all_data[key_inp] = [fullname_inp, email_inp, group_inp]
    with open('data.csv', 'w') as out:  # Запись в файл
        for element in all_data:
            out.write(element + "," + all_data[element][0] + "," +
                      all_data[element][1] + "," + all_data[element][2] + "\n")
        out.close()


all_data = {}


def read_f():
    with open("data.csv", "r") as f:  # Чтение файла
        reader = csv.reader(f)
        for line in reader:
            all_data[line[0]] = line[1:]
        sort_full()


def sort_full():
    sorted_values = sorted(all_data.values(), key=lambda x: str(x[0]))  # Сортировка словаря Python по значению
    new_sorted_dictionary = {}
    for i in sorted_values:
        for k in all_data.keys():
            if all_data[k] == i:
                new_sorted_dictionary[k] = all_data[k]
                break
    print("Сортировка по фамилии: ")
    for elem in new_sorted_dictionary:  # Добавление отсортированных элементов в новый словарь
        print(elem + " -", *new_sorted_dictionary[elem])
    sort_id()


def sort_id():
    t = dict(sorted(all_data.items(), key=lambda x: int(x[0])))  # Сортировка по id
    print("")
    print("Сортировка по id: ")
    for i in t:
        print(i + " -", *t[i])
    print("")
    print("Учащиеся в группе ИВТАПбд-31: ")
    for elem in all_data:
        if all_data[elem][2] == 'IVTAP31':
            print(elem + " -", *all_data[elem])
    write_csv()


filecount()
read_f()

