with open("my_file2.txt", "r", encoding="utf-16") as f_obj:
    content = f_obj.readlines()
    print("Количество строк в файле: ", len(content))
    print("Количество слов в каждой строке:")
    for line in content:
        print(len(line.split()))
# -----------------------проверка чтения файла ---------------------------------
with open("my_file2.txt", encoding="utf-16") as f_obj:
    for line in f_obj:
        print(line, end="")
