'''
Pol Sánchez
Trishan Mizhquiri
Rubén Sánchez
M03 UF1 A3 PR3
08/11/2023

'''

data = input("Introdueix la data en format DD/MM/AAAA")
dia, mes, any = data.split("/")

if any % 4 == 0 and (any %100 != 0 or any % 400 == 0):
        return True
    else:
        return False




if False:
    if mes == (01 or 03 or 05 or 07 or 08 or 10 or 12):
        match dia:
            case 1=> dia <=31: print("Correcte")
            case _: print("No és un dia correcte")
    elif mes == 04 or 06 or 09 or 11

















