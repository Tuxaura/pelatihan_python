# Selesaikan persamaan quadrat ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = -4
c = 6.25

# Menghitung diskriminan
d = (b**2) - (4*a*c)

# mencari solusi 1 (-b-vd)/2*a
solusi1 = (-b-cmath.sqrt(d))/(2*a)

# mencari solusi 2 (-b+vd)/2*a
solusi2 = (-b+cmath.sqrt(d))/(2*a)

print(f"The solution are {solusi1} and {solusi2}")
