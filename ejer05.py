# Programa que te dice si un numero es primo o no

print("Programa que te dice si un numero es primo o no")
print("En caso de que no se introduzca un número o que esta sea menor que 2 se debe mostrar un mensaje de error.")
print("\n")

num = int(input("Introduce un numero: "))

if num < 2 or num == None:
    print("Error")
else:
    if num % 2 == 0:
        print("El numero es primo")
    else:
        print("El numero no es primo")
