edad = 17

if edad >= 18: #identificacion, espacio que hace referencia a los cuatro puntos de espacios 
    print("Eres mayor de edad")

else:
    print("Eres menor de edad")

"""
RETO

quiero que le pidas al usuario que digite su edad y compares si su edad es mayor o menor de edad.

Recuerda validar el tipo de dato y debe de haber una variable que indique la mayoria de edad/ EDAD = 18 o 21
"""

edad_usuario = input("Cual es tu edad ")

#edad_usuario = int(input("Cual es tu edad ")), tambien se puede hacer asi.

edad_1 = int(edad_usuario)

# Las puertas son expresiones que nos permiten darle opciones a las condiciones.

if edad_1 >= (18 or 21):
    print("Eres mayor de edad")
    
else:
    print("Eres menor de edad")
    
print(type(edad_1))

