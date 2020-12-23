class Stationery:
    # конструктор
    # атрибуты обьекта
    def __init__(self, t):
        self.title = t

    # методы
    def draw(self):
        print("“Запуск отрисовки.”")


class Pen(Stationery):
    def draw(self):

        print("“Рисуем ручкой!”")


class Pencil(Stationery):
    def draw(self):

        print("“Рисуем карандашом!”")


class Handle(Stationery):
    def draw(self):

        print("“Рисуем маркером!”")


user_title = input("Введите название: ")
user_stationery = Stationery(user_title)
user_stationery.draw()
user_pen = Pen(user_title)
user_pen.draw()
user_pencil = Pencil(user_title)
user_pencil.draw()
user_handle = Handle(user_title)
user_handle.draw()
