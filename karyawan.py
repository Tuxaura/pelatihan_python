class Karyawan:
    no_karyawan = 0
    rasio_kenaikan = 1.01

    def __init__(self, depan, belakang, gaji):
        self.depan = depan
        self.belakang = belakang
        self.email = depan + '.' + belakang + '@email.com'
        self.gaji = gaji

        Karyawan.no_karyawan += 1

    def namalengkap(self):
        return f"{self.depan} {self.belakang}"

    def kenaikangaji(self):
        self.gaji = int(self.gaji * self.rasio_kenaikan)

    @classmethod
    def set_rasio_kenaikan(cls, besaran):
        cls.rasio_kenaikan = besaran

    @classmethod
    def pars_karyawan(cls, string_karyawan):
        depan, belakang, gaji = string_karyawan.split('-')
        return cls(depan, belakang, gaji)


karyawan1 = Karyawan("Beben", "Akbar", 5000)
karyawan2 = Karyawan("John", "Doe", 6000)
karyawan3 = Karyawan("Jane", "Doe", 7000)

str_karyawan4 = "Sponge-Bob-5555"
str_karyawan5 = "Patrick-Bintang-6666"
str_karyawan6 = "Tuan-Crab-7777"

karyawan4 = Karyawan.pars_karyawan(str_karyawan4)

# karyawan1.set_rasio_kenaikan(1.7)
Karyawan.set_rasio_kenaikan(1.2)

print(Karyawan.rasio_kenaikan)
print(karyawan1.rasio_kenaikan)
print(karyawan2.rasio_kenaikan)
print(karyawan4.depan)
print(karyawan4.email)
print(karyawan4.gaji)
