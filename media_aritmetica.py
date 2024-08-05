def calcular_media(lista_numeros, numero_adicional):

    lista_completa = lista_numeros + [numero_adicional]

    suma = 0
    contador = 0

    for num in lista_completa:
        suma += num
        contador += 1

    if contador == 0:
        return "No se ingresaron números."

    media = suma / contador
    return media


numeros = [4, 6, 8, 11, 20, 40, 66]  
media = calcular_media(numeros, 10)
print("La media aritmética de los números ingresados es: ", media)