# GUÍA DE ESTILO - PIA Tarea 04

## ESTRUCTURA OBLIGATORIA DEL NOTEBOOK
1. **Celda 0: Setup Examen (Clonado)**
   - Comprobar si la carpeta del repo existe.
   - Si no, ejecutar `!git clone https://github.com/kachytronico/colab-PIA.git`.
   - Verificar rutas de los CSV con `!find . -name "*.csv"`.
2. **Imports y Configuración Gráfica**
   - Estilo `seaborn` definido.
3. **Problema 1: Tesla**
   - 3.1 Carga (usando ruta relativa local).
   - 3.2 AED.
   - 3.3 Preprocesamiento (Pipeline: Limpieza -> Encoding -> Escalado).
   - 3.4 Modelado (GridSearch).
   - 3.5 Ensemble.
4. **Problema 2: Fallos**
   - 4.1 Carga y Análisis de nulos.
   - 4.2 Etiquetado Automático (LabelPropagation).
   - 4.3 Clasificación final.

## REGLAS DE CÓDIGO
- **Rutas:** Nunca usar rutas absolutas de tu ordenador (ej: `C:/Users...`). Usar rutas relativas al entorno de Colab (`/content/...`).
- **Variables:** `df_tesla`, `df_fallos`, `X_train`, `y_test`.
- **Gráficos:** Todos deben tener `plt.title()`, etiquetas en ejes y leyenda si aplica.
- **Manejo de Errores:**
   - Usar bloques `try-except` para la carga de datos. Si falla, imprimir un mensaje claro: "⚠️ No se encuentra el dataset en la ruta X".

## SNIPPET DE CARGA (ESTÁNDAR)
```python
import os
import pandas as pd

REPO_DIR = "colab-PIA" # o el nombre de la carpeta generada
csv_path = os.path.join(REPO_DIR, "PIA_UD04", "nombre_archivo.csv")

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    print(f"✅ Cargado: {csv_path}")
else:
    print(f"❌ Error: No encontrado en {csv_path}. Revisa el clonado.")