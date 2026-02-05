# PIA04 — Guía Operativa Óptima (PDF literal + tutorías)  
**Objetivo:** ejecutar la tarea sin fallos y con el cuaderno “corregible”: **cada punto de la rúbrica aparece como sección con el texto literal del PDF**.  
**Tutorías aplicadas:** anti-leakage, PCA 0.90–0.95, correlación, semisupervisado con valid/test etiquetados, umbral 0.90 para pseudo-etiquetas, expectativas realistas de métrica.

---

## 1) Comparación rápida: lo que aporta la otra IA y lo que hay que corregir
### Lo bueno que mantengo
- Estructura tipo checklist por celdas y foco en “líneas rojas”.
- Recomendación práctica de PCA (cuando hay muchas columnas) y umbral 0.90 para pseudo-etiquetado.
- Separar labeled/unlabeled y reservar **valid/test puros** (solo etiquetas reales).

### Lo que CORRIJO para que cumpla el PDF
- En Problema 1 el PDF exige **4 modelos**: **KNN + DT + SVM + NL** (no 3).  
- El PDF exige **DT (Decision Tree)** y su optimización por **RandomSearch** (no “RandomForest” como sustituto).  
- El ensemble “de criterio Regresión Lineal” debe ser **Regresión Lineal** (no “Regresión Logística” si quieres ir a prueba de rúbrica).  
- “carpeta html exportada” y “git clone modo examen” **no aparecen en el PDF**: quedan como opcionales, no obligatorios.

---

## 2) Entrega (estricta por PDF)
- ✅ **Dos documentos `.ipynb`** (uno por problema).  
- ✅ Entrega en **un único `.zip`** con ambos `.ipynb`.

**Convención recomendada (para que el profe lo identifique fácil):**
- `PIA_04_P1_Tesla_NombreApellido.ipynb`
- `PIA_04_P2_Fallos_NombreApellido.ipynb`
- `PIA_04_NombreApellido.zip`

---

## 3) Líneas rojas (las que más penalizan)
- ⛔ **Fuga de datos**: cualquier `fit()` de imputador/escalador/PCA/encoder hecho con dataset completo.
- ⛔ **Test usado para iterar**: el test se usa al final (idealmente una vez).
- ⛔ **Problema 2**: valid/test con pseudo-etiquetas → inválido. Valid/test deben venir del subset **originalmente etiquetado**.
- ⛔ **Borrado sin justificar**: si eliminas columnas/filas, deja una celda Markdown con umbral y razón.
- ⛔ Librerías fuera de ML clásico (deep learning).

---

## 4) Plantilla de cuadernos con títulos EXACTOS del PDF
> Regla: por cada ítem del PDF, crea:
- 1 celda **Markdown** con el título literal
- debajo, 1+ celdas **Código** con evidencia mínima
- y un mini comentario de 2–5 líneas (qué hiciste y por qué)

---

# NOTEBOOK 1 — `Problema 1: Sistema de arranque Tesla`

## (Opcional) Celda 0 — Markdown: “Contexto + objetivo”
- Qué predices (accidente sí/no), métrica elegida, y cómo vas a evitar leakage.

---

## A) AED (PDF literal)

### ✅ Celda A1 — Markdown (título literal)
`Realiza un AED sobre el conjunto de datos.`  
**Texto sugerido (3–5 líneas):** qué miras: nulos, distribución del target, outliers, correlación.

### ✅ Celda A2 — Markdown (título literal)
`Estadísticos iniciales.`  
**Código mínimo:** `df.describe(include='all')` + 3 hallazgos.

### ✅ Celda A3 — Markdown (título literal)
`Distribuciones de las variables numéricas del conjunto de datos.`  
**Código mínimo:** histogramas/boxplots (si hay muchas, agrupa o muestra top-N).  
**Evidencia:** 3–6 gráficos con título.

### ✅ Celda A4 — Markdown (título literal)
`Matriz de correlación.`  
**Código mínimo:** heatmap.  
**Decisión típica:** si |corr|>0.95 elimina una (mejor si conservas la interpretable).

---

## B) Preprocesamiento (PDF literal)

### ✅ Celda B1 — Markdown (título literal)
`Realiza el preprocesamiento de datos de tu problema.`  
**Texto:** enumera lo que harás: split + nulos + encoding + escalado + (PCA si aplica).

### ✅ Celda B2 — Markdown (título literal)
`Reserva un conjunto de datos para validación y otro para testeo.`  
**Recomendación segura:** 70/15/15 (o 60/20/20) con estratificación si procede.  
**Evidencia:** tamaños y proporciones.

### ✅ Celda B3 — Markdown (título literal)
`Columnas inútiles, valores sin sentido y atípicos.`  
**Checklist:**
- IDs / constantes / duplicadas → fuera.
- valores imposibles → regla definida en train.
- atípicos: si decides tratarlos, que sea con criterio (y deja evidencia).

### ✅ Celda B4 — Markdown (título literal)
`Tratamiento de valores nulos.`  
**Regla:** imputación fit solo en train.  
**Evidencia:** % nulos antes/después y objeto imputador.

### ✅ Celda B5 — Markdown (título literal)
`Análisis de variabilidad.`  
**Acción típica:** eliminar varianza 0/casi 0 (con umbral + lista columnas).

### ✅ Celda B6 — Markdown (título literal)
`Columnas categóricas.`  
**Acción típica:** OneHotEncoder.  
**Línea roja práctica:** si revienta a miles de columnas, lo justificas y simplificas.

### ✅ Celda B7 — Markdown (título literal)
`Reducción de la dimensionalidad.`  
**Tutoría práctica:** si hay muchas columnas, PCA(n_components=0.90 o 0.95).  
**Extra:** PCA 2D solo para visualización si quieres.

---

## C) Modelos (PDF literal) — obligatorio cumplir los 4

### ✅ Celda C1 — Markdown (título literal)
`Entrena y optimiza un modelo de KNN.`  
- Código: `KNeighborsClassifier`  
- Optimización: **GridSearchCV** (n_neighbors, weights, metric…)

Subceldas (títulos literales):
- `Entrenar un KNN.`
- `Optimizar el KNN con la técnica GridSearch.`

### ✅ Celda C2 — Markdown (título literal)
`Entrena y optimiza un modelo de DT.`  
- Código: `DecisionTreeClassifier`  
- Optimización: **RandomizedSearchCV** (max_depth, min_samples_split, min_samples_leaf, criterion…)

Subceldas (títulos literales):
- `Entrenar un DT.`
- `Explicar el DT.`  ← (antes) qué controla sobreajuste  
- `Optimizar el DT con la técnica RandomSearch.`
- `Explicar el DT.`  ← (después) qué cambió y por qué

### ✅ Celda C3 — Markdown (título literal)
`Entrena y optimiza un modelo de SVM.`  
- Código: `SVC(probability=True)` (si necesitas probas para ensembles)  
- Optimización: **GridSearchCV** (C, gamma, kernel)

Subceldas (títulos literales):
- `Entrenar un SVM.`
- `Optimizar el SVM con la técnica GridSearch.`  
**Nota práctica:** puede tardar bastante; evita grids enormes.

### ✅ Celda C4 — Markdown (título literal)
`Entrena y optimiza un modelo de NL.`  
**Como las tutorías no lo definen explícitamente, elige 1 y justifica:**
- Opción A (muy defendible): `Perceptron` (neurona lineal)  
- Opción B: `MLPClassifier` (si tu teoría lo trata como “red neuronal”)

Subceldas (títulos literales):
- `Entrenar un NL.`
- `Optimizar el NL con la técnica RandomSearch.`

---

## D) Ensembles (PDF literal)

### ✅ Celda D1 — Markdown (título literal)
`Crear modelos ensemble usando:`

#### ✅ Celda D1.1 — Markdown (título literal)
`Los tres mejores modelos obtenidos, usando el siguiente criterio: media aritmética de todos los modelos que tengan una fiabilidad superior al 80%.`  
**Implementación clara:**
- Para cada modelo, calcula `predict_proba`.
- Para cada muestra: selecciona modelos con `max_proba >= 0.80`.
- Media aritmética de probas seleccionadas → predicción final.
- **Fallback** si ninguno cumple: usa el mejor modelo (lo documentas).

#### ✅ Celda D1.2 — Markdown (título literal)
`Todos los modelos, usando como criterio un modelo de Regresión Lineal.`  
**Implementación “a prueba de rúbrica”:**
- Meta-features: probas de todos los modelos base en **validación**.
- Entrenas `LinearRegression` para predecir `y`.
- En test: predices score y umbral 0.5 (o calibras con valid y lo explicas).

---

# NOTEBOOK 2 — `Problema 2: Fallos de producto`

## A) AED (PDF literal)
Celdas con títulos literales (mismo patrón que en P1):
- `Realiza un AED sobre el conjunto de datos.`
- `Estadísticos iniciales.`
- `Distribuciones de las variables numéricas del conjunto de datos.`
- `Matriz de correlación.`

---

## B) Preprocesamiento (PDF literal)
Celdas con títulos literales:
- `Realiza el preprocesamiento de datos de tu problema.`
- `Reserva un conjunto de datos para validación y otro para testeo.`  ← **valid/test solo con datos etiquetados**
- `Columnas inútiles, valores sin sentido y atípicos.`
- `Tratamiento de valores nulos.`
- `Análisis de variabilidad.`
- `Columnas categóricas.`
- `Reducción de la dimensionalidad.`

---

## C) Semisupervisado (PDF literal)

### ✅ Celda C1 — Markdown (título literal)
`Realiza un etiquetado automático.`  

**Flujo recomendado (compatible con tutorías):**
1) Separa `df_labeled` (target conocido) y `df_unlabeled` (target vacío/NaN/-1).
2) De `df_labeled`, crea `train_labeled`, `valid_labeled`, `test_labeled` (puro).
3) Preprocesado: fit en `train_labeled` → transform en `valid/test/unlabeled`.
4) Semisupervisado con `LabelSpreading` o `LabelPropagation`:
   - `X = train_labeled + unlabeled`
   - `y = y_train` y para unlabeled usa `-1`
5) Obtén `predict_proba` para unlabeled y acepta pseudo-etiquetas con confianza ≥ **0.90**.
6) Añade pseudo-etiquetas al train y reentrena (1–3 iteraciones, si quieres).
7) **Nunca** uses pseudo-etiquetas para validar/testear.

**Texto recomendado en conclusiones:** si accuracy es ~0.55–0.60, es plausible; pide más etiquetas reales para mejorar.

---

## D) Supervisado (PDF literal) — 3 modelos obligatorios

### ✅ Celda D1 — Markdown (título literal)
`Entrena y optimiza distintos modelos supervisados.`  
Subceldas con títulos literales:
- `Modelo 1.`
- `Modelo 2.`
- `Modelo 3.`

**Recomendación simple y coherente con UD4:**
- Modelo 1: KNN o DT  
- Modelo 2: SVM  
- Modelo 3: NL (MLP)  
#### Modelo NL (Neural Layer)
Según las tutorías, “NL” hace referencia a una **red neuronal**.  
En esta tarea se implementa usando:

- `MLPClassifier` (`sklearn.neural_network`)
- Con función de activación (por ejemplo: `relu`)
- Con escalado previo obligatorio (`StandardScaler`)

No usar una capa lineal sin activación, ya que equivaldría a una regresión lineal y **no cumpliría el criterio de NL**.

(pero puedes variar, siempre que sean 3 distintos y optimizados)

---

## E) Ensemble final (PDF literal)

### ✅ Celda E1 — Markdown (título literal)
`Crea un modelo ensemble y explica el criterio que utilizas.`
Criterios defendibles:
- voting soft con pesos por rendimiento en valid
- stacking (si lo haces, justifica por qué no hay leakage)

---

## 5) Checklist final antes de comprimir
- [ ] ¿Dos `.ipynb` (uno por problema) y un `.zip`?
- [ ] ¿Cada apartado del PDF aparece como título literal?
- [ ] ¿Split antes de imputar/escalar/PCA?
- [ ] ¿Transformadores fit solo en train?
- [ ] P1: ¿KNN GridSearch, DT RandomSearch + explicación (2 veces), SVM GridSearch, NL RandomSearch?
- [ ] P1: ¿Ensembles con (a) fiabilidad >80% y (b) Regresión Lineal?
- [ ] P2: ¿valid/test solo con etiquetas reales? ¿pseudo-etiquetado con umbral 0.90?
- [ ] P2: ¿3 modelos supervisados + ensemble explicado?

Nota (modo examen):
Los datasets pueden proporcionarse en repositorios externos y/o comprimidos.
Se asume que el notebook incluye una sección inicial de clonado,
exploración del sistema de archivos y descompresión antes de la carga de datos.
