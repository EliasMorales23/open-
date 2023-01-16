"""
#Ejercicio 1
elias = "Hola mundo"
#Ejercicio 2
elias = 2

#Ejercicio 3
Peso = int(input ("ingrese su peso en kilogramos "))

altura = float(input("ingrese su altura en metros  "))

cuadrado= altura**2 
indice = (Peso / cuadrado)

a= round(indice,2)

print (f"su indice de masa corporal es de  {a}")

"""
"""
#Ejercicio 4

contador= 1
lista=[]
while contador <=100:
    lista.append(contador)
    contador+=1

lista.reverse()
print(lista)

"""
"""
#ejercicio 5 



def Años(año):
    bisiesto= año % 4
    if bisiesto == 0:
        return print("el año es bisiesto")
       
    else: 
        return print("el año no es bisiesto")

a= int(input("ingrese su año "))

año= Años(a)

"""


#EJERCICIO 6 

class Vehiculo():
    Color = None 
    Ruedas=None
    Puertas=None 

class Coche (Vehiculo):
    Velocidad= None
    Cilindrado= None


p= Coche()
print(p.Color)