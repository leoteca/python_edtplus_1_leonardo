# funciones en python
# Las funciones son habitantes de primer orden 
# Las funciones estan conformadas por parametros y argumentos

# ejercicio sin funciones 

nombre = "Leonardo"
nombre2 = "Eiver"
nombre3 = "Pedro"
nombre4 = "Angel"
nombre5 = "Joel"

print(f"hola, {nombre}")
print(f"hola, {nombre2}")
print(f"hola, {nombre3}")
print(f"hola, {nombre4}")
print(f"hola, {nombre5}")

print("*"*40)

# Palabra reservada (def); identificacion unica (parametro)

def saludo (name: str):
    print(f"Saludos, {name}")
    
# Invocar a la funcion = saludo ("Leonardo") = invocar ("argumentos")

saludo("Leonardo")
saludo("Eiver")
saludo("Joel")
saludo("Angel")
saludo("Pedro")

print("*"*40)

# Funcion sin parametros ni argumentos

def funcion_sin_parametros_ni_argumentos():
    print("funcion sin parametros ni argumentos")
    
# invocar o llamar

funcion_sin_parametros_ni_argumentos()

'''

Reto

1.- Crear una funcion que me permita sumar dos valores. Quiero que contenga valores estrictos que debe recibir la funcion

2.- Crea una fiesta tematica donde tienen que mostrar o imprimir el nombre del invitado y el personaje del cual va disfrazado
'''
print("*"*40)

def sumar (numero: int, numero2: int):
    print(f"la suma de ", numero, "y", numero2, "es igual a", numero + numero2)
    
sumar(3,9)
sumar(5,8)

print("*"*40)

def fiesta (invitado: str, disfraz: str):
    print(f"hola que tal {invitado} veo que estas disfrazado de {disfraz}")
    
fiesta("Leonardo", "Capitan America")

