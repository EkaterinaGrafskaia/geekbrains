class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


mid_result = []
while True:
    try:
        user_list = input("Введите число или команду 'stop': ")
        num = [i for i in user_list.split()]
        if user_list == 'stop':
            break
        for j in range(len(num)):
            if (num[j].isdigit() == False) and user_list != 'stop':
                raise OwnError("Введите число или команду 'stop', выполнение программы при которой завершается!")
        else:
            mid_result.append(user_list)
            continue
    except OwnError as err:
        print(err)
print(f"Элементы списка: {' '.join(el for el in mid_result)} ")
