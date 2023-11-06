
def abrir_puntajes(l_puntaje)-> list:
    try:
        with open("puntajes\mayores_puntajes.txt", "r") as file_puntaje:
            l_puntaje = file_puntaje.readlines()
        for i in range(len(l_puntaje)):
            l_puntaje[i] = l_puntaje[i].strip()
    except:
        print("No se pudo obtener los puntajes")
    
    return l_puntaje

def acomodar_puntajes(l_puntaje, puntaje_actual):
    aux_puntaje_a = 0
    aux_puntaje_b = 0
    cambiar_lista = False
    
    for i in range(len(l_puntaje)):
        if cambiar_lista:
            aux_puntaje_b = l_puntaje[i]
            l_puntaje[i] = aux_puntaje_a
            aux_puntaje_a = aux_puntaje_b
        elif puntaje_actual > int(l_puntaje[i]):
            aux_puntaje_a = l_puntaje[i]
            l_puntaje[i] = str(puntaje_actual)
            cambiar_lista = True
    return cambiar_lista

def reescribir_puntaje(l_puntaje):
    try:
        with open("puntajes\mayores_puntajes.txt", "w") as file_puntaje:
            for i in range(len(l_puntaje)):
                if i != len(l_puntaje) - 1:
                    file_puntaje.write(f"{l_puntaje[i]}\n")
                else:
                    file_puntaje.write(f"{l_puntaje[i]}")
    
    except:
        print("No se reescribir el archivo de puntajes")

# MOSTRAR EN PANTALLA EL PUNTAJE ----------------------------------
def mostrar_puntaje(l_putajes):
    
    pass