from sys import argv

file_name, working_hours, wages, bonus, employee_name = argv

print("Заработная плата сотрудника ", employee_name, "составила ", int(working_hours) * int(wages) + int(bonus))
