from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}, необходимо ткани {self.get_material()}"

    @abstractmethod
    def get_material(self):
        pass

    @property
    def material(self):
        return self.get_material()


class Coat(Clothes):
    def __init__(self, name, size):
        self.size = size
        super().__init__(name)

    def get_material(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        self.height = height
        super().__init__(name)

    def get_material(self):
        return 2 * self.height + 0.3


class MaterialSum:
    def __init__(self):
        self.clothes = []

    def add(self, clothes):
        self.clothes.append(clothes)

    @property
    def total(self):
        summa = 0
        for item in self.clothes:
            summa += item.material
        return f"{summa}"


coat_1 = Coat('Coat 1', 65)
coat_2 = Coat('Coat 2', 130)

suit_1 = Suit('Suit 1', 2)
suit_2 = Suit('Suit 2', 3)

print(coat_1)
print(coat_2)
print(suit_1)
print(suit_2)

material_sum = MaterialSum()
material_sum.add(coat_1)
material_sum.add(coat_2)
material_sum.add(suit_1)
material_sum.add(suit_2)

print("Всего: ", material_sum.total)
