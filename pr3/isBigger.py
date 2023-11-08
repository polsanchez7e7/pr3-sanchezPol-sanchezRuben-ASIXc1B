'''
Pol Sánchez
Trishan Mizhquiri
Rubén Sánchez
M03 UF1 A3 PR3
08/11/2023
Programa que intercanvia el primer numero i el segon en cas de que el primer > segon
'''
try:
    primernumero = int(input("Introdueix el primer numero "))
    segonnumero = int(input("Introdueix el segon numero "))
    intercanvi = (int())

    if primernumero > segonnumero:
        intercanvi = primernumero
        primernumero = segonnumero
        segonnumero = intercanvi
        print ("El primer numero és", primernumero, "El segon numero és", segonnumero)
    else:
        print("El primer numero no és més gran que el segon ")
except ValueError:
    print("ERROR: Introdueix un numero enter")
