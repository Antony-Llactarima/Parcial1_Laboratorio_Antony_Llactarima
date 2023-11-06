import random as rd

def aumentar_vida(player, power_up):
    if player['vida'] < 5:
        player['vida'] += power_up['nivel']
    else:
        player['vida'] += 0

def colision_power_up(power_up, player):
    colision = False
    if (player['posicion'][0] < power_up['limite'][0]) and (player['posicion'][1] < power_up['limite'][1]) and (player['limite'][0] > power_up['posicion'][0]) and (player['limite'][1] > power_up['posicion'][1]):
        colision = True
    return colision

def posicion_power_up(tam_pantalla):
    posX = rd.randint(0,tam_pantalla[0] - 50)
    posY = rd.randint(50,tam_pantalla[1] - 50)
    return [posX, posY]

def limite_power_up(power):
    power['limite'] = [power['posicion'][0] + power['tamanio'][0], power['posicion'][1] + power['tamanio'][1]]