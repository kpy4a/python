class Cell:
    def __init__(self, name, partition):
        self.name = name
        self.partition = partition

    def __add__(self, other):
        self.check_other(other)
        return Cell("Новая клетка", self.partition + other.partition)

    def __str__(self):
        return f"Клетка '{self.name}', количество ячеек {self.partition}"

    def __sub__(self, other):
        self.check_other(other)
        partition_sub = self.partition - other.partition
        if partition_sub < 0:
            raise ValueError("Нельзя отнимать от меньшей клетки большую!")
        return Cell("Новая клетка", partition_sub)

    def __mul__(self, other):
        self.check_other(other)
        return Cell("Новая клетка", self.partition * other.partition)

    def __floordiv__(self, other):
        self.check_other(other)
        return Cell("Новая клетка", self.partition // other.partition)

    def check_other(self, other):
        if not isinstance(other, Cell):
            raise ValueError("Операция возможна только с двумя клетками!")

    def make_order(self, count):
        result = []
        for i in range(0, self.partition // count):
            result.append("*" * count)
        if self.partition % count:
            result.append("*" * (self.partition % count))
        return "\n".join(result)


cell_1 = Cell("Клетка 1", 30)
cell_2 = Cell("Клетка 2", 15)

print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
# print(cell_2 - cell_1) # выдаст ошибку
# print(cell_1 + 1) # выдаст ошибку
print(cell_1 * cell_2)
print(cell_1 // cell_2)

print("cell_1.make_order(3)", cell_1.make_order(3), sep="\n")
print("cell_1.make_order(4)", cell_1.make_order(4), sep="\n")
print("cell_1.make_order(7)", cell_1.make_order(7), sep="\n")
