numeros = [16, 22, 18, 120, 205, 89, 76, 45]

numero_mayor = numeros[0]

numero_menor = numeros[0]

for numero in numeros:
    if numero > numero_mayor:
        numero_mayor = numero
    if numero < numero_menor:
        numero_menor = numero

print("El número más grande en la lista es: ", numero_mayor)

print("El número más pequeño en la lista es: ", numero_menor)