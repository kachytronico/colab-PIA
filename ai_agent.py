# pylint: disable=no-member
import pygame
import os
import numpy as np
import random
import time

# Inicia el juego
pygame.init()

# Establece la configuración inicial del juego
width, height = 800, 600 # 1200, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Exámenes finales, el videojuego")
small = pygame.font.Font(None, 12)
large = pygame.font.Font(None, 36)

# Establece los límites del mapa
grid_size = 20
cell_width = width // grid_size
cell_height = height // grid_size

# Establece el mapa del juego
map_idx = {
    "wall": [
        (0, 3), (0, 5), (0, 10),
        (1, 3), (1, 5), (1, 10),
        (2, 3), (2, 5), (2, 10),
        (3, 3), (3, 5), (3, 10),
        (4, 3), (4, 5), (4, 10),
        (5, 3), (5, 5), (5, 10),
        (6, 0), (6, 1), (6, 3), (6, 5), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 16), (6, 17), (6, 18), (6, 19), (6, 20),
        (7, 17), (7, 18), (7, 19),
        (8, 1), (8, 17), (8, 18), (8, 19),
        (9, 1), (9, 10),
        (10, 0), (10, 1), (10, 10), (10, 11), (10, 12), (10, 17), (10, 18),
        (11, 1), (11, 10), (11, 11), (11, 12), (11, 17), (11, 18),
        (12, 1), (12, 10), (12, 11), (12, 12), (12, 17), (12, 18),
        (13, 10), (13, 11), (13, 12), (13, 13),
        (14, 0), (14, 1), (14, 2), (14, 4), (14, 5), (14, 6), (14, 8), (14, 9), (14, 10),
        (15, 5), (15, 10), (15, 12), (15, 14), (15, 17), (15, 19), (15, 20),
        (16, 5), (16, 10), (16, 12), (16, 14), (16, 17),
        (17, 5), (17, 10), (17, 12), (17, 14), (17, 17),
        (18, 5), (18, 10), (18, 12), (18, 14), (18, 17),
        (19, 5), (19, 10), (19, 12), (19, 14), (19, 17),
    ],
    "horizontal_door": [(6, 2), (6, 4), (6, 6), (6, 15), (14, 3), (14, 7), (15, 13), (15, 18)],
    "vertical_door": [(7, 1), (13, 1), (14, 12)],
    "up_stairs": [(7, 10)],
    "down_stairs": [(8, 10)],
    "exit": [(18, 8)]
    ,
    # Nuevos elementos del mapa para complicar la llegada al `exit`.
    # He añadido:`trap` casillas con gran penalización, `mud` zonas lentas
    # y `bonus` con recompensa pequeña. No borro nada, solo añado claves.
    "trap": [(2, 8), (3, 9), (4, 9), (9, 7), (10, 5)],
    "mud": [(12, 9), (13, 9)],
    "bonus": [(5, 15)]
}

# Portal: uso una casilla visible como ENTRADA y defino la salida
# Aquí uso `up_stairs` como entrada del portal (PORTAL_IN) y elijo
# una salida no adyacente y que no sea muro (PORTAL_OUT).
PORTAL_IN = map_idx["up_stairs"][0]
# Valor original de salida (lo conservo comentado como referencia):
# PORTAL_OUT = (2, 16)  # Aquí defino la salida; no adyacente y no muro.
# He movido la salida del portal más cerca de la casilla `exit` para que
# el uso del portal sea más visible al agente cuando aprende.
PORTAL_OUT = (16, 8)  # Nueva salida: cerca de `exit` (18, 8), no adyacente y no muro.


# Carga las imágenes y crea un diccionario {nombre: imagen}
image_files = [f for f in os.listdir("img") if f.endswith(".png")]
images = {file.replace(".png", ""): pygame.image.load("img/" + file).convert() for file in image_files}

# Texto para la captura
# Título: Nuevos obstáculos
# Hice: Añadí `trap` en (2, 8), (3, 9), (4, 9), (9, 7), (10, 5); `mud` en (12, 9), (13, 9);
# Hice: También añadí `bonus` en (5, 15) y asigné penalizaciones/recompensas en `update_score`.
# Comprobé: Al ejecutar el juego confirmé los mensajes y penalizaciones cuando piso (2, 8).

# Define un mapeo entre una posición y la imagen correspondiente
def idx2img(x, y, map = map_idx, images = images):
    for idx, pos in map.items():
        if (x, y) in pos:
            # Si el tipo de casilla no tiene imagen asociada, uso 'wall'
            # como fallback para destacar el elemento sin añadir imágenes.
            if idx in images:
                return images[idx].copy()
            else:
                return images.get("wall", images["background"]).copy()

    return images["background"].copy()

# Define el identificador de las casillas
def create_text(message, x, y, font = small):
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    return text, text_rect

# Define la forma de modificar la puntuación
def update_score(player_pos):
    global SCORE
    delta_score = 0
    pos_y, pos_x = player_pos
    
    # choca contra un muro
    if tuple(player_pos) in map_idx["wall"]:
        message = "Boom. ¡Qué bonitas estrellas!"
        delta_score = -np.inf
    
    elif pos_x < 0 or pos_y < 0 or pos_x >= grid_size or pos_y >= grid_size:
        message = "¿A dónde vas?"
        delta_score = -np.inf
    
    elif tuple(player_pos) in map_idx["exit"]:
        message = "¡Has llegado a tiempo!"
        delta_score = 1000000

    # Nuevos elementos: `trap`, `mud`, `bonus`.
    # He añadido estas comprobaciones para aplicar recompensas/penalizaciones
    # a las nuevas casillas sin refactorizar el resto de la función.
    elif tuple(player_pos) in map_idx.get("trap", []):
        message = "Has caído en una trampa. Pierdes 300 segundos."
        delta_score = -300

    elif tuple(player_pos) in map_idx.get("mud", []):
        message = "Zona de barro: te ralentizas y pierdes tiempo."
        delta_score = -20

    elif tuple(player_pos) in map_idx.get("bonus", []):
        message = "Encuentras una ayuda: avanzas más rápido. Ganas 50 segundos."
        delta_score = 50

    # taller
    elif pos_x < 3 and pos_y < 6:
        message = "¿Dónde es el examen? 20 personas te responden a la vez. No te aclaras para nada, pierdes 120 segundos."
        delta_score = -120
    
    # emprendimiento
    elif pos_x == 4 and pos_y < 6:
        message = "Una mesa al final con algún dulce. Como nadie te mira, lo degustas con deseo. Pierdes 220 segundos."
        delta_score = -220
    
    # profesores
    elif pos_x < 10 and pos_y < 6:
        message = "¿Dónde es el examen? 20 personas te responden a la vez. No te aclaras para nada, pierdes 120 segundos."
        delta_score = -120
    
    # salon de actos
    elif pos_y < 6:
        message = "Una habitación enorme, pero seguro que aquí no es el examen. Pierdes 10 segundos."
        delta_score = -10
    
    # baño
    elif pos_x < 1 and pos_y < 14:
        message = "Se te había olvidado, mejor ir vacío. Pierdes 120 segundos."
        delta_score = -120

    # escaleras
    elif (pos_x == 10 and pos_y == 7) or (pos_x == 10 and pos_y == 8):
        message = "No vuelas como superman. Pierdes 15 segundos."
        delta_score = -15
    
    # Aula 1
    elif pos_x < 5 and pos_y > 14:
        message = "No, esta no es. Pierdes 30 segundos."
        delta_score = -30
    
    # Aula 2:
    elif pos_x < 10 and pos_y > 14:
        message = "Estás cerca, los nervios te ralentizan. ¿Dónde es tu sitio?"
        delta_score = -3
    
    # secretaría
    elif pos_x == 11 and pos_y > 13:
        message = "Tres personas te miran con curiosidad. Pierdes 40 segundos."
        delta_score = -40
    
    # dirección
    elif pos_x == 13 and pos_y > 15:
        message = "Has entrado en el despacho del director. Por suerte (para ti) no habla mucho, pierdes 10 segundos."
        delta_score = -10
    
    # dirección empleo
    elif pos_x > 17 and pos_y > 15:
        message = "Ya estabas nervioso, ahora lo estás más. Reduce tu tiempo a la mitad."
        delta_score = -SCORE // 2 - 60

    # otro sitio
    else:
        message = f"Tic tac. El tiempo sigue pasando."
        delta_score = -1
    
    if tuple(player_pos) in game_info["steps"]: # ir a casillas ya visitadas penaliza al jugador
        delta_score *= 20
    
    return message + f" Te quedan {SCORE + delta_score} segundos.", delta_score

# Escala las imagénes para que quepan en la cuadrícula de la pantalla
map = [ # Matriz comprimida
    [pygame.transform.scale(idx2img(row, col), (cell_width, cell_height))
    for col in range(grid_size)]
for row in range(grid_size)]
stepped_background_img = pygame.transform.scale(images["stepped_background"], (cell_width, cell_height))
player_img = pygame.transform.scale(images["player"], (cell_width, cell_height))

# Variables generales
SHOW_COORDINATES = False # define si mostrar o no las coordenadas de cada casilla
score_text = "" # problemas con null en VERBOSE
VERBOSE = False # define si mostrar o no mensajes al jugador
GAME_SPEED = 0 # velocidad del juego

# Variables iniciales del AGENTE
# OLD: q_table = np.zeros((grid_size * grid_size, 4), float) # cada casilla del mapa como fila, cada acción (dirección) como columna
# He cambiado la Q-table a 8 acciones para permitir movimiento diagonal (8-vecindad).
q_table = np.zeros((grid_size * grid_size, 8), float) # cada casilla del mapa como fila, cada acción (dirección) como columna

# 1. Ajusta los hiperparámetros para entrenar el agente en el menor número de episodios posibles.
# Aquí subo el learning_rate a 0.4 porque quiero que las q-values cambien más rápido.
learning_rate = 0.2 # este lo subo un poco para que aprenda más rápido
discount_factor = 0.9 # Este lo dejo igual o 0.95, está bien para ser previsor.

# Reduzco max_iterations a 150 para entrenar con menos episodios y ver convergencia rápida.
# Al hacerlo acepto que pueda necesitar ajustes finos en ALPHA/epsilon si oscila.
max_iterations = 400
for iteration in range(1, max_iterations + 1):
    game_info = {
        "player": [19, 15], # esto es lista en vez de tupla porque lo voy a modificar
        "steps": [] # aquí guardaré las casillas visitadas para marcarlas con un punto rojo
    }
    SCORE = 600 # puntuación inicial
    RUNNING = True # bucle principal del juego
    exploration_threshold = 1 - (iteration / max_iterations) # valor de exploración inicial
    # Política momentum: inicio del episodio, inicializo prev_action
    # Aquí inicializo `prev_action` a None para que la política pueda
    # repetir la acción previa con cierta probabilidad (momentum simple).
    prev_action = None

    if iteration == max_iterations:
        GAME_SPEED = 1
        VERBOSE = True

    # LOG
    print(f"Comenzando la iteración {iteration} de {max_iterations}.")

    while RUNNING:
        # evento de salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    VERBOSE = not VERBOSE
            
                if event.key == pygame.K_c:
                    SHOW_COORDINATES = not SHOW_COORDINATES
            
        ## ESTA ES LA LÓGICA DEL AGENTE AI ##
        player_pos = game_info["player"]

        # Paso 1. Establecer la acción a tomar
        state = q_table[player_pos[0] * grid_size + player_pos[1]]
        if VERBOSE: print(state)
        if random.random() < exploration_threshold:
            # OLD: for pos_action in range(4): # intentamos explorar todas las casillas, busca una nunca accedida
            # He ampliado la exploración a 8 acciones para incluir diagonales.
            for pos_action in range(8): # intentamos explorar todas las casillas, busca una nunca accedida
                if state[pos_action] == 0: # exploración
                    action = pos_action
                    break
            else:
                # OLD: action = random.randint(0, 3)
                # Cambio a randint(0,7) para elegir entre las 8 acciones.
                action = random.randint(0, 7)
                while state[action] == - np.inf:
                    # OLD: action = random.randint(0, 3)
                    action = random.randint(0, 7)
        else:
            # action = np.argmax(state) # explotación
            
            # Política momentum: con probabilidad 0.7 repito la acción previa
            # Yo intento repetir `prev_action` para dar continuidad al movimiento
            # si existe y no está penalizada (-np.inf). Si no, hago `argmax`.
            if prev_action is not None and random.random() < 0.7 and state[prev_action] != - np.inf:
                action = prev_action
            else:
                action = np.argmax(state) # explotación
 
        # Paso 2. Realizar la acción
        fixed_player_pos = player_pos.copy() # voy a necesitar la posición anterior
        match action: # dejamos de comprobar si el movimiento puede hacerse. Si se choca, pierde
            case 0:
                player_pos[0] -= 1
            case 1:
                player_pos[0] += 1
            case 2:
                player_pos[1] -= 1
            case 3:
                player_pos[1] += 1
            # Añado las diagonales para 8-vecindad. Las dejo comentadas antiguas y añado en primera persona.
            case 4:
                # He añadido la acción 4: diagonal NW (arriba-izquierda)
                player_pos[0] -= 1
                player_pos[1] -= 1
            case 5:
                # He añadido la acción 5: diagonal NE (arriba-derecha)
                player_pos[0] -= 1
                player_pos[1] += 1
            case 6:
                # He añadido la acción 6: diagonal SW (abajo-izquierda)
                player_pos[0] += 1
                player_pos[1] -= 1
            case 7:
                # He añadido la acción 7: diagonal SE (abajo-derecha)
                player_pos[0] += 1
                player_pos[1] += 1
        
        # Portal: si piso la casilla de entrada me teletransporto a PORTAL_OUT
        # Aquí compruebo la entrada del portal y la uso.
        if tuple(player_pos) == PORTAL_IN:
            # Si piso el portal, me teletransporto.
            player_pos[0], player_pos[1] = PORTAL_OUT
            print('Portal usado')

        # Paso 3. Recompensa
        score_text, delta_score = update_score(player_pos)

        # Parte 4. Actualizar la Q-TABLA
        prev_q_value = q_table[(fixed_player_pos[0] * grid_size + fixed_player_pos[1]), action]
        if player_pos[0] < 0 or player_pos[0] >= grid_size or player_pos[1] < 0 or player_pos[1] >= grid_size:
            optimistic_value = 0
        else:
            optimistic_value = np.max(q_table[player_pos[0] * grid_size + player_pos[1]])

        q_table[(fixed_player_pos[0] * grid_size + fixed_player_pos[1]), action] = (
            prev_q_value + learning_rate * (delta_score + discount_factor * optimistic_value - prev_q_value)
        )

        # Parte 5. Actualizar la puntuación
        SCORE += delta_score

        # Guardo la acción tomada para el siguiente paso (momentum)
        # Aquí guardo `prev_action` en primera persona para usarla en la
        # siguiente iteración si la política decide repetirla.
        prev_action = action

        ## AQUÍ ACABA LA LÓGICA DEL AGENTE AI ##

        time.sleep(GAME_SPEED)
        # Limpia la pantalla
        screen.fill((0, 0, 0))

        # Añade las imágenes a la cuadrícula
        for row in range(grid_size):
            for col in range(grid_size):
                x = col * cell_width
                y = row * cell_height

                if [row, col] == game_info["player"]:
                    if (row, col) not in game_info["steps"] and (row, col) not in map_idx["up_stairs"] and (row, col) not in map_idx["down_stairs"]:
                        game_info["steps"].append((row, col)) # actualiza los pasos
                    screen.blit(player_img, (x, y)) # muestra el jugador

                elif (row, col) in game_info["steps"]:
                    screen.blit(stepped_background_img, (x, y)) # muestra los pasos
                
                else:
                    screen.blit(map[row][col], (x, y)) # muestra el background

                if SHOW_COORDINATES:
                    text, text_rect = create_text(f"({row}, {col})", x + cell_width // 4, y + cell_height // 8)
                    screen.blit(text, text_rect)
        
        if VERBOSE and score_text: # mensajes para el jugador
            text, text_rect = create_text(score_text, width // 2, height // 15, large)
            screen.blit(text, text_rect)
                
        # Modifica la pantalla
        pygame.display.flip()

        # Control de final de partida
        if SCORE <= 0:
            print("Juego terminado. Derrota.")
            RUNNING = False

        if tuple(player_pos) in map_idx["exit"]:
            print(f"Iteración {iteration} terminada exitosamente. Puntuación {SCORE}.")
            time.sleep(0.1)
            RUNNING = False

# Sale del juego
pygame.quit()


