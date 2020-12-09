my_list = [7, 5, 3, 3, 2]
user_number = int(input("Введите новый элемент рейтинга: "))
for i in range(len(my_list)):
    if user_number > my_list[i]:
        number_position = int(i)
        break
    if user_number == my_list[i]:
        continue
    else:
        number_position = len(my_list)
my_list.insert(number_position, user_number)
print(my_list)
