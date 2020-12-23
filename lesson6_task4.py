class Car:
    # конструктор
    # атрибуты обьекта
    def __init__(self, s, col, n, police=True):
        self.speed = s
        self.color = col
        self.name = n
        self.is_police = police

    # методы
    def go(self):
        print("Машина поехала!")

    def stop(self):
        print("Машина остановилась!")

    def turn(self, direction):
        print(f"Машина повернула {direction}!")

    def show_speed(self, speed):
        print(f"Машина едет со скоростью {speed}!")


class TownCar(Car):
    def show_speed(self, speed):
        if speed >= 60:
            print(f"Вы превысили разрешенную скорость!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, speed):
        if speed >= 40:
            print(f"Машина едет слишком быстро!")


class PoliceCar(Car):
    pass


user_speed = int(input("Введите скорость машины: "))
user_color = input("Введите цвет машины: ")
user_name = input("ВВведите марку машины: ")
user_police = input("Есть ли вблизи полицейский?: ")
user_direction = input("Введите направление движения машины: ")
user_car = Car(user_speed, user_color, user_name, user_police)
user_car.go()
user_car.stop()
user_car.turn(user_direction)
user_car.show_speed(user_speed)
user_towncar = TownCar(user_speed, user_color, user_name, user_police)
user_towncar.show_speed(user_speed)
user_workcar = WorkCar(user_speed, user_color, user_name, user_police)
user_workcar.show_speed(user_speed)
