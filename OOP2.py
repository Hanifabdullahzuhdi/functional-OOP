# Definisikan class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Buat objek
rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 2)

# Akses atribut dan method objek
print(rect1.area()) # output: 15
print(rect2.perimeter()) # output: 24
