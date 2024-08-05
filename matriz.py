import random

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = [[random.randint(1, 100) for _ in range(columnas)] for _ in range(filas)]

print("La matriz generada es:")
for fila in matriz:
    for numero in fila:
        print(f"{numero:2}",)  
    print()