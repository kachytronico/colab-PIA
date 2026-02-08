# PIA04 — P2 (Fallos de producto) — Cómo se resolvió + mejoras mínimas (semisupervisado)

## 0) Idea central
El dataset mezcla:
- Labeled: `failure` con valor real
- Unlabeled: `failure = NaN`

La regla de oro:
- VALID/TEST solo salen de Labeled real.
- El pseudo-etiquetado solo sirve para ampliar TRAIN.

---

## 1) Separación temprana (anti-leakage)
**Qué se hace**
- Cuantificar nulos en `failure`.
- Separar `df_labeled` y `df_unlabeled`.
- Split Train/Valid/Test solo dentro de labeled.

**Por qué**
- Si metes pseudo-etiquetas en valid/test, la evaluación se vuelve falsa.

---

## 2) Preprocesado (fit solo en train)
**Qué se hace**
- ColumnTransformer:
  - num: imputación mediana + StandardScaler
  - cat: imputación moda + OneHotEncoder (handle_unknown)

**Por qué**
- Imputadores/encoders/escaladores aprenden parámetros (si ajustan con valid/test, fuga).

---

## 3) Dimensionalidad
**Qué se hace**
- Si OHE genera muchas columnas, reducir dimensión (PCA/SVD) preservando ~0.90.

**Por qué**
- Menos ruido/colinealidad, mejor estabilidad y tiempos.

---

## 4) Etiquetado automático (self-training)
**Idea**
- Entrenar modelo base con Train etiquetado.
- Predecir probas en Unlabeled.
- Solo aceptar pseudo-etiquetas si max_proba >= 0.90.
- Mover esas filas a Train ampliado.
- Iterar hasta que no se añadan más.

**Qué explicar**
- Umbral alto reduce ruido; es normal que se añadan pocas filas.
- Conclusión típica: hace falta más etiquetado manual para mejorar.

---

## 5) Entrenamiento final + evaluación limpia
**Qué se hace**
- Entrenar 3 modelos supervisados con Train ampliado.
- Elegir modelo final (o ensemble) según VALID.
- Evaluar en TEST original (solo una vez al final).

---

## 6) Mejoras mínimas recomendadas (sin tocar estrategia)
### 6.1 Reporte de métricas robustas (por desbalanceo)
Añadir:
- balanced_accuracy
- F1 de clase 1
- matriz de confusión

```python
from sklearn.metrics import balanced_accuracy_score, confusion_matrix, classification_report
print("Balanced accuracy:", balanced_accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, digits=4))
```
### 6.2 (Opcional) Ajuste de umbral por F1 con VALID
```python
import numpy as np
from sklearn.metrics import f1_score

proba_valid = model.predict_proba(X_valid_proc)[:,1]
ths = np.linspace(0.1, 0.9, 81)
best_t = ths[np.argmax([f1_score(y_valid, (proba_valid>=t).astype(int)) for t in ths])]
print("Mejor umbral por F1:", best_t)
```