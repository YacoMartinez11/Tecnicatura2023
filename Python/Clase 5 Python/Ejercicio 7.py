#Ejercicio 7: juego de adivinar el número
#Realizar un juego para adivinar un número. Para ello se debe generar un número aleatorio entre 1 y 100,
#luego ir pudiendo números indicando "es mayor" o "es menor" según o menor con respeto a N.
#El proceso termina cunado el usaurio acierta y alli se debe mostrar el número de intentos
import random
print("\t.:Juego Adivina el número:.")
aleatorio = random.randint(0, 100)
contador = 0
while True:
    numero = int(input("Digite un número: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el número, Digite un número menor")
    elif numero < aleatorio:
        print("\tNo es el número, Digite un número mayor")
    else:
        print(f"FELICIDADES, acabas de adivinar el número {aleatorio}")
        break
print(f"\nNúmero de intentos: {contador}")
