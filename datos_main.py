# DICCIONARIOS DE PERSONAJES QUE APARECEN EN EL JUEGO

# PANTALLA
pantalla = {
    'tamanio': [1280, 720],
    'color': (0,0,0),
    'menu': True,
    'tutorial': False,
    'game_over': False,
    'juego': False
}

# PERSONAJES
p_tank = {
    'nombre': 'Tanke Jugador',
    'vida': 5,
    'velocidad': 0,
    'tamanio' : [50,50],
    'puntaje': 0
}


# ENEMIGOS
enem_1 = {
    'nivel': 1,
    'vida': 15,
    'velocidad': 3,
    'tamanio' : [60,60],
    'direccion': 'none',
    'timeWait': 0,
    'spawn': False
}

enem_2 = {
    'nivel': 2,
    'vida': 20,
    'velocidad': 3,
    'tamanio' : [60,60],
    'direccion': 'none',
    'timeWait': 0,
    'spawn': False
}

enem_3 = {
    'nivel': 3,
    'vida': 25,
    'velocidad': 4,
    'tamanio' : [60,60],
    'direccion': 'none',
    'timeWait': 0,
    'spawn': False
}

enem_4 = {
    'nivel': 4,
    'vida': 25,
    'velocidad': 10,
    'tamanio' : [50,50],
    'direccion': 'none',
    'timeWait': 0,
    'spawn': False
}

enem_5 = {
    'nivel': 5,
    'vida': 30,
    'velocidad': 30,
    'tamanio' : [60,200],
    'direccion': 'none_down',
    'timeWait': 45,
    'spawn': False
}

# LAS MUNICIONES QUE SE USARAN
d_bala_1 = {
    'nivel': 1,
    'velocidad': 25,
    'danio': 5,
    't_ud' : [10, 20],
    't_lr' : [20,10],
    'direccion': 'none',
    'accion': False
}

d_bala_2 = {
    'nivel': 2,
    'velocidad': 25,
    'danio': 15,
    't_ud' : [10, 20],
    't_lr' : [20,10],
    'direccion': 'none',
    'accion': False
}

# POWER UPS
mas_vida = {
    'nivel': 1,
    'tamanio': [50,50]
}

item_bala2 = {
    'nivel': 2,
    'tamanio': [50,50]
}