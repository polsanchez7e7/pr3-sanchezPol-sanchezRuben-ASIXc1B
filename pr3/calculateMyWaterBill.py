"""
Pol Sánchez
Trishan Mizhquiri
Rubén Sánchez
M03 UF1 A3 PR3
09/11/2023
L'usuari introdueix la lletra del tipus d'habitatge i número de m3  d'aigua gastats. Mostrar per pantalla el preu total de la factura de l’aigua. Arrodonit a 2 decimals
"""




tipus = input("Introdueix el tipus d'habitatge: ")

consum = float(input("Introdueix el número de m³ gastats d'aigua: "))

quota = float()
pr = float()

if tipus == "A":
    quota = 2.46
elif tipus == "B":
    quota = 6.40
elif tipus == "C":
    quota = 7.25
elif tipus == "D":
    quota = 11.21
elif tipus == "E":
    quota = 12.10
elif tipus == "F":
    quota = 17.28
elif tipus == "G":
    quota = 28.01
elif tipus == "H":
    quota = 40.50
elif tipus == "I":
    quota = 61.31



if consum == 0 - 6:
    pr = 0.5849
elif consum == 7 - 9:
    pr = 1.1699
elif consum == 10 - 15:
    pr = 1.7548
elif consum == 16 - 18:
    pr = 2.3397
elif consum > 18:
    pr = 2.9246

Precio = (consum * pr) + quota

print (f"Tienes que pagar, {Precio:.2f}" )
