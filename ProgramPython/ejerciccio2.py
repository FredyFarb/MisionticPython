"""
Errores sintácticos y lógicos

Modificaremos el problema del concepto anterior y agregaremos adrede una serie de errores tipográficos. Este tipo de errores siempre son detectados por el intérprete de Python, 
antes de ejecutar el programa.

A los errores tipográficos, como por ejemplo indicar el nombre incorrecto de la función, nombres de variables incorrectas, falta de paréntesis, palabras claves mal escritas, etc. 
los llamamos errores SINTACTICOS.

Un programa no se puede ejecutar por completo sin corregir absolutamente todos los errores sintácticos.

Existe otro tipo de errores llamados ERRORES LOGICOS. Este tipo de errores en programas grandes (miles de líneas) son más difíciles de localizar. 
Por ejemplo un programa que permite hacer la facturación pero la salida de datos por impresora es incorrecta.

"""

# Hallar la superficie de un cuadrado conociendo el valor de un lado.

'''Ejempos funciones internas input y print
   Ejempos funcion interna int() numeros enteros'''


lado=input("Ingrese la medida del lado del cuadrado:")
lado=int(lado)
superficie=lado*lado
print("La superficie del cuadra es:", superficie)

#Programa con error sintactico
'''
lado=int(input("Ingrese la medida del lado del cuadrado:"))
superficie=lado*lado
print("La superficie del cuadrado es")
print(Superficie)
'''
# Programa con error logico
'''
print("Programa con error logico")
lado=int(input("Ingrese la medida del lado del cuadrado:"))
superficie=lado*lado*lado
print("La superficie del cuadrado es")
print(superficie)
'''