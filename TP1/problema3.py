string1 = input("Introduce el primer string: ")
string2 = input("Introduce el segundo string: ")

if len(string1) != len(string1):
    print("Error: los strings deben tener la misma longitud.")
else:
    intercalado = ""
    for i in range(len(string1)):
        intercalado += string1[i] + string1[i]

    print("Los strings intercalados son:", intercalado)