from ejer12 import excer12_resolution
from ejer7 import excer7_resolution
from os import system, name
from time import sleep
import time

# Limpiar pantalla
def clear_scr():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Imprimir el proceso de iteración
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r\t\t\t\t{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    
    # Print New Line on Complete
    if iteration == total: 
        print()


# Barra de carga
def loading_bar():
    # A List of Items
    items = list(range(0, 20))
    l = len(items)

    # Initial call to print 0% progress
    print('\n\t\t\t\t\t\t\tCARGANDO\n')
    printProgressBar(0, l, prefix = ':', suffix = '', length = 50)

    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = '', suffix = '', length = 50)

    sleep(1)
    clear_scr()


# Menú inicial
def initial_menu():
    clear_scr()
    loading_bar()
    print('\t\t\t\t\t ================================')
    print('\t\t\t\t\t|     TÉCNICAS DE SIMULACIÓN     |')
    print('\t\t\t\t\t ================================')
    print('\t\t\t\t\t|   EJERCICIOS TEORÍA DE COLAS   |')
    print('\t\t\t\t\t --------------------------------')
    print('\t\t\t\t\t|      GRUPO N°      |     4     |')
    print('\t\t\t\t\t --------------------------------')
    print('\t\t\t\t\t|    EJERCICIOS N°   |   7 y 12  |')
    print('\t\t\t\t\t --------------------------------')
    print('\t\t\t\t\t| INTEGRANTES |   Cuenca Alex    |')
    print('\t\t\t\t\t|             | Llinín Francisco |')
    print('\t\t\t\t\t --------------------------------')
    print('\n\t\t\t\t\t  Siendo redireccionado al menú...')
    sleep(4)


# Menú opcional
def opt_menu():
    initial_menu()
    
    clear_scr()

    while True:
        
        print('\t\t\t\t==========================================================')
        print("\t\t\t\t| Seleccione el ejercicio que desea observar su resolución |")
        print('\t\t\t\t ==========================================================')
        print('\t\t\t\t| Opción 1 |      Observar resolución del Ejercicio 7      |')
        print('\t\t\t\t-----------------------------------------------------------')
        print('\t\t\t\t| Opción 2 |      Observar resolución del Ejercicio 12     |')
        print('\t\t\t\t-----------------------------------------------------------')

        option = input("\t\t\t\t\t\t  Ingrese una opción: ")

        if(option > "2"):
            print(f"\n\t\t\t\t      {option} no es una opción válida. Vuelva a intentarlo")
            sleep(2)
        else:
            print(f"\n\t\t\t\t   {option} es una opción válida. Redireccionando al ejercicio {7 if option == '1' else 12}")
            sleep(2)

            break

        clear_scr()
    
    return option


option = opt_menu()

if option == "1":

    clear_scr()
    print('\t\t\t\t\t\t\t =====================')
    print("\t\t\t\t\t\t\t|     EJERCICIO 7     |")
    print('\t\t\t\t\t\t\t =====================')

    excer7_resolution()
else:
    if option == "2":

        clear_scr()
        print('\t\t\t\t\t\t =====================')
        print("\t\t\t\t\t\t|     EJERCICIO 12    |")
        print('\t\t\t\t\t\t =====================')

        excer12_resolution()