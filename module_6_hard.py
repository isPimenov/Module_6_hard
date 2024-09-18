pi = 3.141592653589793
from math import sqrt


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
            if r in range(0, 255) and g in range(0, 255) and b in range(0, 255):
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
            for i in range(0, len(new_sides)):
                self.__sides[i] = new_sides[i]


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], side):
        super().__init__(color, side)
        self.__radius = side / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2
        return sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], side: int):
        super().__init__(color, side)
        self.__sides = [side] * self.sides_count
        #print(self.__sides)

    #def get_sides(self):
        #return self.__sides

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())





