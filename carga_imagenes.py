import pygame as pg
import os

dir_actual = os.getcwd()

# PANTALLA DE INICIO ----------------------------------------------------------------
pantalla_inicio = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_inicio\_menu_inicio.png"))
boton_jugar = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_inicio\_boton_jugar.png"))
boton_salir = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_inicio\_boton_salir.png"))
boton_puntos = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_inicio\_boton_puntos.png"))

# PANTALLA DE PUNTOS -------------------------------------
boton_atras = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_puntos\_boton_atras.png"))
# PANTALLA DE TUTORIAL -------------------------------------------------------------
pantalla_tutorial = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_tutorial\_pantalla_tutorial.png"))

# PANTALLA DEL JUEGO ----------------------------------------------------------------
piso_lab = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_suelo_main.png"))
barra_datos = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_datos.png"))
# BARRA VIDA ----------------------------------------------------------------
vida_llena = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_vida_full.png"))
vida_semillena = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_vida_semifull.png"))
vida_mitad = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_vida_mitad.png"))
vida_semibaja = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_vida_semimitad.png"))
vida_baja = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_vida_baja.png"))
vida_vacia = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_vida_vacia.png"))
# BARRA BALAS 1 --------------------------------
balas1_llena = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_balas1_lleno.png"))
balas1_semillena = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_balas1_casilleno.png"))
balas1_semibaja = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_balas1_casivacio.png"))
balas1_baja = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_balas1_baja.png"))
balas1_vacia = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_balas1_vacia.png"))
# BARRA BALAS 2 --------------------------------
balas2_llena = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_balas2_llena.png"))
balas2_mitad = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_balas2_mitad.png"))
balas2_baja = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_balas2_baja.png"))
balas2_vacia = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_juego\_barra_balas2_vacio.png"))
# JUGADOR --------------------------------
tank_up = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_jugador\_tank_up.png"))
tank_left = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_jugador\_tank_left.png"))
tank_down = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_jugador\_tank_down.png"))
tank_right = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_jugador\_tank_right.png"))
# ENEMIGO NIVEL 1 --------------------------------
enemigo_1_up = pg.image.load(os.path.join(dir_actual,'imgs\_personajes\_enemigo_1\_enemy1_up.png'))
enemigo_1_left = pg.image.load(os.path.join(dir_actual,'imgs\_personajes\_enemigo_1\_enemy1_left.png'))
enemigo_1_down = pg.image.load(os.path.join(dir_actual,'imgs\_personajes\_enemigo_1\_enemy1_down.png'))
enemigo_1_right = pg.image.load(os.path.join(dir_actual,'imgs\_personajes\_enemigo_1\_enemy1_right.png'))
advertencia_1 = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_1\_advertencia.png"))
# ENEMIGO NIVEL 2 --------------------------------
enemigo_2_up = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_2\_enemy2_up.png"))
enemigo_2_left = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_2\_enemy2_left.png"))
enemigo_2_down = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_2\_enemy2_down.png"))
enemigo_2_right = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_2\_enemy2_right.png"))
advertencia_2 = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_2\_advertencia_2.png"))
# ENEMIGO NIVEL 3 --------------------------------
enemigo_3_up = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_3\_enemy3_up.png"))
enemigo_3_left = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_3\_enemy3_left.png"))
enemigo_3_down = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_3\_enemy3_down.png"))
enemigo_3_right = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_3\_enemy3_right.png"))
enemigo_3_upleft = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_3\_enemy3_upleft.png"))
enemigo_3_upright = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_3\_enemy3_upright.png"))
enemigo_3_downleft = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_3\_enemy3_downleft.png"))
enemigo_3_downright = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_3\_enemy3_downright.png"))
advertencia_3 = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_3\_advertencia_3.png"))
# ENEMIGO NIVEL 4 --------------------------------
enemigo_4_upleft = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_4\_enemy4_upleft.png"))
enemigo_4_upright = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_4\_enemy4_upright.png"))
enemigo_4_downleft = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_4\_enemy4_downleft.png"))
enemigo_4_downright = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_4\_enemy4_downright.png"))
advertencia_4 = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_4\_advertencia_4.png"))
# ENEMIGO NIVEL 5 --------------------------------
enemigo_5_up = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_5\_enemy5_up.png"))
enemigo_5_down = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_5\_enemy5_down.png"))
advertencia_5_up = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_5\_advertencia_5_up.png"))
advertencia_5_down = pg.image.load(os.path.join(dir_actual,"imgs\_personajes\_enemigo_5\_advertencia_5_down.png"))
# BALA NIVEL 1 -------------------------------------
bala_1_up_down = pg.image.load(os.path.join(dir_actual,"imgs\_balas\_bala_1\_bala_ud_1.png"))
bala_1_left_right = pg.image.load(os.path.join(dir_actual,"imgs\_balas\_bala_1\_b_lr_1.png"))
# BALA NIVEL 2 -------------------------------------
bala_2_up = pg.image.load(os.path.join(dir_actual,"imgs\_balas\_bala_2\_b_ud_2.png"))
bala_2_left = pg.image.load(os.path.join(dir_actual,"imgs\_balas\_bala_2\_b_left_2.png"))
bala_2_down = pg.image.load(os.path.join(dir_actual,"imgs\_balas\_bala_2\_b_down_2.png"))
bala_2_right = pg.image.load(os.path.join(dir_actual,"imgs\_balas\_bala_2\_b_right_2.png"))
# VIDA EXTRA --------------------------------
vida_up_1 = pg.image.load(os.path.join(dir_actual,"imgs\_powerUps\_vida_extra.png"))
# ITEM BALA 2 --------------------------------
bala_item_2 = pg.image.load(os.path.join(dir_actual,"imgs\_balas\_bala_2\_item_bala2.png"))

# PANTALLA GAME OVER -----------------------------------------------------------------------
pantalla_gameOver = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_gameOver\_pantalla_gameOver.png"))
boton_menu = pg.image.load(os.path.join(dir_actual,"imgs\img_tecnicos\_pantalla_gameOver\_boton_menu.png"))

# DICCIONARIOS DE LAS IMAGENES
# DICC. PNTALLAS -------------------------------------------------
pantalla_imgs = {
    'inicio': pantalla_inicio,
    'tutorial': pantalla_tutorial,
    'gameOver': pantalla_gameOver,
    'juego': piso_lab,
    'barra': barra_datos
}

# DICC. BOTONES -------------------------------------------------
botones_imgs = {
    'jugar': boton_jugar,
    'menu': boton_menu,
    'salir': boton_salir,
    'puntos': boton_puntos,
    'atras': boton_atras
}

# DICC. BARRA VIDAS ------------------------------------------------
vida_imgs = {
    'llena' : vida_llena,
    'semi_llena': vida_semillena,
    'mitad': vida_mitad,
    'semi_baja': vida_semibaja,
    'baja': vida_baja,
    'vacia': vida_vacia,
}

# DICC. JUGADOR -------------------------------------------------
tank_imgs = {
    'up' : tank_up,
    'left' : tank_left,
    'down' : tank_down,
    'right' : tank_right
}

# DICC. ENEMIGO 1 -------------------------------------------------
enemigo_1_imgs = {
    'up': enemigo_1_up,
    'left':enemigo_1_left,
    'down': enemigo_1_down,
    'right': enemigo_1_right,
    'none': advertencia_1
}
# DICC. ENEMIGO 2 -------------------------------------------------
enemigo_2_imgs = {
    'up': enemigo_2_up,
    'left':enemigo_2_left,
    'down': enemigo_2_down,
    'right': enemigo_2_right,
    'none': advertencia_2
}
# DICC. ENEMIGO 3 -------------------------------------------------
enemigo_3_imgs = {
    'up': enemigo_3_up,
    'down' : enemigo_3_down,
    'left' : enemigo_3_left,
    'right' : enemigo_3_right,
    'down_left' : enemigo_3_downleft,
    'down_right' : enemigo_3_downright,
    'up_left' : enemigo_3_upleft,
    'up_right' : enemigo_3_upright,
    'none': advertencia_3

}

# DICC. ENEMIGO 4 -------------------------------------------------
enemigo_4_imgs = {
    'down_left' : enemigo_4_downleft,
    'down_right' : enemigo_4_downright,
    'up_left' : enemigo_4_upleft,
    'up_right' : enemigo_4_upright,
    'none': advertencia_4
}

# DICC. ENEMIGO 5 -------------------------------------------------
enemigo_5_imgs = {
    'up': enemigo_5_up,
    'down': enemigo_5_down,
    'none_down': advertencia_5_down,
    'none_up': advertencia_5_up
}

# DICC. BALA 1
bala_1_imgs = {
    'left_right': bala_1_left_right,
    'up_down': bala_1_up_down
}

# DICC. BARRA BALA 1--------------------------------
barra_bala1_img = {
    'llena': balas1_llena,
    'semillena': balas1_semillena,
    'semibaja': balas1_semibaja,
    'baja': balas1_baja,
    'vacia': balas1_vacia
}

# DICC- BALA 2
bala_2_imgs = {
    'up': bala_2_up,
    'left': bala_2_left,
    'down': bala_2_down,
    'right': bala_2_right
}

# DICC. BARRA BALA 2 --------------------------------
barra_bala2_img = {
    'llena': balas2_llena,
    'mitad': balas2_mitad,
    'baja': balas2_baja,
    'vacia': balas2_vacia
}
