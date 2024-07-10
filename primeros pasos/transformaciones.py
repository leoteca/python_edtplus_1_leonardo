#  Concatenaciones o union entre cadenas de texto (str)

nombre = "Leonardo"
print(type(nombre))

apellido = "Teran"

print("Esta es la union del texto sin espacio entre el nombre y el apellido:", nombre + apellido)

print("Esta es la union del texto con espacio entre el nombre y el apellido:", nombre + " " + apellido)

# RETO

valor1 = 20
valor2 = 20

valor3 = "20"
valor4 = "20"

print(valor1 + valor2)
print(valor3 + valor4)

print("valor es de tipo ->", type(valor1))
print("valor es de tipo ->", type(valor2))
print("valor es de tipo ->", type(valor3))
print("valor es de tipo ->", type(valor4))

print("Para hacer la operacion entre cadena de texto que sean numeros:", int(valor3) + int(valor4))
print("Para hacer la operacion entre cadena de texto que sean numeros:", str(valor2) + str(valor1))

"""

Reto

1) Quiero que le pregunten al usuario su nombre y su apellido.

2) Quiero que unan dos cadenas de texto y un numero entero (Ejemplo: su nombre, apelliodo y edad.)

3)Quiero que realizen una suma y una resta entre una cadadena de texto y un numero entero.

"""

print("Hola bienvenido a el test")

nombre_usuario = input("Cual es tu nombre ")
print ("hola",  nombre_usuario)

apellido_usuario = input("Cual es tu apellido ")
print(apellido_usuario, "interesante")

edad = 13

print  ( " entonces tu nombre es ",  nombre_usuario + " "  + apellido_usuario , " y tu edad es " , " " , edad )

numero1 = 5
numero2 = 7

letra_1 = "3"
letra_2 = "8"

print("sabes que la suma de los siguientes numeros da ...", numero1 +  int (letra_1))
print("sabes que la resta de los siguientes numeros da ...", numero2 -  int (letra_2))