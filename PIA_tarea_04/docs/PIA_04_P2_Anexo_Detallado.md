# Anexo didactico - Problema 2 (Fallos de producto)

Este documento explica, paso a paso y como lo haria un tutor, la solucion del Problema 2 (semisupervisado) y los conceptos teoricos que la sustentan. El objetivo es que entiendas no solo que se hizo, sino por que se hizo asi y como se conecta con las decisiones de negocio.

---

## 1. Contexto del problema y filosofia de negocio

**Problema:** La empresa quiere predecir fallos, pero etiquetar fallos es caro. Por tanto, hay pocas etiquetas reales y muchos registros sin etiqueta.

**Filosofia de negocio aplicada:**
- **Maximizar valor con datos escasos:** Si etiquetar es costoso, uso un enfoque semisupervisado para aprovechar la estructura de los datos sin etiquetar.
- **Evitar riesgos de decisiones falsas:** El objetivo no es solo acertar mas, sino reducir el riesgo de decisiones incorrectas (por ejemplo, no detectar un fallo). Por eso reviso metricas y no solo accuracy.
- **Priorizar generalizacion:** Un modelo que memoriza no sirve en produccion. Por eso separo train/valid/test y evito fugas de datos.

---

## 2. Entorno y herramientas utilizadas

- **Python + Google Colab (modo examen):** permite reproducibilidad, sin rutas locales.
- **Librerias:**
  - **pandas / numpy:** lectura, limpieza, operaciones numericas.
  - **matplotlib / seaborn:** graficas para AED.
  - **scikit-learn:** pipelines, transformaciones, modelos, metricas y validacion.

**Idea clave de ingenieria:** scikit-learn estandariza el flujo con `fit` y `transform` para evitar errores y fugas de datos.

---

## 3. Carga de datos (modo examen) y criterios de calidad

Se sigue un flujo reproducible:
1) Clonar repo de datasets si no existe.
2) Buscar `datasets.zip` con `find`.
3) Descomprimir en carpeta local.
4) Localizar `fallos_producto.csv` sin rutas fijas.
5) Cargar en `df_fallos`.

**Concepto teorico:** el control de rutas y la validacion de existencia evitan errores operativos y hacen la practica reproducible.

---

## 4. AED (Analisis Exploratorio de Datos)

El AED no es un adorno: es un diagnostico de calidad, estructura y riesgos.

### 4.1 Estructura y nulos
- Se revisa `info()` y el porcentaje de nulos.
- Se confirma que `failure` tiene muchos NaN: eso justifica el semisupervisado.

**Concepto teorico:** en aprendizaje semisupervisado, las etiquetas ausentes son parte del problema, no un error.

### 4.2 Estadisticos iniciales
- `describe()` da rangos, medias, dispersion.
- Se detecta desbalance en `failure`.

**Filosofia de negocio:** en fallos, los positivos suelen ser pocos, pero son los mas caros de perder.

### 4.3 Distribuciones
- Histogramas para detectar asimetrias y posibles outliers.

**Concepto teorico:** las distribuciones ayudan a anticipar transformaciones (escalado) y posibles sesgos.

### 4.4 Correlacion
- Matriz de correlacion para redundancias.

**Concepto teorico:** si dos variables estan altamente correlacionadas, aportan poca informacion nueva. En este caso, no se eliminan por correlacion fuerte.

---

## 5. Preprocesamiento (UD02)

El preprocesamiento es la base para un modelo robusto.

### 5.1 Separacion de conjuntos (train/valid/test)
- **Regla clave:** validacion y test deben salir solo de `df_labeled`.
- Se usa `train_test_split` estratificado para mantener la proporcion de clases.

**Concepto teorico:** sin esta separacion no hay generalizacion real. Si el modelo ve los datos de test, se produce data leakage.

### 5.2 Columnas inutiles y outliers
- Se elimina `id` por ser identificador.
- No se eliminan outliers por falta de criterio de dominio.

**Filosofia de negocio:** si no hay regla clara, es mejor conservar datos que destruir informacion util.

### 5.3 Tratamiento de nulos
- **Numericas:** imputacion por mediana.
- **Categoricas:** imputacion por moda.

**Concepto teorico:** la mediana es robusta a outliers. La moda es la opcion natural en categoricas.

### 5.4 Columnas categoricas
- OneHotEncoder convierte categorias a columnas binarias.

**Concepto teorico:** los modelos no entienden texto; se requiere codificacion. OneHot evita imponer un orden falso.

### 5.5 Analisis de variabilidad
- VarianceThreshold detecta columnas con varianza casi cero.

**Concepto teorico:** una columna casi constante aporta poca informacion y puede eliminarse.

### 5.6 Reduccion de dimensionalidad (SVD)
- TruncatedSVD se aplica porque la matriz es dispersa tras OneHot.
- Se busca conservar alrededor del 90% de varianza explicada.

**Concepto teorico:** esto combate la maldicion de la dimensionalidad y mejora el rendimiento con menos ruido.

---

## 6. Comparativa A/B (SVD vs sin SVD)

Se comparan dos pipelines iguales con y sin SVD, evaluando solo en valid.

**Concepto teorico:** una decision de transformacion se valida con datos que no son test para no sesgar la evaluacion final.

---

## 7. Semisupervisado (autoetiquetado)

### 7.1 Idea base
- Se entrena un modelo con `X_train`.
- Se predicen probabilidades en unlabeled.
- Solo se aceptan pseudo-etiquetas con alta confianza (umbral).

**Concepto teorico:** se añade informacion a partir de un modelo inicial, pero solo si la confianza es alta.

### 7.2 Umbral de confianza
- Umbral 0.90 por equilibrio entre calidad y cantidad.
- Se hace tabla de sensibilidad (0.95 / 0.90 / 0.85) solo a nivel de conteo.

**Filosofia de negocio:** es mejor agregar pocas etiquetas fiables que muchas etiquetas dudosas que degraden el modelo.

---

## 8. Modelos supervisados finales

Se entrenan tres modelos con el conjunto ampliado (train + pseudo-etiquetas):

1) **LogisticRegression**
2) **RandomForestClassifier**
3) **SVC con probability=True**

Se optimizan con **GridSearch** o **RandomizedSearch**, usando CV estratificada.

**Concepto teorico:**
- **LogisticRegression** es lineal y sirve como baseline.
- **RandomForest** agrega diversidad y robustez.
- **SVC** permite fronteras no lineales.

**Buenas practicas:** se reportan accuracy, f1 y balanced_accuracy porque el dataset esta desbalanceado.

---

## 9. Ensemble

Se construye un **VotingClassifier (soft voting)** con pesos segun `balanced_accuracy`.

**Concepto teorico:**
- Un ensemble reduce la varianza y aprovecha fortalezas complementarias.
- Soft voting usa probabilidades, mas estable que la simple mayoria.

**Filosofia de negocio:** la decision final se apoya en consenso ponderado, lo que reduce el riesgo de sesgo de un unico modelo.

---

## 10. Evaluacion final en test

El test se usa una sola vez al final. Se reporta:
- Accuracy
- Balanced accuracy
- F1
- Matriz de confusion
- Classification report

**Concepto teorico:** el test es un examen final y no se usa para ajustar decisiones.

**Lectura de negocio:** aunque la exactitud global puede parecer aceptable, la sensibilidad en clase positiva es critica si los fallos son caros. Esto puede justificar invertir en mas etiquetado real o ajustar umbrales de decision.

---

## 11. Anti-leakage (gobernanza del flujo)

Checklist conceptual:
- `fit` solo en `X_train` para imputacion, OneHot, escalado y SVD.
- Valid/test salen solo de labeled.
- Pseudo-etiquetas se usan solo para ampliar train.
- Test solo se usa al final.

**Idea clave:** evitar data leakage es un requisito tecnico y etico. Si contaminamos el test, el resultado es un espejismo y el negocio toma decisiones erroneas.

---

## 12. Relacion con la teoria de la unidad

- **UD02:** limpieza, nulos, variabilidad, codificacion, dimensionalidad.
- **UD03:** aprendizaje semisupervisado y la logica de autoetiquetado.
- **UD04:** division train/valid/test, metricas, modelos y ensembles.

Este flujo conecta teoria y practica: primero garantizo datos limpios, luego un esquema de validacion correcto, y finalmente modelos y ensemble con evaluacion honesta.

---

## 13. Resumen final

La solucion combina:
- Un AED riguroso para entender la calidad del dato.
- Un preprocesamiento prudente para eliminar ruido sin perder informacion.
- Un pipeline semisupervisado para aprovechar los datos sin etiqueta.
- Tres modelos supervisados comparados con metricas adecuadas.
- Un ensemble final ponderado y evaluado en test.

Todo el proceso esta alineado con la filosofia de negocio: maximizar la deteccion de fallos, controlar el riesgo y mantener la fiabilidad del sistema con evaluacion honesta.
