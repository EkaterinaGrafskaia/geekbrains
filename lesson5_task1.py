with open("my_file1.txt", "w", encoding="utf-16") as f_obj:
    set_string = []
    while True:
        user_string = input("Введите данные: ")
        if user_string != "":
            set_string.append(f"{user_string}\n")
            continue
        else:
            break
    f_obj.writelines(set_string)
# -----------------------проверка записи в файл ---------------------------------
with open("my_file1.txt", encoding="utf-16") as f_obj:
    for line in f_obj:
        print(line, end="")
