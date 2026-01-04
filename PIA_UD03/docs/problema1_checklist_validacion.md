# Checklist de Validación - Problema 1 Netflix

## Uso de este Checklist

Usa este checklist para **auto-evaluar tu implementación** antes de entregar. Marca cada ítem conforme lo completes.

---

## ✓ Objetivo Final: 10 Películas Exactas

- [ ] El código verifica que `s5485` existe en el dataset
- [ ] El código verifica que `s5485` es de tipo `Movie` (no `TV Show`)
- [ ] El recomendador retorna exactamente **10 elementos**
- [ ] Todos los 10 elementos son de tipo `Movie`
- [ ] Se muestra `show_id` e `title` de cada recomendación
- [ ] Los resultados son reproducibles (mismos resultados cada vez)

---

## ✓ Preparación y Coherencia de Datos

### Manejo de show_id
- [ ] `show_id` es establecido como índice en `df` desde el AED
- [ ] `show_id` se mantiene recuperable (como índice o columna)
- [ ] No se pierde `show_id` en ningún paso del preprocesamiento

### Manejo de Nulos
- [ ] Se reporta el conteo de nulos por columna
- [ ] `cast` relleno con `"Unknown"` (no se borran filas)
- [ ] `director` relleno con `"Unknown"` (no se borran filas)
- [ ] No hay inconsistencias en el relleno (todas las columnas se tratan igual)

### Coherencia del Pipeline
- [ ] El preprocesamiento se realiza **una sola vez** (sin duplicación)
- [ ] Está claro dónde comienza y dónde termina el preprocesamiento
- [ ] Se describe brevemente qué hace cada paso

---

## ✓ Ingeniería de Características (Features)

### Cast (Reparto)
- [ ] Se crea `num_cast` (número de actores)
- [ ] Fórmula: contar commas + 1, o usar `.split(',')` y `len()`
- [ ] Ejemplo: "Actor1, Actor2, Actor3" → `num_cast = 3`
- [ ] `num_cast` es numérico y no genera errores

### Géneros (listed_in)
- [ ] Se aplica One-Hot Encoding a `listed_in` (ej. con `pd.get_dummies()`)
- [ ] Géneros están separados por comas en el dataset original
- [ ] Cada género genera una columna binaria (0/1)
- [ ] Ejemplo: "Drama, Action" → Drama=1, Action=1, Comedy=0, etc.

### Tipo (type)
- [ ] Se maneja la columna `type` (Movie vs. TV Show)
- [ ] Opción A: Codificar (Movie=1, TV Show=0)
- [ ] Opción B: Descartar antes del clustering (válido también)
- [ ] Si se descarta, el filtrado final se hace sobre el `df` original

### Columnas Eliminadas (Ruido)
- [ ] `title`: Eliminada (es lo que queremos recomendar)
- [ ] `description`: Eliminada (requeriría NLP)
- [ ] `director`: Eliminada (demasiados valores únicos > 4000)
- [ ] `country`: Eliminada (demasiados valores únicos)
- [ ] `show_id`: Mantenida como índice (no como feature)

---

## ✓ Escalado y Reducción Dimensional

### StandardScaler
- [ ] Se aplica `StandardScaler` sobre las features numéricas
- [ ] Se aplica DESPUÉS del One-Hot Encoding
- [ ] Todas las features numéricas se escalan (media=0, desv.std=1)
- [ ] Se muestra cómo se ve una fila escalada (para verificar)

### PCA
- [ ] Se aplica PCA sobre datos escalados
- [ ] Se reporta el **% de varianza explicada**
- [ ] Ejemplo: "Mantenemos 95% de varianza con 15 componentes (de 50 originales)"
- [ ] Se explica brevemente por qué se usa PCA (evitar ruido, reducir dimensiones)
- [ ] La matriz post-PCA es la que se pasa a los modelos

---

## ✓ Modelos de Clustering

### KMeans
- [ ] Se entrena KMeans con k = 3, 4, 5, ..., 10 (o rango elegido)
- [ ] Se calcula **Silhouette Score para cada k** (método real, no manual)
- [ ] Se dibuja el **gráfico del codo** (inercia o silhouette vs. k)
- [ ] Se elige k basándose en el codo o silueta máxima
- [ ] Se entrena el modelo final con el k elegido
- [ ] Se reporta el silhouette score del modelo final
- [ ] Se verifica que el modelo fue entrenado correctamente (sin errores)

### Clustering Jerárquico
- [ ] Se entrena un modelo jerárquico (Agglomerative)
- [ ] Se dibuja el **dendrograma**
- [ ] Se explica a qué altura se hace el corte (número de clusters)
- [ ] Se reporta el número de clusters resultante
- [ ] Se calcula silhouette score del modelo
- [ ] Se verifica que el modelo fue entrenado correctamente

### DBSCAN
- [ ] Se entrena DBSCAN con parámetros `eps` y `min_samples` justificados
- [ ] Se reporta el **número de clusters encontrados**
- [ ] Se reporta el **número de puntos de ruido**
- [ ] Se calcula silhouette score (cuidado: DBSCAN puede ser problemático para esto)
- [ ] Se explica si DBSCAN es adecuado para este dataset
- [ ] Se verifica que el modelo fue entrenado correctamente

### (Opcional) BIRCH u Otro Modelo
- [ ] Si se implementa, está correctamente entrenado
- [ ] Se reportan métricas equivalentes
- [ ] Se incluye en la comparativa

---

## ✓ Resultados y Visualizaciones

### Gráficos Obligatorios
- [ ] **Gráfico de codo** (KMeans: inercia o silhouette vs. k)
- [ ] **Gráfico de silueta** (por modelo o modelos seleccionados)
- [ ] **Dendrograma** (Clustering Jerárquico)
- [ ] **Tabla comparativa** (modelos, k, silhouette, interpretabilidad)
- [ ] Todos tienen etiquetas claras (ejes, título)
- [ ] Todos son legibles (tamaño, colores)

### Explicación de Resultados
- [ ] Se explica por qué se elige el modelo final (vs. otros)
- [ ] La explicación es clara y concisa (máx. 5 líneas)
- [ ] Se menciona alguna métrica que respalda la decisión
- [ ] Se reconoce si hay trade-offs (e.g., "DBSCAN encontró 7 clusters pero 200 puntos ruido")

---

## ✓ Recomendador Final

### Búsqueda de s5485
- [ ] Se busca `show_id = 's5485'` en el dataset
- [ ] Se verifica que existe: `assert 's5485' in df.index` (o similar)
- [ ] Se verifica que es Movie: `assert df.loc['s5485', 'type'] == 'Movie'`

### Búsqueda de Vecinos
- [ ] Se usa `NearestNeighbors` u otro método equivalente
- [ ] Se buscan los vecinos más cercanos en el espacio de clustering
- [ ] Se retornan más de 10 (ej. 15) para luego filtrar
- [ ] Se filtra correctamente para que todos sean `type == 'Movie'`
- [ ] Se retienen exactamente **10 películas**

### Formato de Salida
- [ ] El resultado es un DataFrame o tabla
- [ ] Columnas: `show_id` e `title` (mínimo)
- [ ] Cada fila es una película recomendada
- [ ] Total de 10 filas
- [ ] Sin duplicados (no se recomienda la misma película dos veces)

### Verificación Final
```python
# Verificación automática
resultado = recomendador('s5485', k=10)
assert len(resultado) == 10
assert all(resultado['type'] == 'Movie')
print("✅ Recomendador correcto")
```

---

## ✓ Documentación y Estructura

### Estructura del Notebook
- [ ] **Sección 1: Objetivo** - Qué se va a hacer
- [ ] **Sección 2: AED** - Análisis del dataset
- [ ] **Sección 3: Preprocesamiento** - Limpieza e ingeniería
- [ ] **Sección 4: Modelos** - Entrenamiento y evaluación
- [ ] **Sección 5: Visualizaciones** - Gráficos y tabla comparativa
- [ ] **Sección 6: Recomendador** - Implementación y prueba
- [ ] **Sección 7: Conclusiones** - Reflexión y referencias

### Explicaciones
- [ ] Cada celda markdown explica qué hace la siguiente celda
- [ ] Las explicaciones están en **español**
- [ ] Las explicaciones son simples y directas
- [ ] Se usan comentarios en el código (`# Esto es...`)

### Ejecución
- [ ] El notebook corre de arriba a abajo sin errores
- [ ] Todas las librerías están importadas al inicio
- [ ] No hay referencias a variables no definidas
- [ ] Los gráficos se visualizan correctamente

---

## ✓ Fuentes y Referencias

- [ ] Se cita el dataset (Kaggle Netflix Titles)
- [ ] Se mencionan librerías usadas (scikit-learn, pandas, etc.)
- [ ] Si se inspira en tutoriales, se referencia el URL
- [ ] No hay plagio; el código es propio (o claramente marcado como referencia)

---

## Puntuación Rápida

**Usa esta escala para auto-evaluación:**

| Sección | Completitud | Calidad |
|---------|-------------|---------|
| AED | 0-3 | A B C |
| Preprocesamiento | 0-5 | A B C |
| Modelos | 0-3 | A B C |
| Visualizaciones | 0-3 | A B C |
| Recomendador | 0-1 | A B C |
| Documentación | 0-2 | A B C |

*Escala:* A = Excelente, B = Bueno, C = Necesita mejora

---

## Última Verificación Antes de Entregar

- [ ] ¿El código corre sin errores?
- [ ] ¿El recomendador retorna exactamente 10 películas?
- [ ] ¿Todas son de tipo Movie?
- [ ] ¿Se explica cada decisión principal?
- [ ] ¿Hay al menos 3 modelos comparados?
- [ ] ¿Hay gráficos que apoyen la explicación?
- [ ] ¿El show_id se mantiene recuperable?
- [ ] ¿No hay valores hardcodeados (métricas calculadas realmente)?

**Si respondiste SÍ a todas:** ¡Listo para entregar! ✅

