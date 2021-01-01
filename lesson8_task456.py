class Storage:
    def __init__(self):
        self.storage = {}

    def add_item(self, item):
        self.storage.setdefault(item.item_type(), []).append(item)

    def delete_item(self, type, item):
        val_list = self.storage[type]
        for el in enumerate(val_list):
            if el[1] == item:
                num = el[0]
        self.storage[type].remove(self.storage[type][num])

    def get_item_info(self, type):
        return f"В разделе {type} содержится {len(self.storage[type])} единица/ы техники, а именно:\n" \
               f"{','.join(str(el) for el in self.storage[type])}"


class OfficeEquipments:
    def __init__(self, brand, model, year):
        self.type = self.__class__.__name__
        self.model = model
        self.brand = brand
        self.year = year

    def item_type(self):
        return f"{self.type}"


class Printer(OfficeEquipments):
    def __init__(self, brand, model, year, printer_features):
        super().__init__(brand, model, year)
        self.printer_features = printer_features

    def __repr__(self):
        return f"'{self.brand} {self.model} {self.year} {self.printer_features}'"


class Scaner(OfficeEquipments):
    def __init__(self, brand, model, year, scaner_features):
        super().__init__(brand, model, year)
        self.scaner_features = scaner_features

    def __repr__(self):
        return f"'{self.brand} {self.model} {self.year} {self.scaner_features}'"


class Xerox(OfficeEquipments):
    def __init__(self, brand, model, year, xerox_features):
        super().__init__(brand, model, year)
        self.xerox_features = xerox_features

    def __repr__(self):
        return f"'{self.brand} {self.model} {self.year} {self.xerox_features}'"


user_storage = Storage()
scaner1 = Scaner('Brother', 'DS-640', '2018', 'new')
print(scaner1)
user_storage.add_item(scaner1)
scaner2 = Scaner('Brother', 'DS-640', '2013', 'used')
user_storage.add_item(scaner2)
printer = Printer('HP', '107r', '2019', 'new')
user_storage.add_item(printer)
xerox = Xerox('Panasonic', 'KV-S1037', '2015', 'used')
user_storage.add_item(xerox)
print(user_storage.storage)
print(user_storage.get_item_info('Scaner'))
user_storage.delete_item('Scaner', scaner2)
print(user_storage.storage)

while True:
    try:
        question = input("Какую оргтехнику Вы хотите добавить(1 - сканер, 2 - принтер, 3 - ксерокс)?\n"
                         "Ecли Вы передумали, нажмите - q\n")
        if question == "1":
            brand = input("Введите марку сканера:")
            model = input("Введите модель сканера:")
            year = int(input("Введите год производства сканера:"))
            scaner_features = input("Введите дополнительную информацию о сканере:")
            user_storage.add_item(Scaner(f"{brand}", f"{model}", f"{year}", f"{scaner_features}"))
        if question == "2":
            brand = input("Введите марку принтера:")
            model = input("Введите модель принтера:")
            year = int(input("Введите год производства принтера:"))
            printer_features = input("Введите дополнительную информацию о принтере:")
            user_storage.add_item(Printer(f"{brand}", f"{model}", f"{year}", f"{printer_features}"))
        if question == "3":
            brand = input("Введите марку ксерокса:")
            model = input("Введите модель ксерокса:")
            year = int(input("Введите год производства ксерокса:"))
            xerox_features = input("Введите дополнительную информацию о ксероксе:")
            user_storage.add_item(Xerox(f"{brand}", f"{model}", f"{year}", f"{xerox_features}"))
        if question == "q":
            print(user_storage.storage)
            break
    except ValueError:
        print("Неверно введены данные!!! Попробуйте еше раз!")
        continue
