def suma(sum1,sum2):
# Propósito: Imprimir por pantalla la suma de **sum1** y **sum2**
# Parámetros: sum1 - numero - El primer numero a sumar
#             sum2 - numero - El segundo numero a sumar
# precondiciones: ninguna
# tipo: tupla
    suma = sum1 + sum2
    print(f"Suma: {sum1} + {sum2} = {suma}")
    return suma, "Suma"

def resta(rest1,rest2):
# Propósito: Imprimir por pantalla la resta de **rest1** y **rest2**
# Parámetros: rest1 - numero - El primer numero a restar
#             rest2 - numero - El segundo numero a restar
# precondiciones: ninguna
# tipo: tupla
    resta = rest1 - rest2
    print(f"Resta: {rest1} - {rest2} = {resta}")
    return resta, "Resta"

def multiplicacion(mul1,mul2):
# Propósito: Imprimir por pantalla la multiplicación de **mul1** y **mul2**
# Parámetros: mul1 - numero - El primer numero a multiplicarr
#             mul2 - numero - El segundo numero a multiplicar
# precondiciones: ninguna
# tipo: tupla
    multiplicar = mul1 * mul2
    print(f"Multiplicación: {mul1} * {mul2} = {multiplicar}")
    return multiplicar, "multiplicacion"

def division(div1,div2):
# Propósito: Imprimir por pantalla la división de **div1** y **div2**
# Parámetros: div1 - numero - El dividendo
#             div2 - numero - El divisor
# precondiciones: ninguna
# tipo: tupla
    division = div1 / div2
    print(f"Division: {div1} / {div2} = {division}")
    return division, "Division"

def divisonEntera(divE1,divE2):
# Propósito: Imprimir por pantalla la división entera de **divE1** y **divE2**
# Parámetros: divE1 - numero - El dividendo
#             divE2 - numero - El divisor
# precondiciones: ninguna
# tipo: tupla
    division = divE1 // divE2
    print(f"Division entera: {divE1} / {divE2} = {division}")
    return division, "Division Entera"

def restoDivisionEntera(rDivE1,rDivE2):
# Propósito: Imprimir por pantalla el resto entera de **rDivE1** y **rDivE2**
# Parámetros: rDivE1 - numero - El dividendo
#             rDivE2 - numero - El divisor
# precondiciones: ninguna
# tipo: tupla
    division = rDivE1 % rDivE2
    print(f"Resto: {rDivE1} % {rDivE2} = {division}")
    return division, "Resto Division Entera"

def potencia(base,expo):
# Propósito: Imprimir por pantalla la potencia de la base **base** elevado al exponente **expo**
# Parámetros: base - numero - La base
#             expo - numero - El exponente
# precondiciones: ninguna
# tipo: tupla
    potencia = base ** expo
    print(f"Potencia: {base} ^ {expo} = {potencia}")
    return potencia, "Potencia"

def inputUsuario(textoAMostrar):
# Propósito: Ingresar el dato **textoAmostrar** y retornarlo
# Parámetros: textoAMostrar - String - El texto a mostrar
# precondiciones: ninguna
# tipo: numero 
    inputUsuario = int(input(textoAMostrar))
    return inputUsuario
    
def calculadora():
# Propósito: Realizar operaciones matemáticas
# precondiciones: ninguna
# tipo: ninguna 
    print("Bienvenidos a la calculadora de Python")
    menu() 
    opcion = inputUsuario("Ingrese una operación ")
    while opcion != 0:
        if opcion >= 1 and opcion <= 7:
            aplicar_funcion(operaciones.get(opcion))
        elif opcion == 8:
            val1 = inputUsuario("Ingrese el primer numero ")
            np = numerosPrimosHasta(val1)
            print(np)
            agregarHistorial(f"Numeros primos hasta {val1}", np)
        elif opcion == 9:
            historial()
        else:
            print("Error")
        menu()
        opcion = inputUsuario("Ingrese una operación ")
    print("Gracias por usar la calculadora de Python")


def menu():
# Propósito: Mostrar un menú con las operaciones a realizar
# precondiciones: ninguna
# tipo: ninguna  
    print("Ingrese la operación a realizar:")
    print("1- Suma ")
    print("2- Resta ")
    print("3- Multiplicación ")
    print("4- División ")
    print("5- División entera ")
    print("6- Resto división entera ")
    print("7- Potencia")
    print("8- Primos hasta")
    print("9- Historial")
    print("0- Salir")

def esPrimo(num):
    # Propósito: Indica si el numero **num** es primo o no
    # Parámetros: num - Numero - El número a saber si es primo
    # precondiciones: El numero ingresado debe ser mayor o igual a 2
    # tipo: booleano
    for i in range(2,num-1):
        if num % i == 0:
            return False
    return True

def numerosPrimosHasta(num):
    # Propósito: Retorna una lista de numeros primos hasta el numero **num** indicado
    # Parámetros: num - Numero - El número hasta saber si es primo
    # precondiciones: El numero ingresado debe ser mayor o igual a 2
    # tipo: Lista
    lista_primos = []
    for i in range(2,num):
        if esPrimo(i):
            lista_primos.append(i)
    return lista_primos
    
operaciones_realizadas = {}

def historial():
# Propósito: Mostrar el historial de operaciones
# tipo: ninguna
    for k,v in operaciones_realizadas.items():
        print(f"Operación realizada {k} y su resultado {v}")

def agregarHistorial(key, value):
# Propósito: Agrega al historial las operaciones realizadas juntos con sus valores
# precondiciones: key - String - La operación y valores realizados
#                 value - String - El resultado de la operación
# tipo: ninguna 
    operaciones_realizadas[key] = value
    
def aplicar_funcion(funcion):
    # Propósito: Aplicar una función matemática con sus dos valores y guardarlo en el historial
    # Parámetros: funcion - función - La función a ejecutarse
    # precondiciones: ninguna
    # tipo: Nada 
    val1 = inputUsuario("Ingrese el primer numero ")
    val2 = inputUsuario("Ingrese el segundo numero ")
    # Desestructuro para guardar los dos retornos en variables
    resultado,operacion = funcion(val1,val2)
    agregarHistorial(f"{operacion} {val1} y {val2}", resultado)
    
operaciones = {
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division,
    5: divisonEntera,
    6: restoDivisionEntera,
    7: potencia,
    8: numerosPrimosHasta
}

calculadora()