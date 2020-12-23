class Road:
    # конструктор
    # атрибуты обьекта
    def __init__(self, l, w):
        self._length = l
        self._width = w

    # методы
    def pavement_mass(self):
        mass = 25
        thickness = 5
        counting = (self._length * self._width * 25 * 5) / 1000
        print(f"Масса асфальта, необходимого для покрытия всего дорожного полотна {round(counting, 2)} т")


user_length = int(input("Введите длину асфальта в метрах: "))
user_width = int(input("Введите ширину асфальта в метрах: "))
mass_pavement = Road(user_length, user_width)
mass_pavement.pavement_mass()
