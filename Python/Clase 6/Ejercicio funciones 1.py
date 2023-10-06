# Ejercicio 1: Crea una función para sumar los valores recibidos de tipo numéricos, utilizando argumentos varioables
# *args como parametro de la Función y agregar como resultado la suma de todos los valores pasados como argumentos.
def sumar_valor(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(sumar_valor(3, 5, 9, 2, 1))
