import os

def abrir_puntajes(l_puntaje:list, dir_actual:str)-> list:
    '''
    DESCRIPCION: 
    La funcion se encarga de buscar el archivo de los mejores puntajes
    y llenar la lista de puntajes.
    
    ARGUMENTOS:
    Recibe la lista de puntajes vacia, donde se colocaran los puntajes 
    del archivo.
    Tambien recibe la direccion del directorio actual.
    
    RETORNA:
    Retorna la lista recibida con los puntajes del archivo.
    '''
    lista_aux = []
    try:
        with open(os.path.join(dir_actual, "puntajes\mayores_puntajes.txt")) as file_puntaje:
            lista_aux = file_puntaje.readlines()
        for i in range(len(lista_aux)):
            l_puntaje.append(lista_aux[i].strip())
    except:
        print("No se pudo obtener los puntajes")
    
    if len(l_puntaje) > 0:
        return True
    return False

def acomodar_puntajes(l_puntaje:list, puntaje_actual:int):
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

def reescribir_puntaje(l_puntaje:list, dir_actual:str):
    try:
        with open(os.path.join(dir_actual,"puntajes\mayores_puntajes.txt"),"w") as file_puntaje:
            for i in range(len(l_puntaje)):
                if i != len(l_puntaje) - 1:
                    file_puntaje.write(f"{l_puntaje[i]}\n")
                else:
                    file_puntaje.write(f"{l_puntaje[i]}")
    
    except:
        print("No se reescribir el archivo de puntajes")
