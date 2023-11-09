'''
Pol Sánchez
Trishan Mizhquiri
Rubén Sánchez
M03 UF1 A3 PR3
08/11/2023
Programa que detecta si tres números demanats han estat introduïts en ordre creixent.
'''
try:
    primernumero = int(input("Introdueix el primer numero "))
    segonnumero = int(input("introdueix el segon numero "))
    tercernumero = int(input("Introdueix el tercer numero "))

    if primernumero < segonnumero < tercernumero:
        print("L'ordre dels numeros és creixent ")

    else:
        print("L'ordre dels numeros no és creixent")
except ValueError:
    print("ERROR: Introdueix numeros enters")