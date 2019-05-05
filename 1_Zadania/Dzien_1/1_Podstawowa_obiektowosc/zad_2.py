class Shape:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return "Figura {} o środku w punkcie x :{}, y: {}" .format(self.color, self.x, self.y)


    def describe(self):
        info = "info o kształcie : x -{}, y - {}, color - {}" .format(self.x, self.y, self.color)
        print(info)

    def distance(self, sh):
        return (((self.x-sh.x)**2)+((self.y-sh.y)**2))**0.5



a1 = Shape(3, 5, "red")
a2 = Shape(2, 8, "green")

a1.describe()
print(a1)
print(a1.distance(a2))

