with open("my_file1.txt", "w", encoding="utf-16") as f_obj:
    f_obj.write(f"{n * (n - 1) for n in range (5, 150, 6)}")

with open("my_file5.txt", "r", encoding="utf-16") as f_obj:
    content = f_obj.readlines()
    print(sum(list(int(el) for el in content[0].split())))

# -----------------------проверка чтения файла ---------------------------------
with open("my_file5.txt", "r", encoding="utf-16") as f_obj:
    for line in f_obj:
        print(line, end="")
    print("\n")
    sum = 0
    for el in content[0].split():
        sum += int(el)
