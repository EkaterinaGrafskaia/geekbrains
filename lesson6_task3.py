class Worker:
    # конструктор
    # атрибуты обьекта
    def __init__(self, n, s, p, wage, bonus):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    # методы
    def get_full_name(self):
        print(f"Сотрудник {self.name} {self.surname} исполняет обязанности {self.position}")

    def get_total_income(self):
        wages = self._income["wage"]
        bonuses = self._income["bonus"]
        print(f"Доход сотрудника с учетом премии составил {wages + bonuses}")


user_name = input("Введите имя сотрудника: ")
user_surname = input("Введите фамилию сотрудника: ")
user_position = input("Введите должность сотрудника: ")
user_wage = int(input("Введите доход сотрудника: "))
user_bonus = int(input("Введите премию сотрудника: "))
employee = Position(user_name, user_surname, user_position, user_wage, user_bonus)
employee.get_full_name()
employee.get_total_income()
