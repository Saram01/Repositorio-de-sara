def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

grados_fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))

grados_celsius = fahrenheit_a_celsius(grados_fahrenheit)

print(grados_fahrenheit, "grados Fahrenheit son: ", grados_celsius, "grados Celsius.")