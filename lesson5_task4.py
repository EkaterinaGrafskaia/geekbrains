from num2words import num2words

#---------------меняем регистр первого слова в переводе---------------
def titlise(string):
    new_string = string.split()
    if len(new_string) > 1:
        new_string[0] = new_string[0].title()
        return ' '.join(new_string)
    else:
        return string.title()


with open("my_file4.txt", "r", encoding="utf-16") as f_obj:
    with open("new_file.txt", "w", encoding="utf-16") as f_obj_new:
        content = f_obj.readlines()
        new_content = []
        for line in content:
            number = line.split(" — ")[1]
            new_line = num2words(int(number), lang='ru')
            f_obj_new.write(f"{titlise(new_line)} — {number}")

# -----------------------проверка чтения файла ---------------------------------
with open("my_file4.txt", "r", encoding="utf-16") as f_obj:
    for line in f_obj:
        print(line, end="")
    print("\n")

with open("new_file.txt", "r", encoding="utf-16") as f_obj_new:
    for line in f_obj_new:
        print(line, end="")
