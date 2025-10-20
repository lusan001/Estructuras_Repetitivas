#Aplicacion que permite adivinar un numero.
#Se genera un numero aleatorio del 1 al 100
#Se ira pidiendo numeros y se dira si es mayor o menor que el numero aleatorio
#Se mostrara el numero de intentos(tenemos 10 intentos)
#El programa termina cuando se acierta el numero , te dice en cuantos intenos lo has acertado, si se llega al limite de intentos te dice que has perdido y te muestra el numero que habia generado

import random

num_aleatorio = random.randint(1, 100)
print("\n")
print("Bienvenido al juego de adivinar el numero")
print("\n")
print("Tienes 10 intentos para adivinar el numero")
print("\n")


#Nº de intentos
intentos = 10

#Bucle
for i in range(1, intentos + 1):
    num = int(input("Introduce un numero del 1 al 100 : "))
    if num > num_aleatorio:
        print("El numero es mayor")
    elif num < num_aleatorio:
        print("El numero es menor")
    else:
        print("Has acertado el numero")
        break

if i == intentos:
    print("Has perdido")
    print("El numero era: ", num_aleatorio)
    print("\n")