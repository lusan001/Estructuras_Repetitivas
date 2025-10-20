#Algoritmo que pide numeros. El progrma debe de informar de cuantos numeros introducidos son mayores de que 0, menores de 0 y iguales a 0

print("Programa que pide numeros. El progrma debe de informar de cuantos numeros introducidos son mayores de que 0, menores de 0 y iguales a 0")
print("\n")

num = int(input("Introduce un numero: "))

#Contadores
mayores = 0
menores = 0
iguales = 0

#Bucle
for i in range(num):
    num = int(input("Introduce un numero: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1

print("Mayores de 0: ", mayores)
print("Menores de 0: ", menores)
print("Iguales a 0: ", iguales)