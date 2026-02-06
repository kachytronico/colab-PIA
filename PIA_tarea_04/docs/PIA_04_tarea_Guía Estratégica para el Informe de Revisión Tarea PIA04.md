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
