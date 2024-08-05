def invertir_lista(lista):
    
    lista_invertida = []
    for i in lista:
        lista_invertida.insert(0, i)
    return lista_invertida

mi_lista = [22, 66, 88, 1000, 2000]

lista_invertida = invertir_lista(mi_lista)

print("Lista original:", mi_lista)

print("Lista invertida:", lista_invertida)