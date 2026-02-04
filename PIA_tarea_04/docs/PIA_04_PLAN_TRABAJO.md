# PLAN DE TRABAJO - Tarea 4 PIA

Iremos completando estos hitos secuencialmente. No avanzar al siguiente sin validar el anterior.

## FASE A: PROBLEMA 1 (TESLA - SUPERVISADO)
- [ ] **Hito 1: Carga y Configuración.**
  - Crear notebook.
  - Importar librerías.
  - Cargar `sistema_de_arranque.csv` desde GitHub Raw.
  - Verificar carga (`head`, `info`).

- [ ] **Hito 2: EDA y Limpieza P1.**
  - Estadísticos básicos (`describe`).
  - Matriz de correlación (`heatmap`).
  - Visualización de la variable objetivo.
  - Limpieza de nulos y tratamiento básico de outliers si existen.

- [ ] **Hito 3: Preprocesamiento P1.**
  - Separación (`train_test_split`).
  - Encoding de variables categóricas (`OneHot` o `LabelEncoder`).
  - Escalado (`StandardScaler`).
  - (Opcional) PCA si hay muchas dimensiones.

- [ ] **Hito 4: Modelado P1.**
  - Entrenar Modelo A (ej. KNN) con GridSearch.
  - Entrenar Modelo B (ej. Árbol Decisión).
  - Entrenar Modelo C (ej. SVM).
  - Comparar métricas (Accuracy/F1).

- [ ] **Hito 5: Ensemble P1.**
  - Crear un `VotingClassifier` con los modelos anteriores.
  - Explicación del resultado.

## FASE B: PROBLEMA 2 (FALLOS - SEMISUPERVISADO)
- [ ] **Hito 6: Carga y Análisis P2.**
  - Cargar `fallos_producto.csv` desde GitHub Raw.
  - Identificar la columna target con valores no etiquetados (suelen ser `-1` o `NaN`).

- [ ] **Hito 7: Etiquetado Automático (Label Spreading).**
  - Preparar los datos (Encoding/Escalado igual que en P1).
  - Aplicar `LabelSpreading` o `LabelPropagation` para deducir las etiquetas faltantes.
  - Verificar cuántas etiquetas se han recuperado.

- [ ] **Hito 8: Modelo Final P2.**
  - Entrenar un clasificador final (ej. RandomForest) usando el dataset completo ya etiquetado.
  - Conclusiones finales.