'''
Operador or

raducido se lo lee como “O”. Si la condición 1 es Verdadera o la condición 2 es Verdadera, luego ejecutar la rama del Verdadero.
Cuando vinculamos dos o más condiciones con el operador “or", con que una de las dos condiciones sea Verdadera alcanza para que el resultado de la condición compuesta sea Verdadero.

'''

# Se carga una fecha (día, mes y año) por teclado. Mostrar un mensaje si corresponde al primer trimestre del año (enero, febrero o marzo) 
# Cargar por teclado el valor numérico del día, mes y año.


ia=int(input("Ingrese nro de día:"))
mes=int(input("Ingrese nro de mes:"))
año=int(input("Ingrese nro de año:"))
if mes==1 or mes==2 or mes==3:
    print("Corresponde al primer trimestre")
