# Mostrar por pantalla todos los números enteros entre 1 y 10.
# Primero hacerlo codificando como venimos haciendo hasta ahora, luego hacerlo usando un bucle for.

# Forma antigua
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# con bucle for
for i in range(1,11):
    print(i)

'''Ejercicio 2

Mostrar por pantalla todos los números enteros entre 1 y 100, hacerlo usando un bucle while 
y tambien con un bucle for.
'''
# bucle while
i = 1
while i <= 100:
    print(i)
    i += 1

# bucle for
for i in range(1,101):
    print(i)
'''
**Ejercicio 3** 

Escribir un programa que pida al usuario dos números enteros e imprima todos los números
enteros entre ellos.
'''
num1 = int(input("Escriba el primer numero "))
num2 = int(input("Escriba el segundo numero "))

for i in range(num1,num2):
    print(i)

'''
**Ejercicio 4** 

Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima 
por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''
nombre_usuario = input("Ingrese su nombre ")
numero_usuario = int(input("Ingrese la cantidad de repeticiones "))

for i in range(numero_usuario):
    print(nombre_usuario)

'''
**Ejercicio 5** 

Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. 
En cada iteración, solicitar al usuario que ingrese un número. 
Al finalizar, mostrar la suma de todos los números ingresados.
'''
numero_iteraciones = int(input("Ingrese las iteraciones "))

total = 0
for i in range(numero_iteraciones):
    total += int(input("Ingrese un numero "))

print(f"La suma de todos los numeros ingresados es {total}")

'''
**Ejercicio 6** 

Realizar un programa que solicite la carga de un valor entero del 1 al 10. 
Mostrar después la tabla de multiplicar de dicho número.
'''
num = int(input("Ingrese un numero del 1 al 10"))

for i in range(1,11):
    print(f"{i} * {num} = {i*num}")

'''
**Ejercicio 7** 

Escribir un programa que pida al usuario un número entero y muestre por pantalla 
un triángulo rectángulo como el de más abajo, de altura igual al número introducido.
'''

num = int(input("Escriba un numero entero "))

for i in range(num+1):
    print(i*"*")

'''
**Ejercicio 8** 

Escribir un programa que imprima la sucesión de fibonacci. 
Para ello pida un número natural n al usuario e imprima por pantalla la suma de los 
números naturales de 1 hasta n. 
Por ejemplo para n = 5, la salida debe ser:
1 + 2 + 3 + 4 + 5 = 15
'''

num = int(input("Escriba un numero natural "))
string = ""
suma = num
for i in range(1,num):
    string += f"{i} + "
    suma += i

print(f"{string}{num} = {suma}")

'''
**Ejercicio 9** 

Escribir un programa que imprima por pantalla todas las fichas del domino, una por línea, sin repetir.
'''

for i in range(0,7):
    for j in range(i,7):
        print(f"{i}|{j}")
    print()
