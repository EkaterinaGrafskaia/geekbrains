from abc import ABC, abstractmethod


class Clothes:
    def __init__(self,type):
        self.type = type

    @property
    @abstractmethod
    def total_fabric(self):
        pass

    def __add__(self, other):
        return self.total_fabric + other.total_fabric


class Coat(Clothes):
    @property
    def total_fabric(self):
        print(f"На пошив пальто размера {self.type} необходимо {round((self.type / 6.5 + 0.5), 2)} м. ткани")
        return round((self.type / 6.5 + 0.5), 2)


class Costume(Clothes):
    @property
    def total_fabric(self):
        print(f"На пошив костюма на рост {self.type} необходимо {round((self.type * 2 + 0.3) / 100,2)} м. ткани")
        return round((self.type * 2 + 0.3) / 100,2)


cl_1 = Coat(38)
cl_2 = Costume(180)
print(cl_1 + cl_2)
