import math


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def square(self):
        return math.fabs((self.x2 - self.x1) * (self.y3 - self.y1) - (self.x3 - self.x1) * (self.y2 - self.y1)) / 2

    def height(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** (1 / 2) + (
                (self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2) ** (1 / 2) + (
                       (self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2) ** (1 / 2)


my_tr = Triangle(2, 1, 6, 5, 5, 10)
print(my_tr.square())
print(my_tr.height())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class TrapezeIsometric:
    A = 0
    B = 0
    C = 0
    D = 0

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.A = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** (1 / 2)
        self.B = ((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2) ** (1 / 2)
        self.C = ((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2) ** (1 / 2)
        self.D = ((self.x1 - self.x4) ** 2 + (self.y1 - self.y4) ** 2) ** (1 / 2)
        print(self.A, self.B, self.C, self.D)

    def is_isometric(self):
        if (self.A == self.C and (self.x4 - self.x1) / self.D == (self.x3 - self.x2) / self.B) or (
                self.B == self.D and (self.x3 - self.x4) / self.D == (self.x2 - self.x1) / self.B):
            print('Трапеция равнобочная')
        else:
            print('Трапеция не равнобочная')

    def perimeter(self):
        return self.A + self.B + self.C + self.D

    def square(self):
        h = (self.A ** 2 - (((self.D - self.B) ** 2 + self.A ** 2 - self.C ** 2) / 2 * (self.D - self.B))) ** 1 / 2
        return 1 / 2 * (self.A + self.B) * h


my_trapeze = TrapezeIsometric(2, 4, 0, 2, 0, 7, 2, 5)
my_trapeze.is_isometric()
print(my_trapeze.perimeter())
print(my_trapeze.square())
