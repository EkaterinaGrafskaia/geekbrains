import os
import time

os.system("")


class TrafficLight:
    # конструктор
    # атрибуты обьекта
    def __init__(self):
        self.__color = "Красный свет!"

    # методы
    def running(self):
        print('\033[31m' + "Красный свет!")
        time.sleep(7)
        print('\033[33m' + "Желтый свет!")
        time.sleep(2)
        print('\033[32m' + "Зеленый свет!")
        time.sleep(7)
        print('\033[33m' + "Желтый свет!")
        time.sleep(2)


lights = TrafficLight()
lights.running()
print(lights._TrafficLight__color)
