# Ejecicio 4: Sumar Números pares dentro de un rango
# Hacer un programa para sumar número pares dentro de un rango, por ejemplo:
#                                                                           suma de numeros pares del 2 al 30
#                                                                           suma = 240

a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a,b+1):
    if i % 2 == 0:
        suma += i
print(f"\nLa suma de números pares dentro del rango es: {suma}")


# Ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo