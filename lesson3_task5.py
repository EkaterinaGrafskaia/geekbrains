def my_func():
    mid_result = []
    while True:
        user_list = input("Введите числа: ").split()
        num = [i for i in user_list]
        try:
            for j in range(len(num)):
                if num[j] == 'q':
                    print(sum(mid_result))
                    return False
                else:
                    mid_result.append(int(num[j]))
                    continue
            print(sum(mid_result))

        except ValueError:
            print("Вводите числа или специальный символ - q, выполнение программы при котором завершается!")


my_func()
