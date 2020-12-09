user_string = input("Введите несколько слов: ").split()
for i in range(len(user_string)):
    print(user_string[i][:10])
