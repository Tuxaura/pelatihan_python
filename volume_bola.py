import math

# input panjang diameter
diameter = input("Masukkan nilai diameter : ")

# perhitungan volume bola 4/3 * pi * (diameter/2)^2
volume = 4/3 * math.pi * math.pow(float(diameter)/2, 3)

# perhitungan volume bola 4 * pi * (diameter/2)^2
luas = 4 * math.pi * math.pow(float(diameter)/2, 2)

print(f"Volume Bola : {volume}")
print(f"Luas Bola : {luas}")
