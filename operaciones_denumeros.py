numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2

resta = numero1 - numero2

multiplicacion = numero1 * numero2

if numero2 != 0:
    division = numero1 / numero2
else:
    division = "Error, no se puede dividir por cero)"

print("El resultado de la suma es: ", suma)
print("El resultado de la resta la resta es: ", resta)
print("El restulado de la multiplicacion es: ", multiplicacion)
print("El resultado de la division es: ", division)