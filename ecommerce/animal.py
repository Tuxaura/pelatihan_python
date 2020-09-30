class Animal:
    def __init__(self):
        print("eat")


class Mamal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mamal()
print(help(m))
