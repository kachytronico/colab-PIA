# PIA04 — P1 (Tesla) — Cómo se resolvió + mejoras mínimas (a prueba de rúbrica)

## 0) Objetivo
Documentar el flujo completo del cuaderno (por rúbrica) y dejar mejoras mínimas para:
- evitar fugas de datos,
- blindar la literalidad del “ensemble de Regresión Lineal”,
- mejorar la explicación del DT si se usó PCA.

---

## 1) Estructura por rúbrica (qué hace cada bloque y por qué)

### 1.1 Reserva un conjunto de datos para validación y otro para testeo
**Qué se hace**
- Split estratificado Train/Valid/Test (60/20/20).
- Se verifica proporción del target en cada split.

**Base teórica**
- Separar Valid y Test evita optimizar con el conjunto de evaluación final.
- Estratificar preserva distribución de clases.

**Evidencia esperada**
- Shapes y proporciones similares de `y` en train/valid/test.

---

### 1.2 Columnas inútiles, valores sin sentido y atípicos
**Qué se hace**
- Duplicados: eliminar SOLO en Train y realinear `y_train`.
- Constantes: detectar SOLO en Train y eliminar en train/valid/test.

**Base teórica**
- Si decides con todo el dataset, filtras información del futuro (leakage estructural).
- Las columnas constantes aportan 0 información y pueden complicar algunos modelos.

---

### 1.3 Tratamiento de valores nulos
**Qué se hace**
- Imputación ajustada SOLO en Train.
- Aplicación del imputador a valid/test sin volver a ajustar.

**Base teórica**
- Un imputador aprende estadísticos (mediana/moda). Ajustarlo con valid/test es fuga de datos.

---

### 1.4 Análisis de variabilidad
**Qué se hace**
- `VarianceThreshold` para eliminar varianza 0 (decisión basada en Train).

**Base teórica**
- Variables sin variación no ayudan a predecir.

---

### 1.5 Columnas categóricas
**Qué se hace**
- OneHotEncoder: fit SOLO en Train.
- Transform en valid/test con `handle_unknown="ignore"`.

**Base teórica**
- OHE “aprende” categorías existentes; si ve valid/test al ajustar, fuga de datos.

---

### 1.6 Reducción de dimensionalidad
**Qué se hace**
- Estandarizar (fit SOLO en Train).
- PCA para conservar ~0.90 varianza.

**Base teórica**
- PCA reduce dimensionalidad y ruido; ayuda a modelos sensibles a la dimensión (SVM/KNN/MLP).

---

## 2) Modelos obligatorios y optimización (qué, por qué y evidencia mínima)

### 2.1 KNN + GridSearch
- GridSearch en hiperparámetros típicos (n_neighbors, weights, metric).
- Reportar mejor config y métrica en VALID.

### 2.2 DT + RandomSearch
- RandomizedSearch en max_depth, min_samples_split, min_samples_leaf, criterion.
- Reportar mejor config y métrica en VALID.
- Explicar el DT (ver sección 4 si hay PCA).

### 2.3 SVM + GridSearch
- GridSearch en C, gamma, kernel.
- Reportar mejor config y métrica en VALID.

### 2.4 NL (MLP) + RandomSearch
- RandomizedSearch (hidden_layer_sizes, alpha, learning_rate_init, max_iter).
- Reportar mejor config y métrica en VALID.

---

## 3) Ensembles (lo que pide el enunciado + cómo dejarlo blindado)

### 3.1 Ensemble 1 — Media aritmética de probabilidades (fiabilidad>0.80)
**Implementación**
- Calcular fiabilidad en VALID (por defecto: accuracy).
- Seleccionar modelos con fiabilidad > 0.80.
- Promediar `predict_proba[:,1]` y umbral 0.5.
- Si ninguno supera 0.80: justificar fallback al mejor modelo individual (no forzar un ensemble débil).

**Qué explicar**
- Por qué “fiabilidad” se define así (o añadir balanced_accuracy/F1 como apoyo).

---

### 3.2 Ensemble 2 — Criterio “Regresión Lineal” (IMPORTANTE: literalidad)
Si el profe corrige literal, evita LogisticRegression como meta-modelo.
Haz un meta-modelo con LinearRegression sobre probabilidades base en VALID:

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# models_base = {"knn": best_knn, "dt": best_dt, "svm": best_svm, "mlp": best_mlp}

X_meta_valid = np.column_stack([m.predict_proba(X_valid_pca)[:,1] for m in models_base.values()])
meta_lr = LinearRegression().fit(X_meta_valid, y_valid)

X_meta_test  = np.column_stack([m.predict_proba(X_test_pca)[:,1] for m in models_base.values()])
y_pred_cont  = np.clip(meta_lr.predict(X_meta_test), 0, 1)
y_pred       = (y_pred_cont >= 0.5).astype(int)
```

## 4) Explicar el DT si hubo PCA (mejora mínima muy defendible)

Si el DT se entrenó con PCA, sus importancias hablan de PCs, no de variables originales.
Solución mínima: mostrar loadings para traducir PC→variables:

import pandas as pd

loadings = pd.DataFrame(
    pca.components_.T,
    index=feature_names,               # nombres tras OHE
    columns=[f"PC{i+1}" for i in range(pca.n_components_)]
)

top = loadings["PC2"].abs().sort_values(ascending=False).head(10)
display(top)