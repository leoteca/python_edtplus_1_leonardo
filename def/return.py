# Funciones con return (Retornar) solamente se ejecuta una sola vez.
# La funcion con return no devuelve un valor especifico

# Funcion sin return (Sin retornar)

def sumar_valores_sin_return (a: int, b: int):
    print(a + b)
    
sumar_valores_sin_return(1, 6)
sumar_valores_sin_return(98, 34)

print("*"*40)

resultado_de_la_suma_sin_return = sumar_valores_sin_return(2,3)
print("Mostrar valor obtenido mediante la funcion sin return ->",resultado_de_la_suma_sin_return)

print("*"*40)

def sumar_valores_con_return(a: int, b: int):
    return a + b

# Invocando o llamando al al funcion con return y asignando el valor a una variable

resultado_de_la_suma_con_return = sumar_valores_con_return(2, 3)

print("Mostrar valor obtenido mediante la funcion con return ->", resultado_de_la_suma_con_return)

'''
reto

crear una funcion de suma con input
'''