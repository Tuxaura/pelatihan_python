# abstract base class work

from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def sisi(self):
        pass


class Segitiga(Polygon):

    # overriding abstract method
    def sisi(self):
        print("Saya punya 3 sisi")


class Segilima(Polygon):

    # overriding abstract method
    def sisi(self):
        print("Saya punya 5 sisi")


class Segienam(Polygon):

    # overriding abstract method
    def sisi(self):
        print("Saya punya 6 sisi")


class Segiempat(Polygon):

    # overriding abstract method
    def sisi(self):
        print("Saya punya 4 sisi")


# Driver code
polisisi = Polygon()
R = Segitiga()
R.sisi()

K = Segiempat()
K.sisi()

R = Segilima()
R.sisi()

K = Segienam()
K.sisi()
