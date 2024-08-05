nombre = input("Ingrese su nombre: ")

while nombre == "":
    print("El nombre no puede estar vacío. Inténtelo de nuevo.")
    nombre = input("Ingrese su nombre: ")
print("Su nombre ingresado es: ", nombre)

edad = int(input("Ingrese su edad: "))

while edad == "" or edad <= 0:
    if edad == "":
        print("La edad no puede estar vacía. Debe ingresar un número entero.")
    
    elif edad <= 0:
        print("La edad debe ser un número positivo.")
    
    edad = input("Ingrese su edad: ")
    
print("Su edad ingresada es: ", edad)