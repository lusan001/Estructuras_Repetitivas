# Programa que pide el límite inferior y superior a un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir
"""
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
Informa si hemos introducido algún número igual a los límites del intervalo.

"""

print("Programa que pide el límite inferior y superior a un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir")
print("A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:")
print("La suma de los números que están dentro del intervalo (intervalo abierto).")
print("Cuantos números están fuera del intervalo.")
print("Informa si hemos introducido algún número igual a los límites del intervalo.")
print("\n")

lower_limit = int(input("Introduce el límite inferior: "))
upper_limit = int(input("Introduce el límite superior: "))

while lower_limit > upper_limit:
    lower_limit = int(input("Introduce el límite inferior: "))
    upper_limit = int(input("Introduce el límite superior: "))

inside_sum = 0
outside_count = 0
limit_count = 0

while True:
    number = int(input("Introduce un número: "))
    if number == 0:
        break
    if number > lower_limit and number < upper_limit:
        inside_sum += number
    elif number < lower_limit or number > upper_limit:
        outside_count += 1
    if number == lower_limit or number == upper_limit:
        limit_count += 1

print("La suma de los números que están dentro del intervalo es: ", inside_sum)
print("Cuantos números están fuera del intervalo: ", outside_count)
print("Informa si hemos introducido algún número igual a los límites del intervalo: ", limit_count)
