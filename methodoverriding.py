from math import pi


class Bentuk:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def ciri(self):
        return "Saya berbentuk 2 dimensi"

    def __str__(self):
        return self.name


class Kotak(Bentuk):
    def __init__(self, length):
        super().__init__("Saya Kotak")
        self.length = length

    def area(self):
        return self.length**2

    def ciri(self):
        return "Kotak memiliki besar semua sudutnya 90 derajat"


class Lingkaran(Bentuk):
    def __init__(self, radius):
        super().__init__("Saya Lingkaran")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


kotak = Kotak(4)
lingkaran = Lingkaran(7)
print(kotak)
print(lingkaran.ciri())
print(kotak.ciri())
print(lingkaran.area())
