import math

# Horas de trabajo
WORKING_HOURS = 8

# Días laborables
WORKING_DAYS = 7

# Número de servidores
K = 1

# Datos iniciales de la primera alternativa
FIRST_LAMBDA = 1
FIRST_MIU = 2

# Datos iniciales de la segunda alternativa
SECOND_LAMBDA = 1*(1/4)
SECOND_MIU = 2*(1/4)

# Imprimir negritas
b_ini = '\033[1m'
b_fin = '\033[0m'

def initial_data():
    print('\n -----------------')
    print(f'| {b_ini}DATOS INICIALES{b_fin} |')
    print(' -----------------\n')
    print(f"{b_ini}PRIMERA ALTERNATIVA\t\t\t\tSEGUNDA ALTERNATIVA{b_fin}")
    print(f"{b_ini}Población (M) ={b_fin} Infinita\t\t\t{b_ini}Población ={b_fin} Infinita")
    print(f"{b_ini}Número de Servidores ={b_fin} {K}\t\t\t{b_ini}Número de Servidores ={b_fin} {K}")
    print(f"{b_ini}Tasa de llegada (\u03BB) ={b_fin} {FIRST_LAMBDA}\t\t\t\t{b_ini}Tasa de llegada (\u03BB)={b_fin} {SECOND_LAMBDA}")
    print(f"{b_ini}Tasa de servicio (\u03BC) ={b_fin} {FIRST_MIU}\t\t\t{b_ini}Tasa de servicio (\u03BC) ={b_fin} {SECOND_MIU}")


def stability_condition():
    # Determinar condiciones de estabilidad
    first_stab_cond = FIRST_LAMBDA / FIRST_MIU
    second_stab_cond = SECOND_LAMBDA / SECOND_MIU

    print('\n --------------------------------------')
    print(f'| {b_ini}REVISIÓN DE CONDICIÓN DE ESTABILIDAD{b_fin} |')
    print(' --------------------------------------\n')
    print(f"{b_ini}PRIMERA ALTERNATIVA\t\t\t\tSEGUNDA ALTERNATIVA{b_fin}")
    print(f"{first_stab_cond} < 1 {b_ini}{'Cumple Condición de estabilidad' if first_stab_cond < 1 else 'No cumple condición de estabilidad'}{b_fin}\t\t{second_stab_cond} < 1 {b_ini}{'Cumple Condición de estabilidad' if second_stab_cond < 1 else 'No cumple condición de estabilidad'}{b_fin}")


def a_literal():
    # Determinar el tiempo de espera en cola
    first_Wq = FIRST_LAMBDA / (FIRST_MIU * (FIRST_MIU - FIRST_LAMBDA))
    second_Wq = SECOND_LAMBDA / (SECOND_MIU * (SECOND_MIU - SECOND_LAMBDA))

    # Determinar el tiempo total
    first_Tt = FIRST_LAMBDA * WORKING_HOURS * first_Wq * WORKING_DAYS
    second_Tt = SECOND_LAMBDA * WORKING_HOURS * second_Wq * WORKING_DAYS

    print('\n --------------')
    print(f'| {b_ini}TIEMPO TOTAL{b_fin} |')
    print(' --------------\n')
    print(f'{b_ini}PRIMERA ALTERNATIVA\t\t\t\tSEGUNDA ALTERNATIVA{b_fin}')
    print(f'{b_ini}Tiempo de espera en cola ={b_fin} {first_Wq} dia/avión\t{b_ini}Tiempo de espera en cola ={b_fin} {second_Wq} dias/avion')
    print(f'\n{b_ini}Wq en Tt{b_fin}')
    print(f'{b_ini}Tiempo total en el taller ={b_fin} {first_Tt} horas\t\t{b_ini}Tiempo total en el taller ={b_fin} {second_Tt} horas')


def b_literal():
    # Determinar la probabilidad de hallar el sistema vacío (población infinita)
    P0 = 1 - (SECOND_LAMBDA / SECOND_MIU)

    # Determinar el tiempo total semanal que estará desocupado el sistema
    Tdd = P0 * WORKING_HOURS * WORKING_DAYS

    print('\n -----------------------------------------------------')
    print(f'| {b_ini}TIEMPO TOTAL SEMANAL QUE PASA DESOCUPADO EL SISTEMA{b_fin} |')
    print(' -----------------------------------------------------\n')
    print(f'{b_ini}Probabilidad de hallar el sistema vacío = {b_fin}{P0}')
    print(f'{b_ini}Tiempo total semanal que el sistema pasa vacío = {b_fin}{Tdd}')


def c_literal():
    # Determinar la probabilidad que tienen los aviones de ser atendidos
    P = SECOND_LAMBDA / SECOND_MIU

    print('\n --------------------------------------------')
    print(f'| {b_ini}PROBABILIDAD DE ESPERAR PARA SER ATENDIDOS{b_fin} |')
    print(' --------------------------------------------\n')
    print(f'{b_ini}Probabilidad de esperar para ser atendidos ={b_fin} {P}')


def truncate(number, decimals):
    # Retornar un valor truncado a un número específico de decimales.
    if not isinstance(decimals, int):
        raise TypeError("los puestos decimales deben ser enteros.")
    elif decimals < 0:
        raise ValueError("los puestos decimales deben ser 0 o mayores.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


def factorial(value):

    if value == 0:
        return 1
    else:
        cont = 1
        factorial_val = 1

        while(cont <= value):
            factorial_val *= cont
            cont += 1

        return factorial_val
        

def prob_empty_sys(POPULATION, LAMBDA_value, MIU_value):
    
    # Valor final de la sumatoria
    summation = 0

    # Incrementador de la sumatoria
    cont = 0

    while(cont <= POPULATION):
        summation += (factorial(POPULATION)/factorial(POPULATION-cont))*((LAMBDA_value/MIU_value) ** cont)
        cont += 1 

    return summation


def d_literal():
    #Población dada
    POPULATION = 5

    # Probabilidad de hallar el sistema vacío dada una población (población finita)
    P0 = 1 / prob_empty_sys(POPULATION, SECOND_LAMBDA, SECOND_MIU)

    # Número esperado de clientes en el sistema
    L = POPULATION - (SECOND_MIU / SECOND_LAMBDA) * (1 - P0)

    print('\n -------------------------------------------')
    print(f'| {b_ini}NÚMERO ESPERADO DE CLIENTES EN EL SISTEMA{b_fin} |')
    print(' -------------------------------------------\n')
    print(f'{b_ini}Probabilidad de hallar el sistema vacío ={b_fin} {truncate(P0, 3)}')
    print(f'\n{b_ini}P0 en L{b_fin}')
    print(f'{b_ini}Número esperado de aviones ={b_fin} {truncate(L, 3)} aviones')


def excer12_resolution():
    initial_data()
    stability_condition()
    a_literal()

    print('\n\n ================================================')
    print(f"| {b_ini}TOMANDO COMO REFERENCIA LA SEGUNDA ALTERNATIVA{b_fin} |")
    print(' ================================================\n')

    b_literal()
    c_literal()
    d_literal()