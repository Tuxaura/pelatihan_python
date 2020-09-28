def penjumlahan(var1, var2):
    return var1+var2


def pengurangan(var1, var2):
    return var1-var2


def pengalian(var1, var2):
    return var1*var2


def pembagian(var1, var2):
    return var1/var2


print("Pilih operasi.")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Pengalian")
print("4.Pembagian")
print("Masukkan nomor operasi(1/2/3/4):")

while True:
    pilihan = input("Masukan operasi pilihanmu : ")
    if pilihan in ("1", "2", "3", "4"):
        angka1 = float(input("Masukkan angka pertama :"))
        angka2 = float(input("Masukkan angka kedua :"))
        if pilihan == "1":
            print(f"{angka1} + {angka2} = {penjumlahan(angka1, angka2)}")
        if pilihan == "2":
            print(f"{angka1} + {angka2} = {pengurangan(angka1, angka2)}")
        if pilihan == "3":
            print(f"{angka1} + {angka2} = {pengalian(angka1, angka2)}")
        if pilihan == "4":
            print(f"{angka1} + {angka2} = {pembagian(angka1, angka2)}")
    else:
        print("pilihan yang anda masukkan salah")
        print("pilihan yang anda masukkan salah")
