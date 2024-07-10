'''

Lista = []
dict "diccionario" = {}
tuple = ()

'''

mi_diccionario = {}
print("La forma en que lo representa python", type(mi_diccionario))

#  Los dicionarios se representan por tener llave -> valor (ingles: Key - value)

mi_diccionario = {
    "key": "value", 
    "llave": "valor",
    "nombre": "leonardo",
    "vida": "es necesario para saber que estamos vivos",
    "edad": 26
}

print(mi_diccionario)

# Para saber la longitud de nustro diccionario se aplica el metodo len (longitud)

longitud_dict = len(mi_diccionario)
print("Esta es la longitud de nuestro diccionario ->", longitud_dict)

#  Obtener valores segun su palabra clave (Key o llave)

print( "El valor de la palabra clave vida es ->", mi_diccionario["vida"])
print( "El valor de la palabra clave edad es ->", mi_diccionario["edad"])

#  Metodo para obtener el valor segun su palabra clave

print("Este metodo get me permite obtener el valor segun su llave ->", mi_diccionario.get("vida"))

# Metodo in para saber si el key esta dentro del diccionario

print("Saber si esta key esta en el diccionario y retorna un booleano ->", "nombre" in mi_diccionario)