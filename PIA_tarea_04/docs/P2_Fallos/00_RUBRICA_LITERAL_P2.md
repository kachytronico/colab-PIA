# Rúbrica literal P2 — Checklist (Problema 2: Fallos de producto)

> Dataset: `fallos_producto.csv`
>
> Hechos fijos (para evitar errores):
> - target: `failure`
> - unlabeled: `failure = NaN`
> - categóricas: `product_code`, `attribute_0`, `attribute_1`
> - `id` existe y se trata como identificador (no feature; eliminar y justificar)
> - umbral pseudo-etiquetado: `0.90` (>= 0.90)
>
> Líneas rojas globales (anti-leakage):
> - Valid/Test SOLO con etiquetas reales (nunca pseudo-etiquetas).
> - Fit de transformadores SOLO con train (train_labeled o train_aug, pero nunca con valid/test).
> - El test se usa UNA vez al final.

---

- [ ] 1. Realiza un AED sobre el conjunto de datos.
  Evidencia mínima: celda Markdown con el título y 1+ celdas de código que muestren una vista general del dataset y el flujo de AED.

- [ ] *  Estadísticos iniciales. 0.2 puntos  
  Evidencia mínima: salida de `describe()` (o equivalente) con estadísticos básicos visibles.

- [ ] *  Distribuciones de las variables numéricas del conjunto de datos. 0.3 puntos  
  Evidencia mínima: gráficos de distribución (histogramas/boxplots) con títulos y ejes.

- [ ] *  Matriz de correlación. 0.5 puntos  
  Evidencia mínima: heatmap o tabla de correlaciones con etiquetas legibles.

  Recomendación (para clavar el AED):
  - Separar y comentar `df_labeled` vs `df_unlabeled` (cuántos NaN hay en failure).
  - Confirmar columnas categóricas y numéricas.
  - Mostrar % de nulos por columna (top 10) y comentar plan de imputación.

---

- [ ] 2. Realiza el preprocesamiento de datos de tu problema.
  Evidencia mínima: celda Markdown con el título y 1+ celdas de código mostrando el plan de limpieza y transformaciones.
  Líneas rojas: no hacer `fit()` de transformadores con el dataset completo.

- [ ] *  Reserva un conjunto de datos para validación y otro para testeo. 0.5 puntos
  Evidencia mínima: separación train/valid/test con tamaños y porcentajes mostrados.
  Líneas rojas: valid/test solo con datos originalmente etiquetados; no usar pseudo-etiquetas.

- [ ] *  Columnas inútiles, valores sin sentido y atípicos. 1 punto
  Evidencia mínima: listado de columnas eliminadas o reglas aplicadas y justificación breve (hecho SOLO con train).
  Líneas rojas: no decidir filtros usando información de valid/test.

- [ ] *  Tratamiento de valores nulos. 0.5 puntos
  Evidencia mínima: porcentaje de nulos antes/después y método de imputación.
  Líneas rojas: imputadores ajustados solo con `X_train` y aplicados a valid/test.

- [ ] *  Análisis de variabilidad. 0.5 puntos
  Evidencia mínima: criterio de baja varianza (al menos en numéricas) y columnas eliminadas si aplica.
  Líneas rojas: el análisis/selección se hace SOLO con `X_train`.

- [ ] *  Columnas categóricas. 0.5 punto
  Evidencia mínima: método de codificación (OneHot) y resultado (número de columnas/shape).
  Líneas rojas: encoder ajustado solo con `X_train`.

- [ ] *  Reducción de la dimensionalidad. 1 punto
  Evidencia mínima: técnica usada (PCA/SVD/otra) y justificación + nº componentes o varianza explicada.
  Nota práctica: si hay OneHot (sparse), usa **TruncatedSVD** (equivalente práctico de PCA para sparse).
  Líneas rojas: ajuste del reductor solo con `X_train`.

---

- [ ] 3. Realiza un etiquetado automático. 1 punto
  Evidencia mínima: separación labeled/unlabeled y resultados del algoritmo de etiquetado (tabla por iteración).
  Líneas rojas: valid/test solo con etiquetas reales; pseudo-etiquetas solo para entrenamiento.

  Evidencia recomendada:
  - Tabla: `iter`, `added`, `remaining_unlabeled`
  - Gráfico: `remaining_unlabeled` vs iter
  - Resumen final: tamaño de train antes/después y distribución de clases tras pseudo-etiquetado

---

- [ ] 4. Entrena y optimiza distintos modelos supervisados.
  Evidencia mínima: comparativa de métricas y parámetros óptimos de cada modelo.
  Líneas rojas: el test se usa al final; valid sirve para seleccionar hiperparámetros/criterios del ensemble.

- [ ] *  Modelo 1. 1 punto
  Evidencia mínima: entrenamiento, hiperparámetros y métricas del modelo 1 en valid.

- [ ] *  Modelo 2. 1 punto
  Evidencia mínima: entrenamiento, hiperparámetros y métricas del modelo 2 en valid.

- [ ] *  Modelo 3. 1 punto
  Evidencia mínima: entrenamiento, hiperparámetros y métricas del modelo 3 en valid.

  Recomendación (por desbalanceo):
  - Reportar accuracy + (f1 o balanced_accuracy) en valid.

---

- [ ] 5. Crea un modelo ensemble y explica el criterio que utilizas. 1 punto
  Evidencia mínima: descripción del criterio, configuración del ensemble y métricas en valid + evaluación final en test.
  Líneas rojas: no usar el test para elegir el criterio; no usar pseudo-etiquetas en valid/test.

---

## Nota importante (“trampa” del resultado)
- Es normal obtener una precisión modesta (~0.55).
- Conclusión correcta para el informe: el etiquetado automático no es suficiente; se necesita invertir en etiquetado manual adicional.