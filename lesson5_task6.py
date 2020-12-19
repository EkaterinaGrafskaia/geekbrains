# -------------трансформируем строку--------------------
def transform_string(string):
    # записываем название предмета + ":"
    name_string = string.split(":")[0]
    string = string.replace(string.split(":")[0] + ':', '')
    # оставляем только числа
    return name_string, ''.join(el for el in string if el not in '(л)праб—.')


with open("my_file6.txt", "r", encoding="utf-16") as f_obj:
    content = f_obj.readlines()
    courses = []
    total_classes = []
    for line in content:
        name, line = transform_string(line)
        courses.append(name)
        sum_classes = 0
        for el in line.split():
            sum_classes += int(el)
        total_classes.append(sum_classes)
my_dict = dict(zip(courses, total_classes))
print(my_dict)

# -----------------------проверка чтения файла ---------------------------------
with open("my_file6.txt", "r", encoding="utf-16") as f_obj:
    for line in f_obj:
        print(line, end="")
    print("\n")
