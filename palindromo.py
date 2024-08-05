texto = input("Ingrese una frase: ")

texto_limpio = texto.replace(" ", "")

i = 0
es_palindromo = "Es palíndromo"

while texto_limpio[i:i + 1] != "":
    if texto_limpio[i] != texto_limpio[-(i + 1)]:
        es_palindromo = "No es palíndromo"
    i += 1

print(es_palindromo)