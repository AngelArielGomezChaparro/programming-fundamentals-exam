import math


medidasTriangulo = float(input("ingrese la medida de su cuadro equilatero: "))

lado = medidasTriangulo * medidasTriangulo
r = 1.73
area = lado * r / 4

total = area

if total < 1000:
    print(f"El area de su triangulo es: {total}")
else:
    print(f"  Datos no validos  ")