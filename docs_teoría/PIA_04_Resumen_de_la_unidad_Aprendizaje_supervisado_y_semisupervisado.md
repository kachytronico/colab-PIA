---
title: PIA 04 — Resumen: Aprendizaje supervisado y semisupervisado
source: PIA_04_Resumen de la unidad Aprendizaje supervisado y semisupervisado.docx
---

# PIA04_Resumen de la unidad Aprendizaje supervisado y semisupervisado

El aprendizaje automático ha trascendido la mera detección de patrones para convertirse en una disciplina de ingeniería capaz de predecir resultados con precisión quirúrgica. Esta unidad sintetiza los fundamentos del aprendizaje supervisado y semisupervisado, dotando al técnico de las herramientas necesarias para la toma de decisiones estratégicas en entornos de producción.
# 1. Aprendizaje supervisado

El **aprendizaje supervisado** se caracteriza por la utilización de datos previamente etiquetados por un experto humano o por otro modelo de referencia. El objetivo técnico es la **inferencia** : la capacidad de deducir valores futuros a partir de un histórico de observaciones conocidas.Este enfoque aborda cuatro tareas críticas:
**Regresión:** Predicción de variables numéricas continuas.
**Clasificación:** Asignación de categorías discretas.
**Detección y Segmentación:** Localización y delimitación de entidades en datos complejos.**El "Factor Crítico":** El diferenciador clave frente al modelo no supervisado es la posesión de la "solución" previa. Mientras que el aprendizaje no supervisado busca estructuras ciegas, el supervisado utiliza el error entre su predicción y la etiqueta real para corregir su comportamiento. Para que esta corrección sea efectiva, es vital una gestión rigurosa del flujo de datos mediante la división de conjuntos.
# 2. Conjuntos de entrenamiento, validación y testeo

La segmentación de datos no es una mera formalidad, sino la estrategia fundamental para garantizar la **generalización** . Sin una división adecuada, el modelo corre el riesgo de "memorizar" (sobreajuste), invalidando su utilidad ante datos reales.Una división profesional estándar suele seguir una proporción de **75% entrenamiento, 5% validación y 20% testeo** :
**Entrenamiento (75%):** Se utiliza para ajustar los **parámetros internos** del modelo (pesos en redes neuronales, puntos en KNN o reglas en árboles).
**Validación (5%):** Esencial para la optimización de **hiperparámetros estructurales** . Es la única pista real del rendimiento antes del despliegue.
**Testeo (20%):** Evaluación final de la capacidad de generalización. Funciona como un examen con preguntas nunca vistas para evitar la memorización.**Instrucción técnica:** Todo proceso de síntesis de datos (imputación de nulos, escalado, reducción de dimensiones) debe calcularse basándose exclusivamente en el **conjunto de entrenamiento** . Aplicar métricas de otros conjuntos provocaría una "fuga de datos" ( *data leakage* ), falseando los resultados de precisión.
## 2.1. Otros conjuntos de entrenamiento

Existen escenarios donde la aleatoriedad compromete el modelo. Por ejemplo, en el caso de un **viticultor** que desea predecir el riego según datos de la AEMET, la división debe ser **temporal** : entrenar con el pasado (2022-2023) y testear con el futuro (2024).Para conjuntos de datos pequeños (como el caso de imágenes de vendimia limitadas), se emplean técnicas avanzadas:
**k-fold cross-validation:** Divide los datos en $k$ partes, alternando entrenamiento y validación para obtener resultados robustos.
**Repeated k-fold:** Ejecuta el proceso anterior múltiples veces para maximizar la fiabilidad estadística.**Análisis de impacto:** En conjuntos desbalanceados, es imperativo usar la versión **estratificada** . En clasificación, mantiene la proporción de clases; en regresión, respeta la **distribución de varianzas** (asegurando una presencia equitativa de valores atípicos en cada grupo).
# 3. Métricas

La métrica seleccionada define el éxito del proyecto. No se busca lo mismo al predecir un salario que al detectar una enfermedad.
**Regresión:** El objetivo es la **aproximación** . Se emplean el Error Absoluto Medio ( **MAE** ), la Raíz del Error Cuadrático Medio ( **RMSE** ), e incluso la **Curva ROC** o la **Entropía** para medir la proximidad entre la predicción y el valor real.
**Clasificación:** El objetivo es la **exactitud** . Se basa en la matriz de confusión: **Verdaderos/Falsos Positivos (TP/FP)** y **Verdaderos/Falsos Negativos (TN/FN)** . Las métricas clave son **Accuracy** (exactitud global), **Precision** (calidad del positivo) y **Recall** (sensibilidad o capacidad de captura).**El "So What?":** Mientras que la regresión tolera márgenes de error (cercanía), la clasificación exige la coincidencia exacta de la etiqueta.
# 4. KNN (k-nearest neighbors)

El algoritmo KNN basa su lógica en la vecindad espacial mediante dos fases:
**Memorización:** Posiciona todos los puntos de entrenamiento en un hiperespacio.
**Búsqueda:** Localiza los $k$ vecinos más cercanos al nuevo dato para asignar un valor por mayoría (clasificación) o media (regresión).**Configuración Técnica:** Sus hiperparámetros son el **Número de vecinos (** **$k**$ **)** —preferiblemente impar para evitar empates— y la **Métrica de distancia** (Minkowski o **Distancia del Coseno** ).**Advertencia de experto:** Es obligatorio **estandarizar** los datos. KNN es extremadamente sensible a las escalas de las variables, lo que puede derivar en la "maldición de la dimensionalidad".
# 5. Optimización de hiperparámetros

Es crucial distinguir entre **parámetros** (valores internos aprendidos automáticamente) e **hiperparámetros** (ajustes estructurales manuales definidos por el programador). Una mala definición de estos últimos puede invalidar el modelo más sofisticado.
## 5.1. Optimización completa (GridSearch)

Método de "fuerza bruta" que prueba todas las combinaciones posibles en una rejilla definida. Es útil para pocos hiperparámetros, pero ineficiente cuando el espacio de búsqueda crece.
## 5.2. Optimización aleatoria (RandomSearch)

Búsqueda estocástica que selecciona valores aleatorios dentro de distribuciones de probabilidad ( **Uniforme, Binomial, Poisson** ). Es significativamente más rápida y suele encontrar soluciones óptimas con menor coste computacional.
## 5.3. Otras optimizaciones

**Algoritmos Genéticos:** Simulan la selección natural (Darwin) mediante poblaciones de modelos que "mutan" y se cruzan.
**Optimización Bayesiana:** Busca el máximo global con las mínimas iteraciones, ideal cuando el entrenamiento es costoso.
**Optuna:** *Framework* moderno que abstrae y automatiza estas estrategias.
# 6. Árboles de decisión

Representan el concepto de **"caja blanca"** : modelos totalmente interpretables que generan reglas lógicas binarias (nodos y hojas). Utilizan criterios de partición como **Gini, Entropía o log_loss** .**Valor Estratégico:** Al no depender de distancias, **no requieren estandarización** y son inmunes a valores atípicos. Su transparencia los hace obligatorios en sectores con implicaciones éticas o legales, como la medicina o la banca.
# 7. SVM (Support Vector Machines)

Las SVM proyectan datos en el espacio de características para hallar fronteras de separación óptimas (hiperplanos). Para problemas no lineales (como el XOR), emplean **Kernels** (Linear, Poly, RBF, **Sigmoid** ) que elevan los datos a dimensiones superiores.**Hiperparámetros Críticos:**
**Gamma:** Coeficiente del kernel.
**C (Regularización):** Controla el sobreajuste. Un valor de **C más grande** produce un modelo más **laxo** , aumentando la tendencia al **sobreajuste** . Se recomiendan especialmente para conjuntos con una dimensionalidad muy elevada.
# 8. Perceptrón

Unidad mínima de computación que simula una neurona artificial mediante un modelo de regresión lineal en un hiperplano: $$p = X_1M_1 + X_2M_2 + ... + X_nM_n + b$$ Donde $X_i$ son pesos, $M_i$ características y $b$ el **sesgo o intercepto** . Su limitación principal es la rigidez lineal; no pueden modelar curvas.
# 9. Redes neuronales

Estructuras complejas de perceptrones interconectados, usualmente implementadas mediante la librería **Pytorch** .
**Arquitectura:** Capas de entrada, ocultas y de salida (un perceptrón para binaria/regresión; varios para multi-clase mediante **Softmax** ).
**No linealidad:** Se logra mediante **funciones de activación** como ReLU, Sigmoide, **Tanh** y **Softmax** .
**Entrenamiento:**
**Forward:** Cálculo de la predicción.
**Backward:** Ajuste de pesos mediante el descenso del gradiente y la **matriz Jacobiana** .
**Conceptos Clave:** Un **Batch** es el paquete de datos procesado sin modificar pesos; una **Epoch** es el procesamiento completo del conjunto de entrenamiento.**Optimización:** Las **Funciones de Pérdida** ( *Loss Functions* ) se **minimizan** siempre (vía Jacobiana). Si se desea usar una métrica de maximización (como Accuracy), se debe invertir para medir "qué tan mal clasifica". Se utilizan optimizadores como **Adam** , controlando el **Learning Rate** y el **Momentum** (inercia para saltar mínimos locales). El uso de **GPU** es crítico para el procesamiento paralelo de matrices.
# 10. Modelos ensemble

Estrategia de asamblea para maximizar la precisión:
**Bagging:** Modelos iguales en paralelo (ej. **Random Forest** ). Nota: Transforma una "caja blanca" (árbol) en una "caja negra" (bosque).
**Stacking:** Unión de modelos distintos. Se puede usar un **Perceptrón como meta-modelo** para realizar una **mayoría ponderada** , asignando pesos a cada modelo según su eficacia.
**Boosting:** Modelos débiles en serie que corrigen errores previos (ej. **XGBoost** ). Alto coste computacional pero máxima precisión.
# 11. Aprendizaje semisupervisado

Técnica esencial cuando disponemos de datos parcialmente etiquetados. El sistema emplea la **auto-supervisión** para imputar etiquetas a los valores nulos, permitiendo el uso posterior de algoritmos supervisados tradicionales sobre el conjunto resultante.
# 12. Convergencia tecnológica

El **Resultado de Aprendizaje 3 (RA3)** establece que la integración de tecnologías unificadas mejora la toma de decisiones estratégicas en los negocios. Frameworks como **scikit-learn** ejemplifican esta convergencia al estandarizar métodos heterogéneos bajo interfaces comunes ( *fit/predict* ).
## 12.1. Blockchain

Registro inmutable y descentralizado. El uso de **hashing** y seguridad criptográfica garantiza la integridad de los datos de IA. La implementación de **Smart Contracts** permite la ejecución automatizada de decisiones derivadas de modelos predictivos.
## 12.2. IoT (Internet de las cosas)

Ecosistema sensorial de sensores y actuadores. Aporta la recopilación masiva de datos en tiempo real. La **interoperabilidad** entre dispositivos es la clave para alimentar sistemas de IA escalables.
## 12.3. Cloud

Infraestructura bajo demanda ( **IaaS, PaaS, SaaS** ) que aporta la virtualización y escalabilidad necesarias para el entrenamiento de modelos complejos (como las Redes Neuronales) sin costes prohibitivos de hardware físico.
