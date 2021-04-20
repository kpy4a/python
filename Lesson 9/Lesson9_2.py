class Road:
    __weight = 25  # удельный вес 1 кв м
    __thickness = 5  # толщина

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_weight(self):
        return self.__weight * self.__thickness * self._length * self._width


length = 5000  # метров
width = 20  # метров

road = Road(length, width)
print(road.calculate_weight(), 'кг')
