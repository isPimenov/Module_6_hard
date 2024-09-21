import math


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
        if self.__is_valid_sides(*new_sides):
            for i in range(0, len(new_sides)):
                self.__sides[i] = new_sides[i]


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], side):
        super().__init__(color, side)
        self.__radius = side / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], side: int):
        super().__init__(color, side)
        self.__sides = [side] * self.sides_count

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] ** 3

    def __len__(self):
        prmtr = sum(self.__sides)
        return prmtr


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((100,150,200), 5,6,7)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
triangle1.set_color(150,200,300) # Не изменится
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
triangle1.set_sides(3,5,7,9)  # Не изменится
print(triangle1.get_sides())

# Проверка периметра фигур:
print(f'Периметр круга: {len(circle1)}')
print(f'Периметр куба: {len(cube1)}')
print(f'Периметр треугольника: {len(triangle1)}')

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площадь (треугольника):
print(triangle1.get_square())

# Проверка площадь (круга):
print(circle1.get_square())