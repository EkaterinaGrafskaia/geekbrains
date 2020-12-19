import json

with open("my_file7.txt", "r", encoding="utf-16") as f_obj:
    content = f_obj.readlines()
    firm_names = []
    total_profit = []
    summary_profit = 0
    number_firms = 0
    for line in content:
        firm_names.append(line.split()[0])
        profit = int(line.split()[2]) - int(line.split()[3])
        if profit >= 0:
            summary_profit += int(profit)
            number_firms += 1
        total_profit.append(profit)
my_dict1 = dict(zip(firm_names, total_profit))
my_dict2 = {"average_profit": round(summary_profit / number_firms, 3)}
results = [my_dict1, my_dict2]
print(results)
print(summary_profit / number_firms)
with open("my_file.json", "w") as write_f:
    json.dump(results, write_f)

# -----------------------проверка чтения и создания файлов ---------------------------------
with open("my_file7.txt", "r", encoding="utf-16") as f_obj:
    for line in f_obj:
        print(line, end="")
    print("\n")

with open("my_file.json") as read_f:
    data = json.load(read_f)

print(data)
print(type(data))
