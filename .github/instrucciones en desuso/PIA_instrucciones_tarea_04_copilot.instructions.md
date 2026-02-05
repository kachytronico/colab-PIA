---
applyTo: '**'
---
Provide project context and coding guidelines that AI should follow when generating code, answering questions, or reviewing changes.

# Instrucciones del repositorio — PIA04 (UD4)

## Fuente de verdad
- docs/PIA04_Guia_Operativa_optima_v2.md
- docs/PIA_04_tarea_enunciado.md

## Reglas NO negociables
- Los títulos de secciones/celdas Markdown deben ser EXACTAMENTE los del PDF (literal).
- Prohibido data leakage: cualquier fit (imputer/scaler/PCA/encoder) SOLO en train; luego transform en valid/test.
- Problema 2: valid/test solo con etiquetas reales (nunca pseudo-labels).
- Problema 1: entrenar y optimizar 4 modelos: KNN(GridSearch), DT(RandomSearch + explicar 2 veces), SVM(GridSearch), NL(RandomSearch).
- Ensembles P1: (1) media con fiabilidad >80%, (2) criterio con Regresión Lineal (no logística).
- Solo sklearn y librerías permitidas (nada de TF/Keras/PyTorch).

## Cómo responder
- Siempre proponer estructura por secciones del PDF y checklist final.
- Si falta una decisión (por ejemplo NL), ofrecer 2 opciones sklearn y pedir que el usuario elija una o justificar la elegida.

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