pi = 3.141592653589793


class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if r in range[0, 255] and g in range[0, 255] and b in range[0, 255]:
                return True
            return False
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        prmtr = sum(self.__sides)
        return prmtr

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            for i in len(new_sides):
                self.__sides[i] = new_sides[i]


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__()
        self.__radius = self.__sides[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


#class Triangle:
#class Cube:

circle1 = Circle((200, 200, 100), 10)
print(circle1.get_color())
print(circle1.get_sides())
print(circle1.get_square())
#fig1 = Figure((200, 200, 100), 10)
#print(fig1.get_sides())
