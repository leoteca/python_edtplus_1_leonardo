texto = "aprender a programar en python con un simple paso"

lenguaje_de_programacion = "python"

if lenguaje_de_programacion in texto:

    print("si esta la palabra")

else:

    print("no esta la palabra")

# longitud de una cadena

tamano_texto = len(texto)

print(tamano_texto)

# upper case  = Todo en mayuscula

texto_en_mayuscula = texto.upper()
print(texto_en_mayuscula)

# lower case = todo en minuscula

texto_en_minuscula = texto.lower()
print(texto_en_minuscula)

# title case = Todas las iniciales en mayuscula

texto_inicial = texto.title()
print(texto_inicial)

# swap case = pasar todas las palabras a minusculas o mayuscula

texto_inverso = texto.swapcase()
print(texto_inverso)
print(texto_inicial.swapcase())

#  count = contar todas las palabras que hay en el texto que coincidan

conteo_palabras = texto.lower().count("python")
print(conteo_palabras)

# capitalize = la primera letra en mayuscula 

inicial_mayuscula = texto.capitalize()
print(inicial_mayuscula)

#  