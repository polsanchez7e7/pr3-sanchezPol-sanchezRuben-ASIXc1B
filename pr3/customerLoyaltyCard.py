'''
Pol Sánchez
Trishan Mizhquiri
Rubén Sánchez
M03 UF1 A3 PR3
08/11/2023
Programa que demana l'import d'una factura
'''
try:
    targetaclient = input("Tens targeta client? (S/N) ")
    importfactura = float(input("introdueix l'import amb l'IVA inclós "))

    if targetaclient == "S" and importfactura >= 100:
        importdescompte = (importfactura * 0.79) * 1.21
        print(f"L'import a pagar és, {importdescompte:.2f}")
    elif targetaclient == "N":
        print("No tens descompte de client")
except ValueError:
    print("ERROR: Introdueix el numero només")

