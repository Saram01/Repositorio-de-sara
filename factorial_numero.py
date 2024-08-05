def factorial(a):

    if a < 0:
        return "El factorial no está definido para números negativos."
    elif a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a - 1)

numero = int(input("Ingrese un número: "))

resultado = factorial(numero)

print(f"El factorial de", numero, "es: ", resultado)