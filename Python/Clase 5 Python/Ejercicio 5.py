# Ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo
numero = int(input("Digite un número"))
while numero < 0: # Es decir número negativo
    print("Error -> El número debe ser positivo")
    numero = int(input("Digite un número: "))
factorial = 0 # Variable para calcular el factorial
for i in range(1,numero+1):
    factorial *= i
print(f"\nEl factorial del número {numero} positivo ingresado es: {factorial}")
