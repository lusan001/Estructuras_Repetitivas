#Programa que imprime todos los numeros pares entre dos numeros que se le pide al usuario

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

# Imprime todos los numeros pares entre numero1 y numero2
for i in range(numero1, numero2 + 1):
    if i % 2 == 0:
        print(i)
