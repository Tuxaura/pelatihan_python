class Orang:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def banding_umur(self, other):
        if self.age > other.age:
            return print(f"{self.name} lebih tua dari {other.name}")
        elif self.age < other.age:
            return print(f"{self.name} lebih muda dari {other.name}")
        else:
            return print(f"umur {self.name} sama dengan umur {other.name}")

# main program


p1 = Orang("Budi", 32)
p2 = Orang("Wati", 36)
p3 = Orang("John", 32)

p1.banding_umur(p2)
p2.banding_umur(p1)
p3.banding_umur(p1)
