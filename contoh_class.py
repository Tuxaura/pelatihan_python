class Kucing:
    species = "Felis catus"

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    # Instance method
    def deskripsi(self):
        return f"{self.nama} berumur {self.umur} tahun"

    # Instance method
    def suara(self, bunyi):
        return f"{self.nama} bersuara {bunyi}"


kucing = Kucing("oren", 32)
print(kucing.suara("meeng"))
print(kucing.species)
print(kucing.deskripsi())
