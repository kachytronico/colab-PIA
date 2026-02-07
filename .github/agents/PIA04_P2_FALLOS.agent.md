# Agente exclusivo — PIA04 Problema 2: Fallos de producto

## Fuente de verdad (prioridad absoluta)
1) `docs/P2_Fallos/00_RUBRICA_LITERAL_P2.md`
2) `docs/P2_Fallos/01_PLAYBOOK_P2.md`
3) `docs/P2_Fallos/02_NOTEBOOK_TEMPLATE_P2.md`
4) `docs/PIA_04_tarea_enunciado.md` (enunciado oficial)

Si hay conflicto: Rubrica literal P2 -> Playbook P2 -> Template -> Enunciado.

---

## Hechos fijos del dataset (no negociables)
- Target: `failure`
- Unlabeled: `failure` es `NaN`
- Categóricas: `product_code`, `attribute_0`, `attribute_1`
- `id` existe y es identificador: NO usar como feature; eliminar y justificar.
- Umbral recomendado para pseudo-etiquetado: `0.90` (>= 0.90)

---

## Líneas rojas innegociables (anti-leakage)
- Valid/Test SOLO con etiquetas reales (nunca pseudo-etiquetas).
- Fit de transformadores (imputer/encoder/scaler/SVD/PCA/selector) SOLO con train.
- Prohibido incluir valid/test en el fit del self-training.
- Test se usa UNA vez al final, cuando ya están cerradas decisiones.
- No inventar resultados: si no se ejecuta, usar placeholders.

Si detectas una violación, DETENTE y corrige antes de seguir.

---

## Estructura obligatoria del notebook (títulos LITERALES)
El notebook debe contener exactamente estas secciones (celdas Markdown con ese texto):
- `Realiza un AED sobre el conjunto de datos.`
- `Estadísticos iniciales. 0.2 puntos`
- `Distribuciones de las variables numéricas del conjunto de datos. 0.3 puntos`
- `Matriz de correlación. 0.5 puntos`
- `Realiza el preprocesamiento de datos de tu problema.`
- `Reserva un conjunto de datos para validación y otro para testeo. 0.5 puntos`
- `Columnas inútiles, valores sin sentido y atípicos. 1 punto`
- `Tratamiento de valores nulos. 0.5 puntos`
- `Análisis de variabilidad. 0.5 puntos`
- `Columnas categóricas. 0.5 punto`
- `Reducción de la dimensionalidad. 1 punto`
- `Realiza un etiquetado automático. 1 punto`
- `Entrena y optimiza distintos modelos supervisados.`
  - `Modelo 1. 1 punto`
  - `Modelo 2. 1 punto`
  - `Modelo 3. 1 punto`
- `Crea un modelo ensemble y explica el criterio que utilizas. 1 punto`

Usa como base: `docs/P2_Fallos/02_NOTEBOOK_TEMPLATE_P2.md`.

---

## Decisiones técnicas recomendadas (para evitar fallos típicos)
- OneHotEncoder suele generar salida sparse. Por tanto:
  - Reducción dimensional recomendada: **TruncatedSVD** (no PCA, salvo densificar con justificación).
- Self-training debe mantener trazabilidad:
  - conservar índices de unlabeled y registrar `iter/added/remaining`.
- Métricas:
  - reportar accuracy (obligatorio) y recomendar f1/balanced_accuracy por desbalanceo.

---

## Flujo obligatorio exacto
1) Carga y verificación:
   - localizar `fallos_producto.csv` sin rutas rígidas.
   - confirmar NaN en `failure`.

2) Separar labeled/unlabeled:
   - `df_labeled = failure.notna()`
   - `df_unlabeled = failure.isna()`

3) Split SOLO en labeled:
   - estratificado -> train/valid/test
   - `valid/test` quedan congelados.

4) Preprocesado + reducción dimensional:
   - ColumnTransformer: imputación + OneHot + escalado
   - reducción: TruncatedSVD
   - fit SOLO con train

5) Etiquetado automático (self-training):
   - modelo base con `predict_proba`
   - threshold 0.90
   - mover pseudo-etiquetas al train
   - iterar hasta convergencia/max_iters
   - evidencia: tabla + gráfico

6) 3 modelos supervisados + optimización:
   - entrenar con `train_aug`
   - seleccionar con valid
   - no mirar test

7) Ensemble:
   - soft voting
   - pesos por métrica en valid (explicarlo)

8) Evaluación final:
   - test una sola vez
   - confusion matrix + classification report
   - conclusión “trampa”: si rendimiento modesto, recomendar etiquetado manual adicional.

---

## Asserts obligatorios
- `assert y_valid.notna().all() and y_test.notna().all()`
- `assert df_unlabeled["failure"].isna().all()`
- `assert set(X_train.index).isdisjoint(set(X_valid.index))`
- `assert set(X_train.index).isdisjoint(set(X_test.index))`
- `assert set(X_valid.index).isdisjoint(set(X_test.index))`
- `assert df_fallos.loc[X_valid.index, "failure"].notna().all()`
- `assert df_fallos.loc[X_test.index, "failure"].notna().all()`

---

## No inventar resultados
- Prohibido escribir métricas numéricas si no aparecen en salidas reales.
- En conclusiones usa placeholders si falta ejecutar:
  - “Por completar tras ejecutar: accuracy, f1, matriz de confusión…”