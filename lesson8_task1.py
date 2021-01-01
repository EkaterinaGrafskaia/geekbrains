class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def transform(cls, data):
        day = int(data.split('-')[0])
        month = int(data.split('-')[1])
        year = int(data.split('-')[2])
        return day, month, year

    @staticmethod
    def data_check(str):
        try:
            day, month, year = Data.transform(str)
            monthlist1 = [1, 3, 5, 7, 8, 10, 12]
            monthlist2 = [4, 6, 9, 11]
            err = 0
            if month == 2:
                if day < 1 or day > 28:
                    err += 1
            for el in monthlist1:
                if month == el:
                    if day < 1 or day > 31:
                        err += 1
            for el in monthlist2:
                if month == el:
                    if day < 1 or day > 30:
                        err += 1
            if month < 1 or month > 12:
                err += 1
            if len(f'{year}') < 0 or len(f'{year}') > 4:
                err += 1
            if err > 0:
                print(f"{day}-{month}-{year} Дата указана неверно!!!")
            if err == 0:
                print(f"{day}-{month}-{year} Дата указана верно!!!")
        except ValueError:
            print("Дата указана неверно!!! Введите дату в формате 'день-месяц-год'!")


str = input("Введите дату в формате 'день-месяц-год':")
data_1 = Data(str)
data_1.data_check(str)

my_str1 = "12-12-2020"
data_2 = Data(my_str1)
data_2.data_check(my_str1)
my_str2 = "12-22-2020"
data_3 = Data(my_str2)
data_3.data_check(my_str2)
my_str3 = "30-02-2020"
data_4 = Data(my_str3)
data_4.data_check(my_str3)
my_str4 = "30-02-21110"
data_5 = Data(my_str4)
data_5.data_check(my_str4)
