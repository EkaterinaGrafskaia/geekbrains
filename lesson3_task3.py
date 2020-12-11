def my_func(var_1, var_2, var_3):
    try:
        my_list = [int(var_1), int(var_2), int(var_3)]
        my_list.remove(min(my_list))
        print(sum(my_list))
    except ValueError:
        print("Некорректные данные!")


user_var_1 = input("Введите первое число: ")
user_var_2 = input("Введите второе число: ")
user_var_3 = input("Введите третье число: ")
my_func(user_var_1, user_var_2, user_var_3)
