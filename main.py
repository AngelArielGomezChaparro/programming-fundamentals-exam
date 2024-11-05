voltaje1 = float(input("ingrese el primer voltaje: "))
voltaje2 = float(input("ingrese el segundo voltaje: "))
voltaje3 = float(input("ingrese el tercer voltaje: "))

promedio = (voltaje1 + voltaje2 + voltaje3) / 3

if promedio > 220:
    print(f"PELIGRO")
elif promedio >= 115:
    print(F"Alto voltaje")
else:
    print(f"Voltaje correcto")