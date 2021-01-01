class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        number_1 = float(input("Введите делимое: "))
        number_2 = float(input("Введите делитель (не нулевое число!): "))
        if number_2 != 0:
            print(f"Все хорошо, результат деления равен {number_1 / number_2}")
            break
        else:
            raise OwnError("Вы ввели нулевое число!")
    except ValueError:
        print("Вы ввели не число! Попробуйте еще раз!")
    except OwnError as err:
        print(err)
