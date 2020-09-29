from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def sisi(self):
        pass


class Segitiga(Polygon):
    def sisi(self):
        print("Saya punya 3 sisi")


class Segilima(Polygon):
    def sisi(self):
        print("Saya punya 5 sisi")


class Segienam(Polygon):
    def sisi(self):
        print("Saya punya 6 sisi")


class Segiempat(Polygon):
    def sisi(self):
        print("Saya punya 4 sisi")


# main program

segitiga = Segitiga()
segitiga.sisi()

segiempat = Segiempat()
segiempat.sisi()

segilima = Segilima()
segilima.sisi()

segienam = Segienam()
segienam.sisi()
