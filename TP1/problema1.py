numero= int(input("intruduce un numero para calcular su factorial: "))
factorial= 1

#cacular
for i in range (1, numero +1):
     factorial= factorial* i
     
     print("el factorial de",numero,"es", factorial)