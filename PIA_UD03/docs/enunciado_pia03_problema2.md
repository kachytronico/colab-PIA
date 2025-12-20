# PIA 03 — Tarea 3 — Problema 2: La partida definitiva

Basándote en el ejemplo **“Exámenes finales, el videojuego”**, realiza las siguientes modificaciones:

- **Optimización**: ajusta los hiperparámetros para entrenar el agente en el **menor número de episodios posible**.
- **8-vecindad**: el agente debe poder moverse en **todas las direcciones** (8 casillas adyacentes).
- **Portal**: debe existir una casilla con una tubería/teletransportador/portal que permita mover el agente a una casilla **NO adyacente** del tablero.
- **Política diferente**: el agente debe adoptar una política distinta a la actual.  
  Ejemplo: política con **momentum (inercia)**: el agente intenta repetir la acción anterior siempre que sea posible.

## Rúbrica (Problema 2)

| Objeto de evaluación | Puntuación |
|---|---:|
| Optimización: modifica hiperparámetros para entrenar en el menor nº de episodios posible | 1 punto |
| 8-vecindad: movimiento a cualquiera de las 8 casillas adyacentes | 3 puntos |
| Portal: existe al menos una casilla que teletransporta al agente | 3 puntos |
| Política diferente: hay un elemento nuevo y diferenciador en la política del agente | 3 puntos |
| Opcional: nuevos elementos al mapa (+ recompensa si aplica) | 0.5 puntos extra |
