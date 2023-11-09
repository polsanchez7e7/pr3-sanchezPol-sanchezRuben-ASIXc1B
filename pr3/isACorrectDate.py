'''
Pol Sánchez
Trishan Mizhquiri
Rubén Sánchez
M03 UF1 A3 PR3
08/11/2023

'''

try:
    data_input = input("Introdueix una data (DD/MM/AAAA): ")


    dia, mes, any = map(int, data_input.split('/'))


    any_de_traspas = (any % 400 == 0) or ((any % 100 != 0) and (any % 4 == 0))


    dies_al_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    if any_de_traspas:
        dies_al_mes[2] = 29


    data_valida = (1 <= dia <= dies_al_mes[mes]) and (1 <= mes <= 12)


    if data_valida:
        print("La data és vàlida!")
    else:
        print("La data no és vàlida.")
except IndexError or ValueError:
    print("Data o format no vàlids.")


















