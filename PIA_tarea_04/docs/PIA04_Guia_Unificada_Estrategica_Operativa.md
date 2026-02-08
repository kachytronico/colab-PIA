# PIA04 — Guía Unificada (Estratégica + Operativa) · v1 (2026-02-07)

> **Objetivo:** mantener en un solo documento TODO lo útil de la **Guía Estratégica** y la **Guía Operativa** sin perder contenido, pero ordenado por capas:
> - **Capa Estratégica:** cómo pensar la tarea (reglas, líneas rojas, heurísticas, decisiones típicas).
> - **Capa Operativa:** cómo ejecutarla (estructura exacta por rúbrica + pasos por notebook).

**Fuentes internas usadas para esta unificación:**  
- `PIA_04_tarea_Guía Estratégica para el Informe de Revisión Tarea PIA04.md`  
- `PIA04_Guia_Operativa_optima_v2.md`

---

## 0) Cómo usar esta guía (modo “examen/tarea”)

### 0.1 Regla de trabajo
- **Primero** estructura el notebook con títulos literales de la rúbrica.
- **Después** ejecuta el flujo: AED → preprocesado → modelos → ensembles → conclusiones.
- Cada punto de rúbrica = **1 celda Markdown** (título literal) + **celdas de código** (evidencia mínima) + **comentario** (2–5 líneas).

### 0.2 Por qué conviene mantener 2 capas (y no solo 1 documento)
- La **estratégica** es **reutilizable** en futuras unidades/tareas (reglas generales: leakage, métricas, CV, interpretabilidad).
- La **operativa** es **hiper-específica** a “lo que pide el PDF” (títulos literales, orden exacto, qué modelos y qué búsqueda).

Esta guía unificada te sirve para estudiar y tener “todo en un sitio”, pero en el repo suele ser útil **mantener también los dos archivos separados**:
- `GUIA_ESTRATEGICA.md` (reutilizable)
- `GUIA_OPERATIVA_UDx.md` (por tarea/unidad, pegada a la rúbrica del PDF)

---

# 1) Capa Estratégica (cómo pensar la tarea)

## 1.1 Resumen ejecutivo (la estrategia ganadora)
- Divide la entrega en **dos cuadernos claros** (P1 y P2).
- **P1 (Tesla / supervisado):** aplica GridSearch/RandomSearch como se pide + construye el ensemble final con **Regresión Lineal como meta-modelo** (stacking).
- **P2 (Fallos / semisupervisado):** lo crítico es el **flujo**:
  - separar etiquetados y no etiquetados,
  - reservar valid/test **solo con etiquetas reales**,
  - usar no etiquetados solo para ampliar train mediante pseudo-etiquetado conservador (umbral alto).
- Si en P2 la precisión es baja (~0.55), **no es un fallo**: la conclusión correcta es “necesitamos más etiquetado manual”.

> Esta sección “resume” y preserva el contenido del apartado 1 (Resumen Ejecutivo) de la guía estratégica original.

## 1.2 Checklist de líneas rojas (lo que más penaliza)
### Anti-leakage (el #1)
- Nunca hagas `fit()` de imputador/escalador/PCA/encoder con **todo** el conjunto.  
  **Siempre:** `fit` solo en **Train** y `transform` en Train/Val/Test.

### P2: validación corrupta (el #2)
- Validación y Test deben contener **solo datos que venían etiquetados originalmente**.  
  Prohibido validar/testear con pseudo-etiquetas.

### NL sin activación
- Si usas “NL” (Neural Layer) sin activación, en la práctica es una regresión lineal.  
  Asegura activación (p.ej. `relu`) si implementas NL como red.

### Interpretabilidad vs PCA
- Si el enunciado pide explicar variables importantes, **evita PCA**: perderás nombres/interpretación.  
  Alternativa: selección de características (SFS, importancias, etc.).

### One-Hot masivo
- Riesgo de explotar dimensionalidad. Si hay demasiadas categorías, justifica y/o reduce.

> Esta sección preserva el apartado 2 de la guía estratégica y el apartado 3 (líneas rojas) de la operativa.

## 1.3 Orden de trabajo recomendado (macro-flujo)
1) Define objetivo, target, métricas (y menciona desbalanceo si aplica).  
2) AED: describe/info/nulos/correlación/distribuciones.  
3) Split: Train/Valid/Test (y en P2, split **solo dentro de labeled**).  
4) Preprocesado con pipeline: imputación + encoding + escalado + (reducción si aplica).  
5) Modelos base → optimización (Grid/Random) usando Valid.  
6) Ensembles (según pide rúbrica) usando **valid**; **test solo al final**.  
7) Conclusiones: qué significa para negocio y qué harías mejor con más tiempo/datos.

> Preserva el apartado 3 (Orden de Trabajo) de la guía estratégica.

## 1.4 Trucos y heurísticas del profesor (lo que suele “caer bien”)
- **PCA al 90%:** `PCA(n_components=0.90)` para mantener 90% varianza explicada.  
- **Umbral alto en semisupervisado:** 0.90–0.95 para aceptar pseudo-etiquetas.  
- **Visualización:** PCA 2D solo para gráficos (aunque entrenes en alta dimensión).  
- **Tamaño valid/test en P2:** si hay pocos etiquetados, ajusta porcentajes para que sean representativos.

> Preserva el apartado 4 (Trucos y heurísticas) de la guía estratégica.

## 1.5 Errores frecuentes y cómo evitarlos
- Usar KFold y olvidar que el enunciado exige reservar Valid y Test:  
  ✅ CV solo dentro de Train, y además mantén Valid/Test separados.
- Confundir “NL”: en la tutoría se interpreta como red neuronal (MLP), no “librería rara”.
- Obsesionarse con subir P2: el objetivo es **flujo correcto** + conclusión correcta.
- Usar PCA cuando te piden interpretar variables: usa selección de características.

> Preserva el apartado 5 (Errores frecuentes) de la guía estratégica.

## 1.6 Mapa rúbrica → acciones (para no olvidarte de evidencias)
*(tabla heredada, mantenida y ampliable)*

| Ítem rúbrica | Acción práctica | Evidencia / justificación |
| --- | --- | --- |
| AED (P1 y P2) | describe(), info(), histogramas y matriz de correlación | Gráficos + texto breve de hallazgos |
| Preprocesamiento | StandardScaler (vital para KNN/SVM/NL). PCA si no afecta a interpretabilidad | shape antes/después + motivo |
| Optimización KNN/SVM | GridSearchCV | best_params_ + best_score_ |
| Optimización DT/NL | RandomizedSearchCV | best_params_ + explicación |
| Ensemble (P1) | Stacking: predicciones modelos base → Regresión Lineal | coeficientes/pesos del meta-modelo |
| Etiquetado Auto (P2) | LabelPropagation/Spreading o Self-training con predict_proba + umbral | tabla/curva disminución unlabeled |
| Conclusión (P2) | Evaluar en Test original | si ~0.55: “faltan etiquetas manuales” |

> Preserva el apartado 7 (Mapa Rubrica -> Acciones) de la guía estratégica.

---

# 2) Capa Operativa (cómo ejecutarlo sin fallos, pegado al PDF)

## 2.1 Entrega (estricta)
- Dos `.ipynb` (uno por problema).
- Un único `.zip` con ambos notebooks.

Convención recomendada:
- `PIA_04_P1_Tesla_NombreApellido.ipynb`
- `PIA_04_P2_Fallos_NombreApellido.ipynb`
- `PIA_04_NombreApellido.zip`

> Preserva el apartado 2 (Entrega) de la guía operativa.

## 2.2 Plantilla universal por rúbrica (regla de oro)
Por cada ítem del PDF:
- 1 celda **Markdown** con el **título literal** del PDF
- 1+ celdas de **código** con evidencia mínima
- 1 mini comentario (2–5 líneas): qué hiciste y por qué

> Preserva el apartado 4 (Plantilla) de la guía operativa.

---

# 3) Notebook 1 — Problema 1: Sistema de arranque Tesla (supervisado)

> **Nota importante:** no mezclar procedimientos ni datos entre P1 y P2. Cada problema se resuelve de forma independiente siguiendo su propio enunciado.

> Nota: aquí la guía operativa es “a prueba de rúbrica”: 4 modelos (KNN, DT, SVM, NL) + ensembles.


## A) AED (PDF literal)
### Titulo literal del enunciado
`Realiza un AED sobre el conjunto de datos.`  
- qué mirar: nulos, distribución target, outliers, correlación.

### Titulo literal del enunciado
`Estadísticos iniciales.`  
- `df.describe(include='all')` + 3 hallazgos.

### Titulo literal del enunciado
`Distribuciones de las variables numéricas del conjunto de datos.`  
- histogramas / boxplots.

### Titulo literal del enunciado
`Matriz de correlación.`  
- heatmap.

## B) Preprocesamiento (PDF literal)
### Titulo literal del enunciado
`Realiza el preprocesamiento de datos de tu problema.`  
- enumerar: split + nulos + encoding + escalado + (PCA si aplica).

### Titulo literal del enunciado
`Reserva un conjunto de datos para validación y otro para testeo.`  
- recomendado: 70/15/15 estratificado.

### Titulo literal del enunciado
`Columnas inútiles, valores sin sentido y atípicos.`  
- IDs/constantes/duplicadas → fuera.  
- valores imposibles → regla en train.

### Titulo literal del enunciado
`Tratamiento de valores nulos.`  
- imputación fit solo en train.

### Titulo literal del enunciado
`Análisis de variabilidad.`  
- eliminar varianza 0/casi 0 con umbral.

### Titulo literal del enunciado
`Columnas categóricas.`  
- OneHotEncoder.

### Titulo literal del enunciado
`Reducción de la dimensionalidad.`  
- PCA 0.90–0.95 si hay muchas columnas y no rompe interpretabilidad.

## C) Modelos (PDF literal) — 4 obligatorios
### C1 — KNN
`Entrena y optimiza un modelo de KNN.`  
Subceldas:
- `Entrenar un KNN.`
- `Optimizar el KNN con la técnica GridSearch.`

### C2 — DT
`Entrena y optimiza un modelo de DT.`  
Subceldas:
- `Entrenar un DT.`
- `Explicar el DT.` (antes)
- `Optimizar el DT con la técnica RandomSearch.`
- `Explicar el DT.` (después)

### C3 — SVM
`Entrena y optimiza un modelo de SVM.`  
Subceldas:
- `Entrenar un SVM.`
- `Optimizar el SVM con la técnica GridSearch.`

### C4 — NL
`Entrena y optimiza un modelo de NL.`  
Subceldas:
- `Entrenar un NL.`
- `Optimizar el NL con la técnica RandomSearch.`  
Recomendación: implementar NL como `MLPClassifier` (activación obligatoria), con escalado.

## D) Ensembles (PDF literal)
`Crear modelos ensemble usando:`

### D1.1 — Fiabilidad > 80%
`Los tres mejores modelos obtenidos, usando el siguiente criterio: media aritmética de todos los modelos que tengan una fiabilidad superior al 80%.`  
- seleccionar modelos con `max_proba >= 0.80`, promediar probas; fallback si ninguno cumple.

### D1.2 — Regresión lineal como criterio
`Todos los modelos, usando como criterio un modelo de Regresión Lineal.`  
- stacking: usar probas/preds de modelos base como entradas y entrenar `LinearRegression` como meta.  
- umbral 0.5 para convertir score a clase (o calibrar con valid y explicarlo).

---

# 4) Notebook 2 — Problema 2: Fallos de producto (semisupervisado)

> **Nota importante:** no mezclar procedimientos ni datos entre P1 y P2. Cada problema se resuelve de forma independiente siguiendo su propio enunciado.

## A) AED (PDF literal)
- `Realiza un AED sobre el conjunto de datos.`
- `Estadísticos iniciales.`
- `Distribuciones de las variables numéricas del conjunto de datos.`
- `Matriz de correlación.`

## B) Preprocesamiento (PDF literal)
- `Realiza el preprocesamiento de datos de tu problema.`
- `Reserva un conjunto de datos para validación y otro para testeo.`  
  **Línea roja:** valid/test solo con filas con etiqueta real.
- `Columnas inútiles, valores sin sentido y atípicos.`
- `Tratamiento de valores nulos.`
- `Análisis de variabilidad.`
- `Columnas categóricas.`
- `Reducción de la dimensionalidad.`

## C) Semisupervisado (PDF literal)
### Titulo literal del enunciado
`Realiza un etiquetado automático.`

Flujo recomendado (compatible con tutorías):
1) Separa `df_labeled` (target conocido) y `df_unlabeled` (target vacío).  
2) De `df_labeled`, crea `train_labeled`, `valid_labeled`, `test_labeled` (puros).  
3) Preprocesado: **fit en train_labeled** → transform en valid/test/unlabeled.  
4) Etiquetado automático (dos opciones válidas, elige UNA y justifica):
   - **Opción A: LabelSpreading/LabelPropagation:** entrenas con labeled + unlabeled (-1) y luego filtras por confianza.  
   - **Opción B: Self-training iterativo:** entrenas un modelo base, predices probas en unlabeled, aceptas si conf≥0.90, añades a train y repites.
5) Umbral recomendado: **0.90** (o 0.95 si quieres ultra-conservador).  
6) Prohibido: usar pseudo-etiquetas para validar/testear.

Texto recomendado en conclusiones:
- Si accuracy ronda 0.55–0.60, es plausible; conclusión correcta: “necesitamos más etiquetas reales”.

## D) Supervisado (PDF literal) — 3 modelos
`Entrena y optimiza distintos modelos supervisados.`
- `Modelo 1.`
- `Modelo 2.`
- `Modelo 3.`

Recomendación simple:
- Modelo 1: KNN o DT  
- Modelo 2: SVM  
- Modelo 3: NL (MLP)

## E) Ensemble final (PDF literal)
`Crea un modelo ensemble y explica el criterio que utilizas.`
Criterios defendibles:
- soft voting con pesos por rendimiento en valid
- stacking (justificar anti-leakage)

---

# 5) Fragmentos clave (aclaraciones que resuelven dudas típicas)
- “NL” se interpreta como *neural layer / red neuronal* (evita una capa lineal sin activación).
- El ensemble del P1 pide explícitamente “Regresión Lineal” como criterio (mejor no cambiarlo por logística si quieres ir seguro).
- En P2: valid/test siempre con datos etiquetados reales; pseudo-etiquetas solo para entrenar.
- En P2: es normal que el resultado sea modesto; conclusión correcta: invertir en etiquetado manual.

---

# 6) Apéndice: plantillas rápidas y “superfunción clean” sin leakage

## 6.1 “Superfunción clean” (cómo usarla bien)
La idea de una `clean()` es buena *siempre que*:
- **fit** solo en train (devuelve un objeto “preprocesador” ya ajustado),
- y luego uses **transform** en valid/test.

Patrón recomendado: `Pipeline` + `ColumnTransformer` (evita fugas por diseño).

## 6.2 Checklist final antes de comprimir
- ¿Dos `.ipynb` y un `.zip`?
- ¿Cada apartado del PDF aparece como título literal?
- ¿Split antes de imputar/escalar/PCA?
- ¿Transformadores fit solo en train?
- P1: ¿KNN GridSearch, DT RandomSearch + explicación, SVM GridSearch, NL RandomSearch?
- P1: ¿Ensembles con (a) fiabilidad >80% y (b) Regresión Lineal?
- P2: ¿valid/test solo con etiquetas reales? ¿umbral 0.90?
- P2: ¿3 modelos supervisados + ensemble explicado?

---

## 7) ANEXO — Texto original preservado (por trazabilidad)

### 7.1 Guía Estratégica original (sin modificaciones)
```text
Informe de Revision: Tarea PIA04 (Supervisado y Semisupervisado)

1. Resumen Ejecutivo
Para aprobar sin complicaciones, divide la tarea en dos cuadernos claros. En el Problema 1 (Tesla), centrate en aplicar GridSearch/RandomSearch como se pide y construye el ensemble final usando una Regresion Lineal que tome como input las predicciones de los otros modelos (Stacking). En el Problema 2 (Fallos), la clave es el flujo de trabajo: separa los datos etiquetados para Validacion/Test y usa los no etiquetados solo para entrenar iterativamente (Self-training). No te asustes si la precision del Problema 2 es baja (~0.55); el profesor espera ese resultado y la conclusion correcta es "necesitamos etiquetar mas datos manualmente". Usa una "superfuncion" (clean) para el preprocesamiento para evitar fuga de datos.

2. Checklist de Lineas Rojas (Lo que penaliza)
- Fuga de Datos (Data Leakage): Nunca hagas fit del escalador o PCA con todo el conjunto. Haz fit solo con Train y transform a Train, Val y Test.
- Validacion Corrupta (Prob. 2): Los conjuntos de Validacion y Test deben contener SOLAMENTE datos que venian etiquetados originalmente. No uses datos pseudo-etiquetados para validar.
- NL sin activacion: Si usas NL (Neural Layer/Red Neuronal) sin funcion de activacion, es solo una regresion lineal. Usala obligatoriamente.
- Interpretabilidad vs PCA: Si el enunciado pide explicar que variables son importantes (interpretacion), NO uses PCA, o perderas la capacidad de explicar el modelo.
- One-Hot masivo: Cuidado con generar demasiadas columnas con One-Hot Encoding si no es necesario.

3. Orden de Trabajo Recomendado
- Funcion de Limpieza Global: Crea una funcion clean(dataset) que incluya imputacion, encoding y escalado. Esto facilita reutilizarla para Train/Val/Test (fit solo en Train).
- Problema 1 (Tesla - Supervisado):
	- AED y Preprocesamiento (StandardScaler es vital para KNN/SVM/Redes).
	- Entrenar KNN, DT, SVM, NL (Red Neuronal) optimizando hiperparametros.
	- Ensemble (Stacking): Entrena una Regresion Lineal usando las predicciones de los modelos anteriores como entrada y la etiqueta real como salida.
- Problema 2 (Fallos - Semisupervisado):
	- Division Critica: Separa datos con etiqueta (Conocidos) y sin etiqueta (Desconocidos).
	- Sub-division: De los Conocidos, separa Train/Val/Test.
	- Bucle Semisupervisado: Usa LabelPropagation o LabelSpreading para etiquetar y filtra los de alta confianza (>90%) antes de anadirlos a Train.
	- Evaluacion final: Evalua contra el Test original (etiquetado real).

4. Trucos y Heuristicas del Profesor
- PCA al 90%: En lugar de elegir un numero fijo de componentes, configura PCA con n_components=0.90 para mantener el 90% de la varianza explicada.
- Umbral de Confianza: En el problema semisupervisado, usa un threshold alto (0.90 - 0.95) en predict_proba para aceptar una pseudo-etiqueta.
- Visualizacion: Aunque uses muchas dimensiones para entrenar, puedes hacer un PCA a 2 dimensiones aparte solo para generar graficos y mostrar los datos.
- Ajuste de divisiones (Prob 2): Si tienes pocos datos etiquetados, calcula el porcentaje exacto para que Val/Test tengan un tamano representativo respecto al total, no solo respecto a los etiquetados.

5. Errores Frecuentes y Como Evitarlos
- Error: Usar KFold y separar manualmente validacion.
	- Solucion: Aunque uses CrossValidation, el enunciado exige reservar Validacion y Test. Usa CV solo dentro de Train.
- Error: Pensar que NL es una libreria rara.
	- Solucion: NL significa Neural Layer (Red Neuronal / MLPClassifier).
- Error: Intentar arreglar la baja precision del Problema 2 hasta el infinito.
	- Solucion: Aceptar que 0.55 es normal y concluir que el etiquetado automatico no basta.
- Error: Usar PCA cuando se pide identificar factores de riesgo importantes.
	- Solucion: Usar Feature Selection (ej. SequentialFeatureSelector) en lugar de PCA para mantener los nombres de las columnas originales.

6. Entrega y Formato
- Formato: Un unico archivo ZIP.
- Contenido: Dos documentos .ipynb (Jupyter o Colab), uno por problema.
- Estructura interna: Se recomienda importar librerias al principio o donde se necesiten, pero mantener el orden logico de los hitos.

7. Mapa Rubrica -> Acciones
| Item Rubrica | Accion Practica | Evidencia / Justificacion |
| --- | --- | --- |
| AED (P1 y P2) | describe(), info(), histogramas y matriz de correlacion. | Graficos y breve texto explicando si hay nulos o correlaciones. |
| Preprocesamiento | StandardScaler (obligatorio para KNN/SVM/NL). PCA (si >20 cols y no pide explicacion). | Mostrar shape antes y despues. Justificar escalado por distancias. |
| Optimizacion KNN/SVM | Usar GridSearchCV. | Imprimir best_params_ y best_score_. |
| Optimizacion DT/NL | Usar RandomizedSearchCV. | Imprimir best_params_. Explicar el arbol si se pide (feature importance). |
| Ensemble (P1) | Stacking: Crear DF con predicciones de modelos base -> Entrenar Regresion Lineal. | Mostrar coeficientes de la Regresion Lineal (pesos de cada modelo). |
| Etiquetado Auto (P2) | LabelPropagation o LabelSpreading. Usar predict_proba > 0.90. | Grafica mostrando como disminuyen los unlabeled en cada iteracion. |
| Conclusion (P2) | Evaluar en Test set original. | Si Accuracy es baja (~0.55), escribir: "Se requieren mas etiquetas manuales". |

8. Fragmentos Clave (Conflictos y Aclaraciones)
- Sobre el significado de NL: "NL significa neural layer, vale? Que basicamente es red neuronal... MLPClassifier".
- Sobre el Ensemble del Problema 1: "Basicamente lo que quiero es... que el modelo de regresion lineal sea el que me esta produciendo los resultados para mi ensemble con esos pesos que ha establecido".
- Sobre la baja nota en el Problema 2: "Lo normal es que este conjunto de datos como mucho, os de una precision del 055... El que supere eso... que sepa que lo tiene muy bien".
- Sobre la conclusion del Problema 2: "Necesito etiquetar mas datos. Esa seria mi conclusion despues del problema 4.2".
- Sobre Validacion en Semisupervisado: "Para validar y testear siempre, siempre, siempre datos que esten etiquetados... Si coges datos seudoetiquetados para vuestra validacion y testeo, va a haber problemas".
- Sobre PCA: "Yo personalmente suelo empezar a aplicar la PCA cuando paso de 20 columnas... PCA siempre la pondria a 0.90".
- Conflicto resuelto (PCA vs Seleccion): "Si es una PCA, no se si se borrara la columna de genero... Como quiero si o si que una de las columnas... se mantenga... no puedo usar una PCA, tengo que aplicar una seleccion de caracteristicas".
```

### 7.2 Guía Operativa original (sin modificaciones)
```text
# PIA04 — Guía Operativa Óptima (PDF literal + tutorías)  
**Objetivo:** ejecutar la tarea sin fallos y con el cuaderno “corregible”: **cada punto de la rúbrica aparece como sección con el texto literal del PDF**.  
**Tutorías aplicadas:** anti-leakage, PCA 0.90–0.95, correlación, semisupervisado con valid/test etiquetados, umbral 0.90 para pseudo-etiquetas, expectativas realistas de métrica.

**Documento complementario de revisión:** `PIA_04_tarea_Guía Estratégica para el Informe de Revisión Tarea PIA04.md`.

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

## (Opcional) Contexto + objetivo
- Qué predices (accidente sí/no), métrica elegida, y cómo vas a evitar leakage.

---

## A) AED (PDF literal)

### ✅ Titulo literal del enunciado
`Realiza un AED sobre el conjunto de datos.`  
**Texto sugerido (3–5 líneas):** qué miras: nulos, distribución del target, outliers, correlación.

### ✅ Titulo literal del enunciado
`Estadísticos iniciales.`  
**Código mínimo:** `df.describe(include='all')` + 3 hallazgos.

### ✅ Titulo literal del enunciado
`Distribuciones de las variables numéricas del conjunto de datos.`  
**Código mínimo:** histogramas/boxplots (si hay muchas, agrupa o muestra top-N).  
**Evidencia:** 3–6 gráficos con título.

### ✅ Titulo literal del enunciado
`Matriz de correlación.`  
**Código mínimo:** heatmap.  
**Decisión típica:** si |corr|>0.95 elimina una (mejor si conservas la interpretable).

---

## B) Preprocesamiento (PDF literal)

### ✅ Titulo literal del enunciado
`Realiza el preprocesamiento de datos de tu problema.`  
**Texto:** enumera lo que harás: split + nulos + encoding + escalado + (PCA si aplica).

### ✅ Titulo literal del enunciado
`Reserva un conjunto de datos para validación y otro para testeo.`  
**Recomendación segura:** 70/15/15 (o 60/20/20) con estratificación si procede.  
**Evidencia:** tamaños y proporciones.

### ✅ Titulo literal del enunciado
`Columnas inútiles, valores sin sentido y atípicos.`  
**Checklist:**
- IDs / constantes / duplicadas → fuera.
- valores imposibles → regla definida en train.
- atípicos: si decides tratarlos, que sea con criterio (y deja evidencia).

### ✅ Titulo literal del enunciado
`Tratamiento de valores nulos.`  
**Regla:** imputación fit solo en train.  
**Evidencia:** % nulos antes/después y objeto imputador.

### ✅ Titulo literal del enunciado
`Análisis de variabilidad.`  
**Acción típica:** eliminar varianza 0/casi 0 (con umbral + lista columnas).

### ✅ Titulo literal del enunciado
`Columnas categóricas.`  
**Acción típica:** OneHotEncoder.  
**Línea roja práctica:** si revienta a miles de columnas, lo justificas y simplificas.

### ✅ Titulo literal del enunciado
`Reducción de la dimensionalidad.`  
**Tutoría práctica:** si hay muchas columnas, PCA(n_components=0.90 o 0.95).  
**Extra:** PCA 2D solo para visualización si quieres.

---

## C) Modelos (PDF literal) — obligatorio cumplir los 4

### ✅ Titulo literal del enunciado
`Entrena y optimiza un modelo de KNN.`  
- Código: `KNeighborsClassifier`  
- Optimización: **GridSearchCV** (n_neighbors, weights, metric…)

Subceldas (títulos literales):
- `Entrenar un KNN.`
- `Optimizar el KNN con la técnica GridSearch.`

### ✅ Titulo literal del enunciado
`Entrena y optimiza un modelo de DT.`  
- Código: `DecisionTreeClassifier`  
- Optimización: **RandomizedSearchCV** (max_depth, min_samples_split, min_samples_leaf, criterion…)

Subceldas (títulos literales):
- `Entrenar un DT.`
- `Explicar el DT.`  ← (antes) qué controla sobreajuste  
- `Optimizar el DT con la técnica RandomSearch.`
- `Explicar el DT.`  ← (después) qué cambió y por qué

### ✅ Titulo literal del enunciado
`Entrena y optimiza un modelo de SVM.`  
- Código: `SVC(probability=True)` (si necesitas probas para ensembles)  
- Optimización: **GridSearchCV** (C, gamma, kernel)

Subceldas (títulos literales):
- `Entrenar un SVM.`
- `Optimizar el SVM con la técnica GridSearch.`  
**Nota práctica:** puede tardar bastante; evita grids enormes.

### ✅ Titulo literal del enunciado
`Entrena y optimiza un modelo de NL.`  
**Como las tutorías no lo definen explícitamente, elige 1 y justifica:**
- Opción A (muy defendible): `Perceptron` (neurona lineal)  
- Opción B: `MLPClassifier` (si tu teoría lo trata como “red neuronal”)

Subceldas (títulos literales):
- `Entrenar un NL.`
- `Optimizar el NL con la técnica RandomSearch.`

---

## D) Ensembles (PDF literal)

### ✅ Titulo literal del enunciado
`Crear modelos ensemble usando:`

#### ✅ Titulo literal del enunciado
`Los tres mejores modelos obtenidos, usando el siguiente criterio: media aritmética de todos los modelos que tengan una fiabilidad superior al 80%.`  
**Implementación clara:**
- Para cada modelo, calcula `predict_proba`.
- Para cada muestra: selecciona modelos con `max_proba >= 0.80`.
- Media aritmética de probas seleccionadas → predicción final.
- **Fallback** si ninguno cumple: usa el mejor modelo (lo documentas).

#### ✅ Titulo literal del enunciado
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

### ✅ Titulo literal del enunciado
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

### ✅ Titulo literal del enunciado
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

### ✅ Titulo literal del enunciado
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
```
