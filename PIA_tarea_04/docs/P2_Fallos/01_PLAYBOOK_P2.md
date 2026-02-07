# Playbook P2 — Fallos de producto (SOLO P2)
Guía operativa paso a paso para `fallos_producto.csv`, diseñada para cumplir la rúbrica y evitar fugas de datos.

## Datos clave (confirmados y no negociables)
- target: `failure`
- unlabeled: `failure` es `NaN`
- categóricas: `product_code`, `attribute_0`, `attribute_1`
- `id` existe y se trata como identificador (no feature; eliminar y justificar)
- umbral recomendado de pseudo-etiquetado: `0.90`

---

## 1) Carga y verificación básica
1. Cargar `fallos_producto.csv` en `df_fallos`.
2. Confirmar shape, columnas y tipos (`info()`).
3. Confirmar unlabeled: `df_fallos["failure"].isna().sum()`.
4. Confirmar categóricas: `product_code`, `attribute_0`, `attribute_1`.
5. Confirmar `id` como identificador:
   - decisión recomendada: eliminar de features (evita “memorizar” ids).

---

## 2) Separar labeled y unlabeled (CRÍTICO)
1. `df_labeled = df_fallos[df_fallos["failure"].notna()].copy()`
2. `df_unlabeled = df_fallos[df_fallos["failure"].isna()].copy()`
3. Registrar conteos para el informe (nº labeled, nº unlabeled y %).

---

## 3) Split SOLO dentro de labeled (anti-leakage)
1. Crear features/target SOLO con labeled:
   - `X_labeled = df_labeled.drop(columns=["failure", "id"])`
   - `y_labeled = df_labeled["failure"].astype(int)`
2. Split estratificado:
   - train 70%, valid 15%, test 15% (o similar)
3. Guardar `X_valid`, `y_valid`, `X_test`, `y_test` y NO tocarlos en el self-training.
4. `X_unlabeled = df_unlabeled.drop(columns=["failure", "id"])`

Regla de oro:
- Valid/Test contienen SOLO etiquetas reales (nunca pseudo-etiquetas).

---

## 4) Preprocesado (Pipeline + ColumnTransformer) + Reducción dimensional
Objetivo: imputación + OneHot + escalado + reducción dimensional sin romper sparse.

### 4.1 Definir columnas
- `cat_cols = ["product_code", "attribute_0", "attribute_1"]`
- `num_cols = [c for c in X_labeled.columns if c not in cat_cols]`

### 4.2 Limpieza mínima (rúbrica “columnas inútiles / valores sin sentido / atípicos”)
- Eliminar `id` (ya fuera).
- Si aplicas reglas de atípicos, defínelas SOLO con train (ej. percentiles) y aplica luego al resto.
- Si no hay reglas claras de dominio, documenta que no se eliminan outliers por falta de criterio de negocio.

### 4.3 Nulos (imputación)
- Numéricas: `SimpleImputer(strategy="median")`
- Categóricas: `SimpleImputer(strategy="most_frequent")`

### 4.4 OneHot en categóricas
- `OneHotEncoder(handle_unknown="ignore")`

### 4.5 Escalado
- Para numéricas: `StandardScaler()`
- Ojo: con OneHot la salida suele ser sparse; evita centrar sparse:
  - opción A: escalar solo numéricas dentro del ColumnTransformer (recomendado)
  - opción B: si escalas después, usa `StandardScaler(with_mean=False)`

### 4.6 Reducción de dimensionalidad (rúbrica)
- Recomendación práctica: **TruncatedSVD** (apto para matrices sparse)
- “PCA(n_components=0.90)” solo si conviertes a dense (no recomendado por memoria).
- Justificación en el informe:
  - OneHot → alta dimensionalidad
  - SVD reduce dimensionalidad manteniendo estructura útil

### 4.7 Anti-leakage (obligatorio)
- `fit` del preprocesador (imputer/encoder/scaler/SVD) SOLO con `X_train_labeled`.
- `transform` a valid/test/unlabeled con el mismo objeto ajustado.

---

## 5) Análisis de variabilidad (rúbrica)
Opción robusta y simple (sin pelear con sparse):
- Hacer “análisis de baja varianza” SOLO sobre **numéricas** en `X_train_labeled`:
  - `var = X_train[num_cols].var()`
  - eliminar columnas con var muy baja (ej. `< 1e-6`) si aparece alguna
- Documentar si no se elimina nada.

---

## 6) Etiquetado automático (Self-training iterativo)
Método: modelo base + `predict_proba` + threshold 0.90 + mover ejemplos al train.

1. Modelo base recomendado:
   - `LogisticRegression(max_iter=2000, class_weight="balanced")` o KNN
2. Preparación:
   - ajustar preprocesador SOLO con `X_train_labeled`
   - transformar `X_train_labeled` y `X_unlabeled`
3. Iterar:
   - entrenar modelo base con el train actual
   - `predict_proba` en unlabeled
   - aceptar pseudo-etiquetas si `max_proba >= 0.90`
   - mover a train (con pseudo etiqueta)
   - eliminar de unlabeled
   - parar si no se añade nada o `max_iters`

Evidencia mínima:
- tabla por iteración: `iter`, `added`, `remaining_unlabeled`
- gráfico: remaining vs iter
- resumen final: tamaño train antes/después y distribución de clases

Líneas rojas:
- Nunca pseudo-etiquetar valid/test.
- Nunca incluir valid/test en el fit del modelo base ni del preprocesador.

---

## 7) Modelos supervisados (3 distintos) + optimización
1. Entrenar y optimizar 3 modelos distintos con el **train ampliado** (reales + pseudo).
2. Validación:
   - usar `valid_labeled` (etiquetas reales) para comparar y seleccionar.
3. Test:
   - usar `test_labeled` SOLO al final.

Modelos sugeridos:
- Modelo 1: LogisticRegression
- Modelo 2: RandomForestClassifier
- Modelo 3: SVC(probability=True) o HistGradientBoostingClassifier

Métricas recomendadas:
- accuracy (por enunciado) + f1 o balanced_accuracy (por desbalanceo)

---

## 8) Ensemble final
- Soft voting (promedio de probabilidades) recomendado.
- Pesos: proporcionales a la métrica elegida en valid (explicar fórmula).
- Comparar ensemble vs mejor individual.

---

## 9) Evaluación final
- Evaluar SOLO contra `test_labeled` original.
- Reportar: accuracy + confusion matrix + classification report.
- Conclusión esperable:
  - si accuracy ~0.55, “etiquetado automático no es suficiente; hace falta etiquetado manual”.

---

## 10) Asserts anti-leakage (pegar en el notebook)
- `assert y_valid.notna().all() and y_test.notna().all()`
- `assert df_unlabeled["failure"].isna().all()`
- `assert set(X_train.index).isdisjoint(set(X_valid.index))`
- `assert set(X_train.index).isdisjoint(set(X_test.index))`
- `assert set(X_valid.index).isdisjoint(set(X_test.index))`
- (si conservas índices del df original)
  - `assert df_fallos.loc[X_valid.index, "failure"].notna().all()`
  - `assert df_fallos.loc[X_test.index, "failure"].notna().all()`