# Horas de trabajo
WORKING_HOURS = 12

# Número de servidores
K = 1

# Datos iniciales
LAMBDA = 1/6
MIU = 1/4

# Literal a

def prob_sistema_vacío():
    
    prob_sistema_vacío_value = 1 - (LAMBDA / MIU)

    print(f"La probabilidad de que el sistema este vacío es de {prob_sistema_vacío_value}")

def num_clientes_cola():
    num_clientes_cola_value = (LAMBDA ** 2) / (MIU * (MIU-LAMBDA))
    print(f"La cantidad de clientes en cola es de {num_clientes_cola_value}, que es aproximadamente")

def tiempo_esp_sistema():
    tiempo_esp_sistema_value = 1 / (MIU-LAMBDA)
    print(f"El tiempo esperado en el sistema es de {tiempo_esp_sistema} minutos")

def transforma_horas(value):
    return value * 60

def tiempo_esp_cola(LAMBDA_value, MIU_value):
    return (LAMBDA_value/(MIU_value*(MIU_value-LAMBDA_value)))


def cost_tot_diario():
    MIU_HORAS = transforma_horas(MIU)
    LAMBDA_HORAS = transforma_horas(LAMBDA)

    COST_UNITARIO_SERVIDOR = 100
    COST_UNITARIO_TIEMPO_COLA = 10

    cost_total_espera = LAMBDA_HORAS * WORKING_HOURS * tiempo_esp_cola(LAMBDA_HORAS, MIU_HORAS)*COST_UNITARIO_TIEMPO_COLA
    cost_tot_diario_value = COST_UNITARIO_SERVIDOR + cost_total_espera

    print(f"El costo total diario es: {cost_tot_diario_value}")

def main():
    print("Ejercicio Prueba Parcial")
    prob_sistema_vacío()
    num_clientes_cola()
    tiempo_esp_sistema()
    cost_tot_diario()





