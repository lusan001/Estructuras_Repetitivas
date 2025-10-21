# Programa que muestre por pantalla los N primeros numeros primos. El valor de N se debe pedir al usuario
from itertools import count

print("Programa que muestre por pantalla los N primeros numeros primos. El valor de N se debe pedir al usuario")
print("\n")

N = int(input("Introduce el valor de N: "))

if N <= 0:
    print("Error. Debes introducir un numero mayor que 0")
else:
    counter = 0
    number = 2
    while counter < N:
        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(number)
            counter += 1
        number += 1
