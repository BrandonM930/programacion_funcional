# La programación funcional es un paradigma de programación declarativo basado en el uso de verdaderas funciones matemáticas. 
# En este estilo de programación, las funciones son ciudadanas de primera clase, porque sus expresiones pueden ser asignadas a variables 
# como se haría con cualquier otro valor, además que pueden crearse funciones de orden superior. 
# El paradigma de programación funcional utiliza casi exclusivamente funciones, priorizan el uso de la recurisividad y la aplicaciones de 
# funciones de orden superior para resolver problemas que en otros lenguajes se resoverían mediante estructuras de control (ej, ciclos) 

# Programa sencillo en python que aplique programación funcional
# Hallar la suma del doble de los elementos pares de la lista

#programacion funcional con map, filter, reduce

from functools import reduce 

datos = [3, 8, 11, 16, 21, 24]

suma = reduce (lambda x, y : x + y, map(lambda x : x*2, filter(lambda x : x % 2 ==0, datos)))

print("Resultado primer ejemplo de programación funcional: \n ")
print ("La suma del doble de los elementos pares de la lista es: ", suma, "\n ")

# Programa que calcula la suma de los cuadrados de una lista de números:

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Función para calcular el cuadrado de un número
def cuadrado(x):
    return x ** 2

# Función para calcular la suma de los cuadrados de una lista de números
def sumacuadrados(numeros):
    cuadrados_numeros = map(cuadrado, numeros)
    total = sum(cuadrados_numeros)
    return total

# Calcular la suma de los cuadrados utilizando programación funcional
result = sumacuadrados(numeros)

print("Resultado segundo ejemplo de programación funcional: \n ")
print("Lista de números:", numeros)
print("Suma de los cuadrados:", result)
