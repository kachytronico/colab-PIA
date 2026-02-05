# PLAN DE TRABAJO - Tarea 4 PIA (Modo Examen)

## FASE A: INFRAESTRUCTURA Y PROBLEMA 1
- [ ] **Hito 1: Setup de Examen.**
  - Clonar repositorio GitHub en Colab.
  - Localizar las rutas exactas de los CSV (`sistema_de_arranque.csv` y `fallos_producto.csv`).
  - Localizar rutas de cuadernos de ejemplo (para referencia nuestra).
  - Cargar Dataset P1 y mostrar `head()`.

- [ ] **Hito 2: AED y Limpieza P1.**
  - `.describe()`, histogramas de variables numéricas.
  - Matriz de correlación (`heatmap`).
  - Limpieza de atípicos/nulos (si los hay).

- [ ] **Hito 3: Preprocesamiento P1.**
  - Split `train_test_split`.
  - Encoding (`OneHot` o `Label`) y Escalado (`StandardScaler`).
  - *Check:* Ver shape de los datos transformados.

- [ ] **Hito 4: Modelado Supervisado P1.**
  - Entrenar KNN, Árbol y SVM (o similar).
  - Usar `GridSearchCV` para buscar hiperparámetros.
  - Mostrar métricas de cada uno.

- [ ] **Hito 5: Ensemble P1.**
  - Combinar los 3 modelos en un `VotingClassifier`.
  - Comparar métrica final vs modelos individuales.

## FASE B: PROBLEMA 2 (SEMISUPERVISADO)
- [ ] **Hito 6: Carga y Análisis de Etiquetas P2.**
  - Cargar `fallos_producto.csv`.
  - Identificar cuántos datos no tienen etiqueta (NaN o -1).

- [ ] **Hito 7: Propagación de Etiquetas.**
  - Usar `LabelSpreading` para imputar las clases faltantes.
  - Evaluar la distribución de las nuevas etiquetas.

- [ ] **Hito 8: Modelo Final P2 y Entrega.**
  - Entrenar modelo final con los datos "rellenados".
  - Generar conclusiones finales.
  - Revisar Checklist de Rúbrica.