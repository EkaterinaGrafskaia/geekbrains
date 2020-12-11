def int_func(user_string):
    my_string = [i for i in user_string]
    var = 0
    for j in range(len(my_string)):
        if (ord(my_string[j]) >= 97) and (ord(my_string[j]) <= 122):
            var += 1
            continue
        else:
            var = 0
            break
    if var > 0:
        my_string[0] = my_string[0].upper()
        return ''.join(my_string)
    else:
        print("Вводите слово, состоящее только из маленьких латинских букв!")


user_string = input("Введите слово из маленьких латинских букв: ")
print(int_func(user_string))

new_user_string = input("Введите слова из маленьких латинских букв, разделенных пробелами: ").split()
try:
    for k in range(len(new_user_string)):
        new_user_string[k] = int_func(new_user_string[k])
    print(' '.join(new_user_string))
except TypeError as err:
    print("Маленькие латинские буквы!!!")
