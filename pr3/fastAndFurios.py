'''
Pol Sánchez
Trishan Mizhquiri
Rubén Sánchez
M03 UF1 A3 PR3
08/11/2023
Volem un programa que calculi la velocitat instantània i la velocitat mitjana.
'''

try:
    velocitatinicial = float(input("Introdueix la velocitat inicial "))
    acceleracio = float(input("Introdueix l'acceleració "))
    temps = float(input("Introdueix el temps "))

    velocitatinstantania = velocitatinicial + acceleracio * temps
    velocitatmitjana = (velocitatinicial + velocitatinstantania )/2

    if velocitatinstantania <= 0:
        print("La velocitat mitjana no és calculable ")

    else:
        print("La velocitat instantania és", velocitatinstantania, "La velocitat mitjana és", velocitatmitjana)
except ValueError:
    print("ERROR: Introdueix els numeros només")


