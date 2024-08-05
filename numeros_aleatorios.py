import random

cantidad = int(input("Ingrese la cantidad de números aleatorios: "))

numeros = []

for i in range(cantidad):
    numeros.append(random.randint(1, cantidad))

print("Lista de números aleatorios:", numeros)