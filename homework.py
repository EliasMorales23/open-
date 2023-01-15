Peso = int(input ("ingrese su peso en kilogramos "))

altura = float(input("ingrese su altura en metros  "))

cuadrado= altura**2 
indice = (Peso / cuadrado)

a= round(indice,2)

print (f"su indice de masa corporal es de  {a}")