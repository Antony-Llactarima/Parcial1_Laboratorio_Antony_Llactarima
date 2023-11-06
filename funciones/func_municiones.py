import datos_main as d_main

# DECLARACION DE LAS BALAS
def llenar_lista_balas(l_balas, cantidad_balas):
    while len(l_balas) < cantidad_balas:
        if cantidad_balas == 4:
            l_balas.append(d_main.d_bala_1.copy())
        elif cantidad_balas == 3:
            l_balas.append(d_main.d_bala_2.copy())

def reiniciar_balas(l_balas):
    for bala in l_balas:
        if bala['accion']:
            bala['accion'] = False

# MOVIMIENTO DE LAS MUNICIONES
def disparo_bala(l_balas):
    disparo = False
    for bala in l_balas:
        if bala['accion'] == False:
            bala['accion'] = True
            disparo = True
            break
    return disparo

def posicionar_bala(l_bala, player):
    p_centro_x = (player['tamanio'][0] / 2) + player['posicion'][0]
    p_centro_y = (player['tamanio'][1] / 2 ) + player['posicion'][1]
    for bala in l_bala:
        if bala['accion'] and bala['direccion'] == 'none':
            bala['direccion'] = str(player['direccion'])
            if bala['direccion'] == 'up':
                bala['posicion'] = [p_centro_x - (bala['t_ud'][0] / 2), p_centro_y - (bala['t_ud'][1] / 2)]
            elif bala['direccion'] == 'down':
                bala['posicion'] = [p_centro_x - (bala['t_ud'][0] / 2), p_centro_y + (bala['t_ud'][1] / 2)]
            elif bala['direccion'] == 'left':
                bala['posicion'] = [p_centro_x - (bala['t_ud'][0] / 2), p_centro_y - (bala['t_lr'][1] / 2)]
            elif bala['direccion'] == 'right':
                bala['posicion'] = [p_centro_x + (bala['t_ud'][0] / 2), p_centro_y - (bala['t_lr'][1] / 2)]

def mover_balas(l_bala):
    for bala in l_bala:
        if bala['accion']:
            if bala['direccion'] == 'up':
                bala['posicion'][1] -= bala['velocidad']
            elif bala['direccion'] == 'down':
                bala['posicion'][1] += bala['velocidad']
            if bala['direccion'] == 'left':
                bala['posicion'][0] -= bala['velocidad']
            elif bala['direccion'] == 'right':
                bala['posicion'][0] += bala['velocidad']

def definir_limite_bala(l_bala):
    for bala in l_bala:
        if bala['accion']:
            if bala['direccion'] == 'up' or bala['direccion'] ==  'down':
                bala['limite'] = [bala['posicion'][0] + bala['t_ud'][0], bala['posicion'][1] + bala['t_ud'][1]]
            else:
                bala['limite'] = [bala['posicion'][0] + bala['t_lr'][0], bala['posicion'][1] + bala['t_lr'][1]]

def seleccionar_img_balas(l_balas, img_balas):
    for bala in l_balas:
        if bala['accion']:
            if bala['direccion'] == 'up' or bala['direccion'] == 'down':
                bala['img'] = img_balas['up_down']
            else:
                bala['img'] = img_balas['left_right']

def restringir_balas(l_balas, tam_pantalla):
    for bala in l_balas:
        if bala['accion']:
            if bala['limite'][0] < 0 or bala['limite'][1] < 50:
                if bala['nivel'] == 1:
                    bala['accion'] = False
                    bala['direccion'] = 'none'
                else:
                    bala['direccion'] = 'none'
            elif bala['posicion'][0] > tam_pantalla[0] or bala['posicion'][1] > tam_pantalla[1]:
                if bala['nivel'] == 1:
                    bala['accion'] = False
                    bala['direccion'] = 'none'
                else:
                    bala['direccion'] = 'none'

def detectar_colision(l_balas, lista_enemigo, player):
    colision = False
    for bala in l_balas:
        if bala['accion']:
            for enemigo in lista_enemigo:
                if enemigo['spawn']:
                    if (bala['posicion'][0] < enemigo['limite'][0]) and (bala['limite'][0] > enemigo['posicion'][0]) and (bala['posicion'][1] < enemigo['limite'][1]) and (bala['limite'][1] > enemigo['posicion'][1]):
                        colision = True
                        enemigo['vida'] -= bala['danio']
                        if enemigo['vida'] <= 0:
                            player['puntaje'] += 1
                        if bala['nivel'] == 1:
                            bala['accion'] = False
                            bala['direccion'] = 'none'
                        else:
                            bala['direccion'] = 'none'
                        break
    return colision

def quitar_bala(l_balas):
    for i in range(len(l_balas)):
        if l_balas[i]['direccion'] == 'none' and l_balas[i]['accion']:
            l_balas.pop(i)
            break