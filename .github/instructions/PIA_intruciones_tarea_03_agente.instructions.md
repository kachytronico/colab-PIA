---
description: "PIA03 Problema 2 - Cambios mínimos (nivel básico)"
applyTo: "**/*.py"
---

# Objetivo (PIA03 - Problema 2)
Parto del ejemplo “Exámenes finales, el videojuego” y hago SOLO los cambios mínimos para cumplir:

- Optimización: entrenar en menos episodios (tocando pocos hiperparámetros).
- 8-vecindad: 8 movimientos posibles (incluye diagonales).
- Portal: una casilla teletransporta a otra NO adyacente.
- Política diferente: cambio simple en cómo elijo la acción (momentum).

# Reglas de trabajo (nivel básico)
- NO refactorices el programa entero.
- NO crees clases nuevas.
- NO añadas librerías nuevas.
- Cambios pequeños y claros, con 1 comentario corto por cambio importante.

# Comentarios en el código
- Comentarios cortos, en español y en primera persona.
- Ejemplos:
  - "Aquí subo el learning_rate para que aprenda más rápido."
  - "Aquí permito diagonales (8-vecindad)."
  - "Si piso el portal, me teletransporto."

# Texto para capturas (entrega)
Después de cada paso, genera un bloque llamado “Texto para la captura” con:
- 1 título corto
- 2–3 frases en primera persona (qué hice y por qué)
- 1 frase de cómo lo comprobé (por ejemplo: logs de consola o una ejecución)
