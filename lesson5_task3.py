with open("my_file3.txt", "r", encoding='utf-16') as f_obj:
    content = f_obj.readlines()
    print(content)
    type(content[0])
    underpaid_employees = []
    wages = 0
    for line in content:
        wages += float(line.split()[1])
        if float(line.split()[1]) < 20000.0:
            underpaid_employees.append(line.split()[0])

print("Фамилии сотрудников с зарплатой менее 20 тыс.: ")
for i in range(len(underpaid_employees)):
    print(underpaid_employees[i])
print(f"Cредняя величина дохода сотрудников: {round(wages / len(underpaid_employees), 3)}")

# -----------------------проверка чтения файла ---------------------------------
with open("my_file3.txt", encoding='utf-16') as f_obj:
    for line in f_obj:
        print(line, end="")
