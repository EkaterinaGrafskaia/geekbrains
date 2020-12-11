def my_func(x, y):
    while True:
        try:
            if float(x) <= 0:
                print("Введенное число x не положительно, попробуйте еще раз")
                x = input("Введите действительное положительное число: ")
            if int(y) >= 0:
                print("Введенное число y не отрицательно, попробуйте еще раз")
                y = input("Введите целое отрицательное число: ")
            if (int(y) < 0) and (float(x) > 0):
                print(float(x) ** int(y))
                return True
        except ValueError:
            print("Введенные данные некорректны, попробуйте еще раз")


user_var_1 = input("Введите действительное положительное число: ")
user_var_2 = input("Введите целое отрицательное число: ")
my_func(user_var_1, user_var_2)

#----------------------------------реализация без оператора--------------------------

def my_func(x, y):
    while True:
        try:
            if float(x) <= 0:
                print("Введенное число x не положительно, попробуйте еще раз")
                x = input("Введите действительное положительное число: ")
            if int(y) >= 0:
                print("Введенное число y не отрицательно, попробуйте еще раз")
                y = input("Введите целое отрицательное число: ")
            if (int(y) < 0) and (float(x) > 0):
                result = float(x)
                for i in range(abs(int(y))):
                    result = result * float(x)
                print(result)
                return True
        except ValueError:
            print("Введенные данные некорректны, попробуйте еще раз")


user_var_1 = input("Введите действительное положительное число: ")
user_var_2 = input("Введите целое отрицательное число: ")
my_func(user_var_1, user_var_2)