# GUÍA DE ESTILO - PIA Tarea 04

## ESTRUCTURA DEL CUADERNO
El notebook debe seguir estrictamente este índice:
1. **Imports y Configuración:** Una celda inicial con todos los imports y `sns.set_style()`.
2. **Problema 1: Tesla (Supervisado)**
   - 2.1 Carga de Datos (GitHub Raw).
   - 2.2 EDA (Info, Describe, Histogramas, Correlación).
   - 2.3 Preprocesamiento (Limpieza nulos/outliers, Encoding, Escalado, Split Train/Test).
   - 2.4 Modelado (3 Modelos: KNN, Árbol, SVM/RegLog). Uso de GridSearch.
   - 2.5 Ensemble y Métricas Finales.
3. **Problema 2: Fallos (Semisupervisado)**
   - 3.1 Carga y EDA.
   - 3.2 Preprocesamiento Específico.
   - 3.3 Etiquetado Automático (LabelPropagation).
   - 3.4 Modelo Final (entrenado con las nuevas etiquetas).

## REGLAS DE CODIFICACIÓN
- **Gráficas:** Usar `seaborn` con estilo `whitegrid`. Tamaño `figsize=(10, 6)`. Poner siempre título a los gráficos.
- **Variables:** Nombres descriptivos en minúsculas (`df_tesla`, `X_train`, `y_pred`). Evitar `df1`, `data`, etc.
- **Comentarios:** Comentar encima de la línea de código, no al final.
  - *Mal:* `model.fit(X, y) # entrenamos`
  - *Bien:* ```python
    # Entrenamos el modelo con los datos de validación cruzada
    model.fit(X_train, y_train)
    ```
- **Pipelines:** Si es posible, usar `Pipeline` de sklearn, pero si complica la explicación pedagógica, hacer los pasos por separado (fit_transform).

## MANEJO DE ERRORES
Si el código falla, no propongas soluciones complejas. Busca la causa más simple:
1. ¿La URL del CSV es correcta?
2. ¿Hay nulos que rompen el modelo (`NaN`)?
3. ¿Hay variables categóricas (texto) sin codificar a números?