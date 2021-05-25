'''
Estructura condicional compuesta.

Cuando se presenta la elección tenemos la opción de realizar una actividad u otra. 
Es decir tenemos actividades por el verdadero y por el falso de la condición. 
Lo más importante que hay que tener en cuenta que se realizan las actividades de la rama del verdadero o las del falso, NUNCA se realizan las actividades de las dos ramas.

'''

# Realizar un programa que solicite ingresar dos números distintos y muestre por pantalla el mayor de ellos.

num1=int(input("Ingrese primer valor:"))
num2=int(input("ingrese segundo valor:"))


print("El valor mayor es")
if num1>num2:
    print(num1)
else:
    print(num2)


# Utilizando ==
if num1==num2:
    print("Son iguales")
else:
    print("Son distintos")
