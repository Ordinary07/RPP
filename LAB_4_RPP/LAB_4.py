import os, os.path

class Row():
    idx = 0

    def __init__(self, idx: int):
        self.idx = idx

    def get_idx(self):
        return self.idx

    def set_idx(self, val):
        self.idx = val

class RawModel(Row):
    idx = 0
    number = 0
    dateTime = ""
    plateNumber = ""
    carModel = ""

    def __init__(self, idx:int, number:int, dateTime:str, plateNumber:str, carModel:str):
        super().__init__(idx)
        self.idx = idx
        self.number = number
        self.dateTime = dateTime
        self.plateNumber = plateNumber
        self.carModel = carModel

    def __str__(self):
        return f"Запись №{self.idx}: номер = {self.number}, дата и время = {self.dateTime}, номерной знак = {self.plateNumber}, марка автомобиля = {self.carModel}"

    def __repr__(self):
        return f"RowModel(idx={self.idx},number={self.number},dateTime={self.dateTime},plateNumber={self.plateNumber},carModel={self.carModel})"

    def __setattr__(self, __name, __value):
        self.__dict__[__name] = __value


class Data():
    file_path = ""
    data = {}
    pointer = 0

    def __init__(self, path):
        self.file_path = path
        self.data = self.parse(path)

    def __str__(self):
        d_str = '\n'.join([str(rm) for rm in self.data])
        return f"Контейнер хранит в себе следущее:\n{d_str}"

    def __repr__(self):
        return f"Data({[repr(rm) for rm in self.data]})"

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer >= len(self.data):
            self.pointer = 0
            raise StopIteration
        else:
            self.pointer += 1
            return self.data[self.pointer - 1]

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом.")
        if 0 <= item < len(self.data):
            return self.data[item]
        else:
            raise IndexError("Неверный индекс.")

    def as_generator(self):
        self.pointer = 0
        while self.pointer < len(self.data):
            yield self.data[self.pointer]
            self.pointer += 1

    @staticmethod
    def parse(path):
        parsed = []
        with open(path, "r", encoding='utf-8') as raw_csv:
            for line in raw_csv:
                (idx, number, dateTime, plateNumber, carModel) = line.replace("\n", "").split(",")
                parsed.append(RawModel(int(idx), int(number), dateTime, plateNumber, carModel))
        return parsed

    def sorted_by_carModel(self):
        return sorted(self.data, key=lambda f: f.carModel)

    def sorted_by_number(self):
        return sorted(self.data, key=lambda f: f.number)

    def select_more_than(self, value):
        r = []
        for d in self.data:
            if(d.number > value):
                r.append(d)
        return r

    def add_new(self, number, dateTime, plateNumber, carModel):
        self.data.append(RawModel(len(self.data)+1, number, dateTime, plateNumber, carModel))
        self.save(self.file_path, self.data)

    @staticmethod
    def save(path, new_data):
        with open(path, "w", encoding='utf-8') as f:
            for r in new_data:
                f.write(f"{r.idx},{r.number},{r.dateTime},{r.plateNumber},{r.carModel}\n")

    def print(self):
        for r in self.data:
            print(f"Запись №{r.idx}: номер = {r.number}, дата и время = {r.dateTime}, номерной знак = {r.plateNumber}, марка автомобиля = {r.carModel}")
    def printd(self, d):
        for r in d:
            print(f"Запись №{r.idx}: номер = {r.number}, дата и время = {r.dateTime}, номерной знак = {r.plateNumber}, марка автомобиля = {r.carModel}")

def get_files_count_in_directory(path):
    (loc, dirs, files) = next(os.walk(path))
    return len(files)
data = Data("data.csv")

#__repr__()
print(repr(data), "\n")

#__str__()
print(data, "\n")

#Итератор
for item in iter(data):
        print(item)

print("-"*64)

#Генератор
for item in data.as_generator():
    print(item)

print("-"*64)



print("\nОтсортировано по имени: ")
data.printd(data.sorted_by_carModel())
print("\nОтсортировано по номеру: ")
data.printd(data.sorted_by_number())
print("\nТолько строки, у которых номер больше 500: ")
data.printd(data.select_more_than(500))

#Добавление новых данных
data.add_new(12341, "15.05.2021", "#43424", "Камаз")
data.add_new(423,"21.11.2023", "#4321", "УАЗ")
data.add_new(231, "11.02.2023", "#4241", "Нисан")