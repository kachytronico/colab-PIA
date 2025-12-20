# Teoría breve (UD3): Q-learning aplicada al juego

## 1) Qué hace Q-learning en este juego
- Tengo un tablero 20x20: cada casilla es un **estado**.
- El agente elige una **acción** (moverse).
- El juego devuelve una **recompensa** (en el código es `delta_score`).
- Con eso actualizo una tabla llamada **Q-table** para aprender qué acciones son mejores.

## 2) Q-table (tabla Q)
- La Q-table guarda valores Q(s, a): “qué buena es la acción `a` en el estado `s`”.
- Filas = estados (20x20 = 400).
- Columnas = acciones posibles.

### Importante para la tarea (8-vecindad)
- Antes había 4 acciones: arriba/abajo/izq/der → Q-table (400, 4).
- Con 8-vecindad hay 8 acciones (incluye diagonales) → Q-table (400, 8).
- Lo cambio porque necesito guardar un valor Q para **cada una** de las 8 acciones.

## 3) Exploración vs Explotación (lo básico)
- **Explorar**: moverme “al azar” para descubrir caminos.
- **Explotar**: usar lo aprendido y elegir la mejor acción según la Q-table.

En el código, uso una exploración que baja con los episodios:
- `exploration_threshold = 1 - (iteration / max_iterations)`
- Si `max_iterations` es pequeño, la exploración baja más rápido y el agente empieza a explotar antes.

## 4) Hiperparámetros que toco (los más importantes)
- `learning_rate` (α): “velocidad” a la que aprendo.
  - Más alto → aprende más rápido (pero puede ser más inestable).
- `discount_factor` (γ): cuánto me importa el futuro.
  - Alto (0.9–0.95) suele ayudar a buscar la meta final.
- `max_iterations`: número de episodios de entrenamiento.
  - Menos episodios → entreno antes (y con la fórmula de exploración, exploto antes).

## 5) Optimización (en versión simple, tocando pocos parámetros)
Para el apartado de optimización, hago cambios mínimos:

- Reduzco `max_iterations` (por ejemplo a 150).
  - Como la exploración depende de `max_iterations`, esto hace que el agente deje de explorar “tanto tiempo” y empiece a explotar antes.
- Subo `learning_rate` (por ejemplo de 0.1/0.2 a 0.4).
  - Así doy más peso a la nueva información y aprendo más rápido.
- Mantengo `discount_factor` alto (0.9 o 0.95).
  - Quiero que el agente valore llegar a la salida (objetivo final), no solo moverse sin rumbo.

## 6) Política diferente (momentum / inercia)
La política actual es “epsilon-greedy” (a veces exploro, a veces exploto).
Para cambiarla de forma simple:
- Guardo la acción anterior (`prev_action`).
- Con cierta probabilidad intento repetir la acción anterior si es posible.
Esto ya es un elemento diferenciador en la política (no es exactamente la misma forma de elegir acciones).
