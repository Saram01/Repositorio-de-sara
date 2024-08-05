import math

def area(radio):

    area = math.pi * (radio ** 2)
    return area

radio = float(input("Ingrese el radio del círculo: "))
area = area(radio)
print("El área del círculo con radio", radio, "es: ", area)