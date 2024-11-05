voltaje1 = float(input("ingrese porfavor el primer voltaje: "))
voltaje2 = float(input("ingrese porfavor el segundo voltaje: "))
voltaje3 = float(input("ingrese porfavor el tercero voltaje: "))
voltaje4 = float(input("ingrese porfavor el cuarto voltaje: "))
voltaje5 = float(input("ingrese porfavor el quinto voltaje: "))
voltajeTotal = (voltaje1 + voltaje2 + voltaje3 + voltaje4 + voltaje5) /5
  
if voltajeTotal < 220:
        print(f"Voltaje correcto ({voltajeTotal})")
else:
        print(F"Alto voltaje ({voltajeTotal}) ")