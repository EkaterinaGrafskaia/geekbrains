def my_func():
    try:
        var_1 = float(input("Введите делимое: "))
        var_2 = float(input("Введите делитель (не нулевое число!): "))
        result = var_1 / var_2
        print(result)
    except ZeroDivisionError as err1:
        print(err1)
    except ValueError as err2:
        print(err2)


my_func()
