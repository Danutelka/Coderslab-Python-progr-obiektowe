import math

class Shape:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return "Figura koloru {} o środku w punkcie ({}, {})".format(self.color, self.x, self.y)


    def describe(self):
        info = "info o kształcie : x -{}, y - {}, color - {}" .format(self.x, self.y, self.color)
        print(info)

    def distance(self, sh):
        return (((self.x-sh.x)**2)+((self.y-sh.y)**2))**0.5

class Circle(Shape):

    def __init__(self, x, y, color, r):
        super(Circle, self).__init__(x, y, color)
        self.radius = r

    def describe(self): #dodać
        info = "info o kształcie : x -{}, y - {}, color - {}".format(self.x, self.y, self.color)
        print(info)

    def area(self):
        return math.pi * (self.radius * 2)

    def perimeter(self):
        return 2 * math.pi * self.radius



a1 = Shape(3, 5, "red")
a2 = Shape(2, 8, "green")

a1.describe()
print(a1)
print(a1.distance(a2))

c = Circle(10, 20, "red", 5)
c.describe()