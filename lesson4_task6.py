from itertools import count, cycle

my_list1 = input("Enter the first and the last number: ").split()
for el in count(int(my_list1[0])):
    if el > int(my_list1[1]):
        break
    else:
        print(el)
my_list2 = input("Enter the elements: ").split()
num_el = int(input("Enter the length of the sequence: "))
с = 0

for el in cycle(my_list2):
    if с > num_el:
        break
    print(el)
    с += 1
