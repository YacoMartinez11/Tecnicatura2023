# Ejercicio 3: Función Recursiva
# Imprimnir números de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejmplo si pasamos el valor de 5.
def imprimir_numeos_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeos_recursivos(numero - 1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto')
imprimir_numeos_recursivos(5)
