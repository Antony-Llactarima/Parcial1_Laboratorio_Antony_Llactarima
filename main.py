# IMPORTACIONES IMPORTANTES ------------------------------------------------------------
import pygame as pg
from funciones.func_personajes import *
import carga_imagenes as c_img
from funciones.func_municiones import *
from funciones.func_powerup import *
from funciones.func_puntaje import *
import os

# INICIALIZACION DE PYGAME Y MIXER ------------------------------------------------------------
pg.init()
pg.mixer.init()

# DECLARACION DE EL DIRECTORIO ACTUAL -------------------------------------------
dir_actual = os.getcwd()

# DECLARACION DE LA PANTALLA ------------------------------------------------------------
pantalla = dec_pantalla()

# INICIO DE PANTALLA Y TITULO ------------------------------------------------------------
screen = pg.display.set_mode(pantalla['tamanio'])
pg.display.set_caption("SUPER TANK (Parcila 1)")

# BUSCAR LA MUSICA Y SONIDOS QUE SE USARAN ---------------------------------------------
try:
    pg.mixer.music.load(os.path.join(dir_actual, "sounds\_menu\loop-menu-preview-109594.mp3"))
    # EFECTOS DE SONIDO ------------------------------------------------------------
    # BALA 1  --------------------------------
    disparo1_sound = pg.mixer.Sound(os.path.join(dir_actual,"sounds\_balas\shooting-sound-fx-159024.mp3"))
    sin_balas_sound = pg.mixer.Sound(os.path.join(dir_actual,"sounds\_balas\_rifle-clip-empty-98832.mp3"))
    # BALA 2  -----------------------
    disparo2_sound = pg.mixer.Sound(os.path.join(dir_actual,"sounds\_balas\shoot02wav-14562.mp3"))
    # SONIDOS DE BOTONES ----------------------------------------------------------
    click_boton_jugar_sound = pg.mixer.Sound(os.path.join(dir_actual,"sounds\_botones\_click-menu-app-147357.mp3"))
    click_boton_menu_sound = pg.mixer.Sound(os.path.join(dir_actual,"sounds\_botones\interface-124464.mp3"))
    # EFECTOS CON ENEMIGOS --------------------------------------------------------
    colision_sound = pg.mixer.Sound(os.path.join(dir_actual,"sounds\_enemigos\musket-explosion-6383.mp3"))
    disparo_enemigo_sound = pg.mixer.Sound(os.path.join(dir_actual,"sounds\_enemigos\explosion-36210.mp3"))
    # SONIDO DE POWER UPS
    aparicion_powers_sound = pg.mixer.Sound(os.path.join(dir_actual,"sounds\_power_ups\energy-90321.mp3"))
    colision_powr_sound = pg.mixer.Sound(os.path.join(dir_actual,"sounds\_power_ups\coin-upaif-14631 (1).mp3"))
    # SONIDO DE GAME OVER --------------------------------------------------------
    game_over_sound = pg.mixer.Sound(os.path.join(dir_actual,"sounds\game_over\gameover-86548.mp3"))
    sound_music_encontrada = True
except:
    print("Error... no se pudo encontrar los Sonidos")
    sound_music_encontrada = False

# RECOPILACION DE LOS MEJORES PUNTAJES --------------------------------
l_puntaje = []
archivo_abierto = abrir_puntajes(l_puntaje, dir_actual)

# IMPORTACION DE TEXTO ------------------------------------------------------------
f_sans_serif = pg.font.SysFont('sans-serif', 50)

# POSICIONES DE LOS BOTONES EN PANTALLA DE INICIO --------------------------------
pantalla_mitad = [pantalla['tamanio'][0]/2, pantalla['tamanio'][1]/2]
pos_btn_jugar = [0, pantalla['tamanio'][1] - 200]
pos_btn_salir =  [pantalla['tamanio'][0] - 300 , pantalla['tamanio'][1] - 200]
pos_btn_puntos = [pantalla_mitad[0] - 125, 500]
limit_btn_jugar = [pos_btn_jugar[0] + 300, pos_btn_jugar[1] + 200]
limit_btn_salir = [pos_btn_salir[0] + 300, pos_btn_salir[1] + 200]
limit_btn_puntos = [pos_btn_puntos[0] + 250, pos_btn_puntos[1] + 100]

# POSICIONAR BOTONES DE GAME OVER ------------------------
pos_btn_menu = [0, pantalla['tamanio'][1] - 200]
limit_btn_menu = [pos_btn_menu[0] + 300, pos_btn_menu[1] + 200]

# FRAMES POR SEGUNDOS --------------------------------------------
fps = 30

# DETECTOR DE CLICK EN LOS BOTONES --------------------------------------------
clicked = False

# BANDERA PARA CORRER EL JUEGO --------------------------------------------
juego_activo = True

# ACTIVAR LA MUSICA DE INICIO --------------------------------------------
if sound_music_encontrada:
    pg.mixer.music.set_volume(.4)
    pg.mixer.music.play(loops=-1)

# INICIO DEL BUCLE PRINCIPAL ----------------------------------------------
while juego_activo:
    
    # CONTROLAR LOS FRAMES POR SEGUNDO --------------------------------
    pg.time.Clock().tick(fps)
    
    # DETECCION DE TECLADO --------------------------------------------
    for event in pg.event.get():
        if event.type == pg.QUIT:
            juego_activo = False
        
        # DETECCION EN PANTALLA DE INICIO Y PANTALLA GAME OVER -------------------------
        if pantalla['menu'] or pantalla['game_over'] or pantalla['puntos']:
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                clicked = True
            
            # DETECCION EN PANTALLA DEL JUEGO -----------------------------------------
        elif pantalla['juego']:
            # DETECCION PARA EL MOVIMIENTO --------------------------------
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    player['direccion'] = 'left'
                    f_velocidad = True
                elif event.key == pg.K_RIGHT:
                    player['direccion'] = 'right'
                    f_velocidad = True
                elif event.key == pg.K_UP:
                    player['direccion'] = 'up'
                    f_velocidad = True
                elif event.key == pg.K_DOWN:
                    player['direccion'] = 'down'
                    f_velocidad = True
                # DETECCION PARA EL DISPARO --------------------------------
                if event.key == pg.K_z:
                    if disparo_bala(l_balas_1):
                        if sound_music_encontrada:
                            disparo1_sound.play()
                    else:
                        if sound_music_encontrada:
                            sin_balas_sound.play()
                elif event.key == pg.K_x:
                    if len(l_balas_2) > 0:
                        disparo_bala(l_balas_2)
                        if sound_music_encontrada:
                            disparo2_sound.play()
                    else:
                        if sound_music_encontrada:
                            sin_balas_sound.play()
    
    # CORRIENDO LA PANTALLA DE INICIO ---------------------------------------------
    if pantalla['menu']:
        # EVENTOS SI CLICKEA DENTRO DE PANTALLA DE INICIO ----------------------
        if clicked:
            # EVENTOS SI CLICKEO EN 'JUGAR' ------------------------------------
            if detectar_click(mouse_pos, pos_btn_jugar, limit_btn_jugar):
                # LISTA DE ENEMIGOS --------------------------------
                l_enemigos = []
                # LISTA DE BALAS 1 --------------------------------------------
                l_balas_1 = []
                # LISTA DE BALAS 2 ---------------------------------------------
                l_balas_2 = []
                # CANTIDAD INICIAL DE ENEMIGOS
                # c_inicial_enemigos = 5
                # CANTIDAD DE BALAS 1 ------------------------------------------
                c_balas_1 = 4
                # CANTIDAD DE BALAS 2 ------------------------------------------
                c_balas_2 = 3
                # DECLARACION DEL JUGADOR --------------------------------
                player = declaracion_jugador()
                posicionar_jugador(player, pantalla['tamanio'])
                definir_limite(player)
                # BANDERA DEL MOVIMIENTO DEL JUGADOR -------------------------------
                f_velocidad = False
                
                # DECLARACION DE LAS BALAS 1 -----------------------------------
                llenar_lista_balas(l_balas_1, c_balas_1)
                
                # CAMBIO DE PANTALLA --------------------------------------------
                pantalla['menu'] = False
                pantalla['tutorial'] = True
                # INICIO TEMPORAL DE LA PANTALLA DE INICIO ---------------------
                time_tutorial = 0
                
                # BANDERAS PARA HACER A PARECER ITEMS ----------------------------
                aparecer_vida = False
                f_bala2 = False
                
                # CUANTOS SEGUNDOS SERA EL TUTORIAL ------------------------------
                segundos_transcurridos = 4
                # DETENER LA MUSICA --------------------------------
                if sound_music_encontrada:
                    pg.mixer.music.stop()
                    # SONIDO DE CLICKEO --------------------------------------------
                    click_boton_jugar_sound.play()
                
                # DEJAR EL CLICKEO EN FALSO -------------------------------------
                clicked = False
                
                # EVENTOS SI SE CLICKEA EN 'SALIR' ---------------------------------
            elif detectar_click(mouse_pos, pos_btn_salir, limit_btn_salir):
                # DETENER EL JUEGO POR COMPLETO --------------------------------
                juego_activo = False
                # PONER EL CLICKEO EN FALSO ----------------------------------------
                clicked = False
                
            elif detectar_click(mouse_pos, pos_btn_puntos, limit_btn_puntos):
                pantalla['menu'] = False
                pantalla['puntos'] = True
                clicked = False
                # EVENTOS SI SE CLICKEA EN ALGUNA OTRA PARTE ------------------------
            else:
                # PONER EL CLICKEO EN FALSO ----------------------------------------
                clicked = False
    elif pantalla['puntos']:
        if clicked:
            if detectar_click(mouse_pos, pos_btn_puntos, limit_btn_puntos):
                pantalla['menu'] = True
                pantalla['puntos'] = False
                clicked = False
            else:
                clicked = False
        # CORRIENDO LA PANTALLA DE JUEGO ---------------------------------------------
    elif pantalla['juego']:
        # MOVIMIENTO CONSTANTE DEL TANKE ----------------------------------------------
        definir_velocidad_jugador(player, f_velocidad)
        mover_personaje(player)
        definir_limite(player)
        restringir_movimiento(player, pantalla['tamanio'])
        
        # AUMENTO DE ENEMIGOS -------------------------------------------------------
        cantidad_enemigos = aumentar_enemigos(player['puntaje'])
        
        # APARICION Y REGENARACION DE ENEMIGOS ----------------------------------
        completar_lista_enemigos(l_enemigos, player['puntaje'], cantidad_enemigos)
        regerar_enemigos(l_enemigos, player['puntaje'])
        posicionar_enemigos(pantalla['tamanio'], l_enemigos, player)
        
        # MOVIMIENTO DE ENEMIGOS ---------------------------------------------------
        for enemigo in l_enemigos:
            if enemigo['timeWait'] > fps * 3:
                direccionar_enemigos(enemigo, player, pantalla['tamanio'])
                mover_personaje(enemigo)
                definir_limite(enemigo)
                enemigo['spawn'] = True
            else:
                enemigo['timeWait'] += 1
        
        # DISPARO DE LAS BALAS -----------------------------------------------------
        posicionar_bala(l_balas_1, player)
        
        # MOVIMIENTO DE LAS BALAS ---------------------------------------------------
        mover_balas(l_balas_1)
        definir_limite_bala(l_balas_1)
        seleccionar_img_balas(l_balas_1, c_img.bala_1_imgs)
        restringir_balas(l_balas_1, pantalla['tamanio'])
        if detectar_colision(l_balas_1, l_enemigos, player):
            disparo_enemigo_sound.play()
        
        # MOVIMIENTO DE LAS BALAS NIVEL 2 -----------------------------------------
        if len(l_balas_2) > 0:
            posicionar_bala(l_balas_2, player)
            mover_balas(l_balas_2)
            definir_limite_bala(l_balas_2)
            restringir_balas(l_balas_2, pantalla['tamanio'])
            if detectar_colision(l_balas_2, l_enemigos, player):
                disparo_enemigo_sound.play()
            quitar_bala(l_balas_2)
        
        # COLISION DE LOS ENEMIGOS ---------------------------------------------
        if colision_enemigo(l_enemigos, player):
            if sound_music_encontrada:
                colision_sound.play()
        
        # POWER UPS ----------------------------------------------------------------
        # RECUPERAR VIDA ----------------------------------------------------------------
        if player['puntaje'] % 10 == 0 and player['puntaje'] > 0:
            if aparecer_vida == False:
                if sound_music_encontrada:
                    aparicion_powers_sound.play()
                one_up = d_main.mas_vida.copy()
                one_up['posicion'] = posicion_power_up(pantalla['tamanio'])
                limite_power_up(one_up)
                aparecer_vida = True
        if aparecer_vida:
            if colision_power_up(one_up, player):
                if sound_music_encontrada:
                    colision_powr_sound.play()
                aumentar_vida(player, one_up)
                player['puntaje'] += 1
                aparecer_vida = False
        
        # GENERAR EL ITEM QUE GENERA LAS BALAS DE NIVEL 2 ------------------------------------------------------
        if player['puntaje'] % 5 == 0 and player['puntaje'] > 0:
            if f_bala2 == False:
                if sound_music_encontrada:
                    aparicion_powers_sound.play()
                f_bala2 = True
                item_balas2 = d_main.item_bala2.copy()
                item_balas2['posicion'] = posicion_power_up(pantalla['tamanio'])
                limite_power_up(item_balas2)
        if f_bala2:
            if colision_power_up(item_balas2, player):
                if sound_music_encontrada:
                    colision_powr_sound.play()
                llenar_lista_balas(l_balas_2, c_balas_2)
                player['puntaje'] += 1
                f_bala2 = False
        
        # VERIFICAR QUE EL JUGADOR ESTE VIVO --------------------------------
        if player['vida'] <= 0:
            pantalla['game_over'] = True
            pantalla['juego'] = False
            if sound_music_encontrada:
                pg.mixer.music.stop()
                try:
                    pg.mixer.music.load(os.path.join(dir_actual,"sounds\game_over\organ-bossa-30-seconds-4644.mp3"))
                    pg.mixer.music.play(loops=-1)
                except:
                    sound_music_encontrada = False
                game_over_sound.play()
            
            if archivo_abierto:
                if acomodar_puntajes(l_puntaje, player['puntaje']):
                    reescribir_puntaje(l_puntaje)
        
        # PANTALLA DE GAME OVER --------------------------------
    elif pantalla['game_over']:
        # EVENTOS SI SE CLICKEA EN LA PANTALLA DE GAME OVER ---------------
        if clicked:
            # EVENTOS SI SE CLICKEA EN 'MENU' ------------------------------
            if detectar_click(mouse_pos, pos_btn_menu, limit_btn_menu):
                pantalla['game_over'] = False
                pantalla['menu'] = True
                clicked = False
                if sound_music_encontrada:
                    pg.mixer.music.stop()
                    try:
                        pg.mixer.music.load(os.path.join(dir_actual,"sounds\_menu\loop-menu-preview-109594.mp3"))
                        pg.mixer.music.play(loops=-1)
                    except:
                        sound_music_encontrada = False
                    click_boton_menu_sound.play()
                # EVENTOS SI SE CLICKEA EN SALIR ----------------------------
            elif detectar_click(mouse_pos, pos_btn_salir, limit_btn_salir):
                juego_activo = False
            else:
                clicked = False
    
    # DIBUJANDO LA PANTALLA -------------------------------------------
    screen.fill((0,0,0))
    
    # IMPLEMENTAR IMAGENES EN LA PANTALLA DE INICIO ----------------------------
    if pantalla['menu']:
        screen.blit(c_img.pantalla_imgs['inicio'], (0,0))
        screen.blit(c_img.botones_imgs['jugar'], pos_btn_jugar)
        screen.blit(c_img.botones_imgs['salir'], pos_btn_salir)
        screen.blit(c_img.botones_imgs['puntos'], pos_btn_puntos)
        if archivo_abierto:
            t_max_puntos = f_sans_serif.render(f"MAX PUNTOS: {l_puntaje[0]}", True, (255,255,255))
        screen.blit(t_max_puntos, (490,620))
        
        # IMPLEMENTANDO IMAGENES EN LA PNTALLA DE TUORIAL ----------------------
    elif pantalla['tutorial']:
        screen.blit(c_img.pantalla_imgs['tutorial'], (0,0))
        texto_segundos = f_sans_serif.render(f"{segundos_transcurridos}", True, (0,0,0))
        screen.blit(texto_segundos, (0,10))
        if time_tutorial > (fps * 3):
            pantalla['tutorial'] = False
            pantalla['juego'] = True
            if sound_music_encontrada:
                try:
                    pg.mixer.music.load(os.path.join(dir_actual,"sounds\_juego\simple-piano-melody-9834.mp3"))
                    pg.mixer.music.set_volume(.4)
                    pg.mixer.music.play(loops=-1)
                except:
                    sound_music_encontrada = False
        else:
            if time_tutorial % fps == 0:
                segundos_transcurridos -= 1
            time_tutorial += 1
    elif pantalla['puntos']:
        screen.blit(c_img.pantalla_imgs['juego'], (0,0))
        puntos_orden = 0
        text_superior_puntaje = f_sans_serif.render(f"MEJORES PUNTAJES", True, (255,255,255))
        screen.blit(text_superior_puntaje, (450,0))
        borde_pantalla = 50
        for puntos in l_puntaje:
            puntos_orden += 1
            borde_pantalla += 50
            texto_puntajes = f_sans_serif.render(f"{puntos_orden}: {puntos}", True, (255,255,255))
            screen.blit(texto_puntajes, (600,borde_pantalla))
        screen.blit(c_img.botones_imgs['atras'], pos_btn_puntos)
        
        # IMPLEMENTANDO IMAGENES A LA PANTALLA DE JUEGO -------------------
    elif pantalla['juego']:
        # SUELO PRINCIPAL ------------------------------
        screen.blit(c_img.pantalla_imgs['juego'], (0,0))
        
        # COLOCANDO LOS ENEMIGOS -------------------------------------
        for enemigo in l_enemigos:
            if enemigo['vida'] > 0:
                if enemigo['timeWait'] % (fps/2) == 0 and enemigo['spawn'] == False:
                    # VACIO PARA TITILEO EN LA IMAGEN DE ADVERTENCIA --------------
                    pass
                elif enemigo['nivel'] == 1:
                    screen.blit(c_img.enemigo_1_imgs[enemigo['direccion']], enemigo['posicion'])
                elif enemigo['nivel'] == 2:
                    screen.blit(c_img.enemigo_2_imgs[enemigo['direccion']], enemigo['posicion'])
                elif enemigo['nivel'] == 3:
                    screen.blit(c_img.enemigo_3_imgs[enemigo['direccion']], enemigo['posicion'])
                elif enemigo['nivel'] == 4:
                    screen.blit(c_img.enemigo_4_imgs[enemigo['direccion']], enemigo['posicion'])
                else:
                    if enemigo['direccion'] == 'none_down':
                        screen.blit(c_img.enemigo_5_imgs[enemigo['direccion']], (enemigo['posicion'][0], 50))
                    elif enemigo['direccion'] == 'none_up':
                        screen.blit(c_img.enemigo_5_imgs[enemigo['direccion']], (enemigo['posicion'][0], pantalla['tamanio'][1] - enemigo['tamanio'][1]))
                    else:
                        screen.blit(c_img.enemigo_5_imgs[enemigo['direccion']], enemigo['posicion'])
        # LAS MUNICIONES --------------------------------
        # BALA NIVEL 1 ----------------------------------
        for bala in l_balas_1:
            if bala['accion']:
                screen.blit(bala['img'], bala['posicion'])
        
        # BALA 2 ---------------------------------------
        for bala in l_balas_2:
            if bala['accion'] and bala['direccion'] != 'none':
                screen.blit(c_img.bala_2_imgs[bala['direccion']], bala['posicion'])
        
        # DIBUJAR VIDA EXTRA ----------------------------------------------------------------
        if aparecer_vida:
            screen.blit(c_img.vida_up_1, one_up['posicion'])
        
        # DIBUJAR ITEM DE BALAS 2 ------------------------------------
        if f_bala2:
            screen.blit(c_img.bala_item_2, item_balas2['posicion'])
        
        # JUGADOR PRINCIPAL ----------------------------------------------------------------
        screen.blit(c_img.tank_imgs[player['direccion']], player['posicion'])
        
        # BARRA DONDE PONER DATOS ------------------------------------------------------------
        screen.blit(c_img.pantalla_imgs['barra'], (0,0))
        
        # BARRA DE VIDA ------------------------------------------------
        text_vida = f_sans_serif.render(f"VIDA:", True, (0,0,0))
        screen.blit(text_vida, (10,10))
        if player['vida'] == 5:
            img_barra_vida = c_img.vida_imgs['llena']
        elif player['vida'] == 4:
            img_barra_vida = c_img.vida_imgs['semi_llena']
        elif player['vida'] == 3:
            img_barra_vida = c_img.vida_imgs['mitad']
        elif player['vida'] == 2:
            img_barra_vida = c_img.vida_imgs['semi_baja']
        elif player['vida'] == 1:
            img_barra_vida = c_img.vida_imgs['baja']
        else:
            img_barra_vida = c_img.vida_imgs['vacia']
        screen.blit(img_barra_vida, (100,0))
        
        # BARRA BALAS 1--------------------------------
        text_balas_1 = f_sans_serif.render(f"BALAS Z:", True, (0,0,0))
        screen.blit(text_balas_1, (330,10))
        balas_usadas = 0
        for bala in l_balas_1:
            if bala['accion']:
                balas_usadas += 1
        if balas_usadas == 0:
            img_barra_balas1 = c_img.barra_bala1_img['llena']
        elif balas_usadas == 1:
            img_barra_balas1 = c_img.barra_bala1_img['semillena']
        elif balas_usadas == 2:
            img_barra_balas1 = c_img.barra_bala1_img['semibaja']
        elif balas_usadas == 3:
            img_barra_balas1 = c_img.barra_bala1_img['baja']
        else:
            img_barra_balas1 = c_img.barra_bala1_img['vacia']
        screen.blit(img_barra_balas1, (480,0))
        
        # BARRA BALAS 2 --------------------------------
        text_balas_2 = f_sans_serif.render(f"BALAS X:", True, (0,0,0))
        screen.blit(text_balas_2, (700,10))
        if len(l_balas_2) == 3:
            img_barra_balas2 = c_img.barra_bala2_img['llena']
        elif len(l_balas_2) == 2:
            img_barra_balas2 = c_img.barra_bala2_img['mitad']
        elif len(l_balas_2) == 1:
            img_barra_balas2 = c_img.barra_bala2_img['baja']
        else:
            img_barra_balas2 = c_img.barra_bala2_img['vacia']
        screen.blit(img_barra_balas2, (850,0))
        
        
        # PUNTAJE ----------------------------------------------------------------
        puntos_texto = f_sans_serif.render(f"PUNTOS: {player['puntaje']}", True, (0,0,0))
        screen.blit(puntos_texto, (1050,10))
        # PANTALLA DE GAME OVER ----------------------------------------------------------------
    elif pantalla['game_over']:
        screen.blit(c_img.pantalla_imgs['gameOver'], (0,0))
        screen.blit(c_img.botones_imgs['menu'], pos_btn_menu)
        screen.blit(c_img.botones_imgs['salir'], pos_btn_salir)
        screen.blit(puntos_texto, (550, 600))
    
    pg.display.flip()

pg.quit()