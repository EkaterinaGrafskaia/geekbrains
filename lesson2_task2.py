user_list = input("Введите элементы списка через пробел: ").split()
num = [int(i) for i in user_list]
new_list = []
for i in range(0, len(num) - 1, 2):
    new_list.append(num[i + 1])
    new_list.append(num[i])
if len(num) % 2 > 0:
    new_list.append(num[-1])
print(new_list)
