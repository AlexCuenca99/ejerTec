from os import truncate
from ejer12 import prob_empty_sys, truncate

# Horas de trabajo
WORKING_HOURS = 8

# Número de servidores
K = 1

# Datos iniciales
# Manuscritos por hora
MANUS_PER_HOUR = 8

# Promedio de páginas por manuscrito
PAGES_PER_MANUS = 0.9

# Cálculo de lambada y miu
LAMBDA = MANUS_PER_HOUR * PAGES_PER_MANUS
MIU = 10

def initial_data():
    print('\n -----------------')
    print('| DATOS INICIALES |')
    print(' -----------------\n')
    print("Tamaño de Población (M) = Infinita")
    print(f"Número de servidores (k) = {K} en cada departamento")
    print(f"Tasa de llegada (\u03BB) = {LAMBDA}")
    print(f"Tasa de servicio (\u03BC) = {MIU}")


def a_literal():
    # Determinar la utilización del sistema
    p = LAMBDA / MIU

    print('\n -------------------------------------------------------------')
    print('| PROPORCIÓN DEL TIEMPO QUE ESTÁ LABORANDO DE UNA MECANÓGRAFA |')
    print(' -------------------------------------------------------------\n')
    print("Un solo departamento tiene una sola mecanógrafa")
    print(f" (\u03C1) = {p}")


# Probabilidad de no esperar en cola
def P0(LAMBDA_value, MIU_value):
    P0 = 1 - (LAMBDA_value / MIU_value)
    return P0


def b_literal():
    # Probabilidad de no esperar en cola
    P0_value = P0(LAMBDA, MIU)

    # Determinar el tiempo total diario
    Tt = (1 - P0_value) * WORKING_HOURS

    print('\n ------------------------------------------------')
    print('| TIEMPO TOTAL DIARIO QUE ESPERAN LOS EMPLEADOS |')
    print(' -----------------------------------------------\n')
    print(f'Probabilidad de hallar el sistema vacío {P0_value}')
    print('\nP0 en Tt')
    print(f'Tiempo total que esperan los empleados {Tt} horas/día')


def prob_n_exactly(MANUS, P0_value):
    count = 0
    summation = 0

    while(count <= MANUS):
        summation += (P0_value * ((LAMBDA/MIU) ** count))
        count += 1
    
    return summation


def c_literal():
    # Cantidad de manuscritos
    MANUS = 4

    # Probabilidad de no esperar en cola
    P0_value = P0(LAMBDA, MIU)

    # Probabilidad de hallar exactamente n clientes dentro del sistema
    P = 1 - prob_n_exactly(MANUS, P0_value)

    print('\n -----------------------------------------------')
    print('| PROBABILIDAD DE QUE HAYA MAS DE 3 MANUSCRITOS |')
    print(' -----------------------------------------------\n')
    print(f'Probabilidad de no esperar en la cola {P0_value}')
    print(f'Probabilidad de que haya mas de 3 manuscritos esperando o siendo mecanografiados {truncate(P, 3)}')


# En cada departamento laboran únicamente 5 empleados.
POPULATION = 5


def P0_finite_population(POPULATION_value, LAMBDA_value, MIU_value):
    return 1 / prob_empty_sys(POPULATION_value, LAMBDA_value, MIU_value)


def d_literal():
    # Probabilidad de hallar el sistema vacío dada una población (población finita)
    P0 = P0_finite_population(POPULATION, LAMBDA, MIU)

    # Número esperado de clientes en el sistema
    L = POPULATION - (MIU / LAMBDA) * (1 - P0)

    print('\n ----------------------------------------------')
    print('| NÚMERO ESPERADO DE MANUSCRITOS EN EL SISTEMA |')
    print(' ----------------------------------------------\n')
    print(f'Probabilidad de hallar el sistema vacío {truncate(P0, 3)}')
    print('P0 en L')
    print(f'Número esperado de manuscritos {truncate(L, 3)} manuscritos')


def e_literal():
    # Número esperado de clientes en la cola
    Lq = POPULATION - ((LAMBDA + MIU) / LAMBDA) * (1 - P0_finite_population(POPULATION, LAMBDA, MIU))

    print('\n -----------------------------------------------------')
    print('| NÚMERO ESPERADO DE EMPLEADOS ELABORANDO MANUSCRITOS |')
    print(' -----------------------------------------------------\n')
    print(f'Empleados elaborando manuscritos {truncate(Lq, 3)}')


def excer7_resolution():
    initial_data() 
    a_literal()
    b_literal()
    c_literal()
    d_literal()
    e_literal()