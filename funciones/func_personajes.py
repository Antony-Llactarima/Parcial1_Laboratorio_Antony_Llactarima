import random as rd
import datos_main as d_main

# DECLARACION DE LA PANTALLA
def dec_pantalla():
    return d_main.pantalla.copy()

def detectar_click(posicion, pos_objetivo, limit_objetivo) -> bool:
    if (posicion[0] > pos_objetivo[0]) and (posicion[0] < limit_objetivo[0]) and (posicion[1] > pos_objetivo[1]) and (posicion[1] < limit_objetivo[1]):
        return True
    return False


# FUNCIONES DE LOS PERSONAJES
def mover_personaje(personaje:dict):
    '''
    DESCRIPCION:
    Se encarga de darle una posicion nueva, sumando o restando la
    velocidad a la posicion, a los personajes que se reciben por parametro.
    
    QUE RECIBE:
    Recibe el diccionario del personaje al que se le cambiara la posicion
    segun su direccion.
    
    QUE DEVUELVE:
    No devuel nada, realiza el cambio directamente al diccionario del personaje.
    '''
    if personaje['direccion'] == "left":
        personaje['posicion'][0] -= personaje['velocidad']
    elif personaje['direccion'] == "right":
        personaje['posicion'][0] += personaje['velocidad']
    elif personaje['direccion'] == "up":
        personaje['posicion'][1] -= personaje['velocidad']
    elif personaje['direccion'] == "down":
        personaje['posicion'][1] += personaje['velocidad']
        
    elif personaje['direccion'] == "up_left":
        personaje['posicion'][1] -= personaje['velocidad']
        personaje['posicion'][0] -= personaje['velocidad']
    elif personaje['direccion'] == "up_right":
        personaje['posicion'][1] -= personaje['velocidad']
        personaje['posicion'][0] += personaje['velocidad']
    elif personaje['direccion'] == "down_left":
        personaje['posicion'][1] += personaje['velocidad']
        personaje['posicion'][0] -= personaje['velocidad']
    elif personaje['direccion'] == "down_right":
        personaje['posicion'][1] += personaje['velocidad']
        personaje['posicion'][0] += personaje['velocidad']

def restringir_movimiento(personaje:dict, tam_pantalla:tuple):
    '''
    DESCRIPCION:
    Se encarga de detener a los personajes que estan por salirse 
    de la pantalla o de la zona jugable.
    
    QUE RECIBE:
    Recibe el diccionario del personaje que se verificara si esta
    por atravesar la pantalla de juego.
    Tambien recibe el tamaño limite por donde puede estar.
    
    QUE DEVUELVE:
    No devuel nada, realiza el cambio directamente al diccionario del personaje.
    '''
    if personaje['posicion'][0] < 0:
        personaje['posicion'][0] = 0
    elif personaje['limite'][0] > tam_pantalla[0]:
        personaje['posicion'][0] = tam_pantalla[0] - personaje['tamanio'][0]
    if personaje['posicion'][1] < 50:
        personaje['posicion'][1] = 50
    elif personaje['limite'][1] > tam_pantalla[1]:
        personaje['posicion'][1] = tam_pantalla[1] - personaje['tamanio'][1]

def definir_limite(personaje:dict):
    '''
    DESCRIPCION:
    Se encarga de añadir una nueva llave al diccionario del personaje recibido,
    esta llave indica el limite del cuerpo.
    
    QUE RECIBE:
    Recibe el diccionario del personaje.
    
    QUE DEVUELVE:
    No devuel nada, realiza el cambio directamente al diccionario del personaje.
    '''
    personaje['limite'] = [personaje['posicion'][0] + personaje['tamanio'][0],
        personaje['posicion'][1] + personaje['tamanio'][1]]

# FUNCIONES DE LOS ENEMIGOS

def elegir_enemigos(puntaje:int):
    '''
    DESCRIPCION:
    Se encarga de elegir un enemigo aleatoriamente
    mediante la eleccion de un numero que depende del puntaje,
    para aniadirlo a la lista de enemigos.
    
    PARAMETRO:
    Recibe el puntaje, que decide hasta que nivel de enemigo
    puede aparecer.
    
    QUE DEVUELVE:
    Devuelve el numero random que define que enemigo
    añadir a la lista.
    '''
    if puntaje < 10:
        enemigo = rd.randint(1,2)
    elif puntaje < 15:
        enemigo = rd.randint(1,3)
    elif puntaje < 20:
        enemigo = rd.randint(1,4)
    else:
        enemigo = rd.randint(1,5)
    return enemigo

def aniadir_enemigo(e_aniadir:int):
    '''
    DESCRIPCION:
    Se encarga de, mediante le numero random, elegir y añadir
    el enemigo a la lista.
    
    PARAMETRO:
    Recibe la lista de enemigos al cual añadira
    un enemigo y el numero que indica que 
    enemigo añadir.
    
    QUE DEVUELVE:
    Devuelve el diccionario del enemigo seleccionado.
    '''
    if e_aniadir == 1:
        enemigo = d_main.enem_1.copy()
    elif e_aniadir == 2:
        enemigo = d_main.enem_2.copy()
    elif e_aniadir == 3:
        enemigo = d_main.enem_3.copy()
    elif e_aniadir == 4:
        enemigo = d_main.enem_4.copy()
    elif e_aniadir == 5:
        enemigo = d_main.enem_5.copy()
    return enemigo

def completar_lista_enemigos(l_enemigos:list, puntos:int, c_enemigos):
    '''
    DESCRIPCION:
    Se encarga de añadir las suficientes enemigos a la lista para
    que este completa.
    '''
    if len(l_enemigos) < c_enemigos:
        for i in range(c_enemigos):
            e_aniadir = elegir_enemigos(puntos)
            enemigo = aniadir_enemigo(e_aniadir)
            l_enemigos.append(enemigo)
            if len(l_enemigos) == c_enemigos:
                break

def regerar_enemigos(l_enemigos:list, puntos:int)->None:
    for i in range(len(l_enemigos)):
        if l_enemigos[i]['vida'] <= 0:
            e_reemplazo = elegir_enemigos(puntos)
            l_enemigos[i] = aniadir_enemigo(e_reemplazo)

def posicionar_enemigos(tam_pantalla, l_enemigos, player):
    for enemigo in l_enemigos:
        if 'posicion' in enemigo:
            pass
        elif enemigo['nivel'] < 5:
            enemigo['posicion'] = [rd.randint(0, tam_pantalla[0] - enemigo['tamanio'][0]),rd.randint(50, tam_pantalla[1] - enemigo['tamanio'][1])]
        else:
            enemigo['posicion'] = [player['posicion'][0], 0 - enemigo['tamanio'][1]]

def dir_enemy_nivel1(centro_x, centro_y, player):
    '''
    DESCRIPCION:
    Direcciona al enemigo de nivel hacia el jugador,
    primero por eje x y luego por eje y.
    
    QUE RECIBE:
    Recibe el centro del enemigo para detectar
    si esta en rango del jugador.
    
    QUE DEVUELVE:
    Devuelve la direccion que tiene que seguir para
    acercarse al jugador.
    '''
    direccion = 'none'
    if centro_x >= player['limite'][0]:
        direccion = 'left'
    elif centro_x <= player['posicion'][0]:
        direccion = 'right'
    elif centro_y >= player['limite'][1]:
        direccion = 'up'
    elif centro_y <= player['posicion'][1]:
        direccion = 'down'
    return direccion

def dir_enemy_nivel2(centro_x, centro_y, player):
    '''
    DESCRIPCION:
    Direcciona al enemigo de nivel hacia el jugador,
    primero por eje y y luego por eje x.
    
    QUE RECIBE:
    Recibe el centro del enemigo para detectar
    si esta en rango del jugador.
    
    QUE DEVUELVE:
    Devuelve la direccion que tiene que seguir para
    acercarse al jugador.
    '''
    direccion = 'none'
    if centro_y >= player['limite'][1]:
        direccion = 'up'
    elif centro_y <= player['posicion'][1]:
        direccion = 'down'
    elif centro_x >= player['limite'][0]:
        direccion = 'left'
    elif centro_x <= player['posicion'][0]:
        direccion = 'right'
    return direccion

def dir_enemy_nivel3(centro_x, centro_y, player):
    '''
    DESCRIPCION:
    Direcciona al enemigo de nivel 3 hacia el jugador,
    primero por las diagonales y luego por eje Y o X.
    
    QUE RECIBE:
    Recibe el centro del enemigo para detectar
    si esta en rango del jugador.
    
    QUE DEVUELVE:
    Devuelve la direccion que tiene que seguir para
    acercarse al jugador.
    '''
    direccion = 'none'
    if (centro_y < player['posicion'][1]) and (centro_x < player['posicion'][0]):
        direccion = 'down_right'
    elif (centro_y > player['limite'][1]) and (centro_x < player['posicion'][0]):
        direccion = 'up_right'
    elif (centro_y > player['limite'][1]) and (centro_x > player['limite'][0]):
        direccion = 'up_left'
    elif (centro_y < player['posicion'][1]) and (centro_x > player['limite'][0]):
        direccion = 'down_left'
    elif (centro_x >= player['posicion'][0]) and (centro_x <= player['limite'][0]):
        if (centro_y <= player['posicion'][1]):
            direccion = 'down'
        elif (centro_y >= player['limite'][1]):
            direccion = 'up'
    elif (centro_y >= player['posicion'][1]) and (centro_y <= player['limite'][1]):
        if (centro_x <= player['posicion'][0]):
            direccion = 'right'
        elif (centro_x >= player['limite'][0]):
            direccion = 'left'
    return direccion

def dir_enemy_nivel4(enemigo):
    if enemigo['direccion'] == 'none':
        e_direccion = rd.randint(0,3)
        if e_direccion == 0:
            enemigo['direccion'] = 'down_left'
        elif e_direccion == 1:
            enemigo['direccion'] = 'down_right'
        elif e_direccion == 2:
            enemigo['direccion'] = 'up_left'
        elif e_direccion == 3:
            enemigo['direccion'] = 'up_right'

def cambiar_direccion(enemigo, tam_pantalla):
    if (enemigo['posicion'][0] + enemigo['tamanio'][0]) > tam_pantalla[0]:
        if enemigo['direccion'] == 'up_right':
            enemigo['direccion'] = 'up_left'
        else:
            enemigo['direccion'] = 'down_left'
    elif enemigo['posicion'][0] < 0:
        if enemigo['direccion'] == 'up_left':
            enemigo['direccion'] = 'up_right'
        else:
            enemigo['direccion'] = 'down_right'
    elif (enemigo['posicion'][1] + enemigo['tamanio'][1]) > tam_pantalla[1]:
        if enemigo['direccion'] == 'down_right':
            enemigo['direccion'] = 'up_right'
        else:
            enemigo['direccion'] = 'up_left'
    elif enemigo['posicion'][1] < 50:
        if enemigo['direccion'] == 'up_left':
            enemigo['direccion'] = 'down_left'
        else:
            enemigo['direccion'] = 'down_right'

def dir_enemy_nivel5(enemigo, tam_pantalla):
    if enemigo['direccion'] == 'none_down':
        enemigo['direccion'] = 'down'
        enemigo['spawn'] = True
    elif enemigo['direccion'] == 'none_up':
        enemigo['direccion'] = 'up'
        enemigo['spawn'] = True
    elif enemigo['direccion'] == 'down' and enemigo['posicion'][1] > tam_pantalla[1]:
        enemigo['direccion'] = 'none_up'
        enemigo['timeWait'] = 45
        enemigo['spawn'] = False
    elif enemigo['direccion'] == 'up' and enemigo['posicion'][1] + enemigo['tamanio'][1] < 50:
        enemigo['direccion'] = 'none_down'
        enemigo['timeWait'] = 45
        enemigo['spawn'] = False

def direccionar_enemigos(enemigo:dict, player:dict, tam_pantalla:list):
    '''
    DESCRIPCION:
    Se encarga de enviar los enemigos a sus respectivas funcionas para
    que puedan direccionarlo hacia el jugador.
    
    QUE RECIBE:
    Recibe el diccionario del enemigo.
    Tambien recibe el diccionario del jugador.
    
    QUE DEVUELVE:
    No devuelve nada.
    Cambia directamente el diccionario del enemigo.
    '''
    centro_x = (enemigo['tamanio'][0] / 2) + enemigo['posicion'][0]
    centro_y = (enemigo['tamanio'][1] / 2) + enemigo['posicion'][1]
    if enemigo['nivel'] == 1:
        enemigo['direccion'] = dir_enemy_nivel1(centro_x, centro_y, player)
        if enemigo['direccion'] == 'up' or enemigo['direccion'] == 'down':
            enemigo['velocidad'] = 5
        else:
            enemigo['velocidad'] = 3
    elif enemigo['nivel'] == 2:
        enemigo['direccion'] = dir_enemy_nivel2(centro_x, centro_y, player)
        if enemigo['direccion'] == 'left' or enemigo['direccion'] == 'right':
            enemigo['velocidad'] = 5
        else:
            enemigo['velocidad'] = 3
    elif enemigo['nivel'] == 3:
        enemigo['direccion'] = dir_enemy_nivel3(centro_x,centro_y, player)
    elif enemigo['nivel'] == 4:
        dir_enemy_nivel4(enemigo)
        cambiar_direccion(enemigo, tam_pantalla)
    elif enemigo['nivel'] == 5:
        dir_enemy_nivel5(enemigo, tam_pantalla)

def colision_enemigo(l_enemigos, player):
    choque = False
    for enemigo in l_enemigos:
        if enemigo['spawn']:
            if (enemigo['limite'][0] - 10 > player['posicion'][0]) and (enemigo['posicion'][0] + 10 < player['limite'][0]) and (enemigo['limite'][1] - 10 > player['posicion'][1]) and (enemigo['posicion'][1] + 10 < player['limite'][1]) :
                player['vida'] -= 1
                enemigo['vida'] = 0
                choque = True
                break
    return choque

def image_enemigo(enemigo, l_imgs):
    if enemigo['direccion'] != 'none':
        enemigo['img'] = l_imgs[enemigo['direccion'] ]

def reinicio_enemigo(l_enemigos, c_enemigos):
    if len(l_enemigos) > c_enemigos:
        while len(l_enemigos) > c_enemigos:
            l_enemigos.pop(len(l_enemigos) - 1)
    for enemigo in l_enemigos:
        enemigo['vida'] = 0


# FUNCINOES DEL JUGADOR
def declaracion_jugador():
    jugador = d_main.p_tank.copy()
    jugador['direccion'] = "down"
    return jugador

def posicionar_jugador(jugador, tam_pantalla):
    centro_x = jugador['tamanio'][0] / 2
    centro_y = jugador['tamanio'][1] / 2
    pos_x = (tam_pantalla[0] / 2) - centro_x
    pos_y = (tam_pantalla[1] / 2) - centro_y
    jugador['posicion'] = [pos_x, pos_y]

def definir_velocidad_jugador(jugador, arranque):
    if jugador['puntaje'] < 10 and arranque:
        jugador['velocidad'] = 8
    elif jugador['puntaje'] >= 10 and arranque:
        jugador['velocidad'] = 10

# EXTRAS
def aumentar_enemigos(puntaje):
    if puntaje < 10:
        cantidad_enemigos = 5
    elif puntaje < 20:
        cantidad_enemigos = 6
    elif puntaje < 30:
        cantidad_enemigos = 7
    else:
        cantidad_enemigos = 8
    return cantidad_enemigos