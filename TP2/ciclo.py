##ciclo while..

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