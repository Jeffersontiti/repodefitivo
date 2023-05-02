## calculadora que realiza suma/resta/multiplicacion/division/factorial/numeros elevados..

##suma de numeros
def sumar_numeros(n):
    numeros = []
    for i in range(n):
        numeros.append(float(input(f"Ingrese el número {i + 1}: ")))
    return sum(numeros)
##resta de numeros
def restar_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return num1 - num2
##multiplicaion de numeros 
def multiplicar_numeros(n):
    numeros = []
    for i in range(n):
        numeros.append(float(input(f"Ingrese el número {i + 1}: ")))
    producto = 1
    for numero in numeros:
        producto *= numero
    return producto
##division de numeros
def dividir_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return num1 / num2
##calculo de factorial
def calcular_factorial():
    num = int(input("Ingrese el número: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial
##Potncia
def calcular_potencia():
    num1 = float(input("Ingrese la base: "))
    num2 = float(input("Ingrese el exponente: "))
    return num1 ** num2
## menu de la calculadora
def menu():
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Factorial")
    print("6. Potencia")
    print("0. Salir")
## ciclo whilw
while True:
    menu()
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        n = int(input("Ingrese la cantidad de números a sumar: "))
        resultado = sumar_numeros(n)
        print(f"El resultado es {resultado}")
    elif opcion == 2:
        resultado = restar_numeros()
        print(f"El resultado es {resultado}")
    elif opcion == 3:
        n = int(input("Ingrese la cantidad de números a multiplicar: "))
        resultado = multiplicar_numeros(n)
        print(f"El resultado es {resultado}")
    elif opcion == 4:
        resultado = dividir_numeros()
        print(f"El resultado es {resultado}")
    elif opcion == 5:
        resultado = calcular_factorial()
        print(f"El resultado es {resultado}")
    elif opcion == 6:
        resultado = calcular_potencia()
        print(f"El resultado es {resultado}")
    elif opcion == 0:
        break
    else:
        print("Opción inválida")