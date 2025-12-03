import pygame
import os

# Inicia el juego
pygame.init()

# Establece la configuración inicial del juego
width, height = 1200, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Exams")
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
}

game_info = {
    "player": [19, 15], # esto es lista en vez de tupla porque lo voy a modificar
    "steps": [] # aquí guardaré las casillas visitadas para marcarlas con un punto rojo
}

# Carga las imágenes y crea un diccionario {nombre: imagen}
image_files = [f for f in os.listdir("img") if f.endswith(".png")]
images = {file.replace(".png", ""): pygame.image.load("img/" + file).convert() for file in image_files}

# Define un mapeo entre una posición y la imagen correspondiente
def idx2img(x, y, map = map_idx, images = images):
    for idx, pos in map.items():
        if (x, y) in pos:
            return images[idx].copy()

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
    pos_y, pos_x = player_pos
    
    # taller
    if pos_x < 3 and pos_y < 6:
        message = "¿Dónde es el examen? 20 personas te responden a la vez. No te aclaras para nada, pierdes 120 segundos."
        SCORE -= 120
    
    # emprendimiento
    elif pos_x == 4 and pos_y < 6:
        message = "Una mesa al final con algún dulce. Como nadie te mira, lo degustas con deseo. Pierdes 220 segundos."
        SCORE -= 220
    
    # profesores
    elif pos_x < 10 and pos_y < 6:
        message = "¿Dónde es el examen? 20 personas te responden a la vez. No te aclaras para nada, pierdes 120 segundos."
        SCORE -= 120
    
    # salon de actos
    elif pos_y < 6:
        message = "Una habitación enorme, pero seguro que aquí no es el examen. Pierdes 10 segundos."
        SCORE -= 10
    
    # baño
    elif pos_x < 1 and pos_y < 14:
        message = "Se te había olvidado, mejor ir vacío. Pierdes 120 segundos."
        SCORE -= 120

    # escaleras
    elif (pos_x == 10 and pos_y == 7) or (pos_x == 10 and pos_y == 8):
        message = "No vuelas como superman. Pierdes 15 segundos."
        SCORE -= 15
    
    # Aula 1
    elif pos_x < 5 and pos_y > 14:
        message = "No, esta no es. Pierdes 30 segundos."
        SCORE -= 30
    
    # Aula 2:
    elif pos_x < 10 and pos_y > 14:
        message = "Estás cerca, los nervios te ralentizan. ¿Dónde es tu sitio?"
        SCORE -= 3
    
    # secretaría
    elif pos_x == 11 and pos_y > 13:
        message = "Tres personas te miran con curiosidad. Pierdes 40 segundos."
        SCORE -= 40
    
    # dirección
    elif pos_x == 13 and pos_y > 15:
        message = "Has entrado en el despacho del director. Por suerte (para ti) no habla mucho, pierdes 10 segundos."
        SCORE -= 10
    
    # dirección empleo
    elif pos_x > 17 and pos_y > 15:
        message = "Ya estabas nervioso, ahora lo estás más. Reduce tu tiempo a la mitad."
        SCORE /= 2

    # otro sitio
    else:
        message = f"Tic tac. Te quedan {SCORE} segundos."
        SCORE -= 1
    
    return message


# Escala las imagénes para que quepan en la cuadrícula de la pantalla
map = [ # Matriz comprimida
    [pygame.transform.scale(idx2img(row, col), (cell_width, cell_height))
    for col in range(grid_size)]
for row in range(grid_size)]
stepped_background_img = pygame.transform.scale(images["stepped_background"], (cell_width, cell_height))
player_img = pygame.transform.scale(images["player"], (cell_width, cell_height))

# Variables generales
RUNNING = True # bucle principal del juego
SHOW_COORDINATES = False # define si mostrar o no las coordenadas de cada casilla
score_text = "" # problemas con null en VERBOSE
VERBOSE = True # define si mostrar o no mensajes al jugador
SCORE = 600 # puntuación inicial
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        
        ## ESTA ES LA LÓGICA DEL AGENTE HUMANO ##
        if event.type == pygame.KEYDOWN:
            player_pos = game_info["player"]
            match event.key:
                case pygame.K_UP:
                    if player_pos[0] != 0 and (player_pos[0] - 1, player_pos[1]) not in [*map_idx["wall"], *map_idx["up_stairs"]]:
                        player_pos[0] -= 1
                case pygame.K_DOWN:
                    if player_pos[0] != grid_size - 1 and (player_pos[0] + 1, player_pos[1]) not in [*map_idx["wall"], *map_idx["down_stairs"]]:
                        player_pos[0] += 1
                case pygame.K_LEFT:
                    if player_pos[1] != 0 and (player_pos[0], player_pos[1] - 1) not in [*map_idx["wall"], *map_idx["down_stairs"]]:
                        player_pos[1] -= 1
                case pygame.K_RIGHT:
                    if player_pos[1] != grid_size - 1 and (player_pos[0], player_pos[1] + 1) not in [*map_idx["wall"], *map_idx["up_stairs"]]:
                        player_pos[1] += 1
        
            score_text = update_score(player_pos)
        
            if tuple(player_pos) in map_idx["exit"]:
                print(f"Juego terminado exitosamente. Puntuación {SCORE}.")
                RUNNING = False
        
        ## AQUÍ ACABA LA LÓGICA DEL AGENTE HUMANO ##

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

# Sale del juego
pygame.quit()