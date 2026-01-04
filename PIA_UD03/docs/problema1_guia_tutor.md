# Guía del Tutor - Problema 1 Netflix

## Resumen para el Tutor

Este documento orienta sobre cómo evaluar el Problema 1 y qué buscar en una solución correcta.

---

## Puntos Clave de Evaluación

### 1. AED y Coherencia de Datos

**¿Qué buscar?**
- ¿Se explora correctamente el dataset? (`info()`, `head()`, nulos, cardinalidad)
- ¿Se identifica que s5485 existe y es Movie?
- ¿Hay al menos un gráfico que aporte insights?

**Errores comunes:**
- Exploración superficial sin análisis de nulos
- No verificar que s5485 es efectivamente Movie
- Gráficos decorativos sin relación con el análisis

---

### 2. Preprocesamiento: El "Hueso" de la Tarea

**Estrategia esperada:**

1. **Manejo de nulos:**
   - Rellenar `cast` y `director` con "Unknown" (no borrar filas)
   - Justificación: conservar otras características del registro

2. **Ingeniería de features:**
   - `num_cast`: contar actores (e.g., "Actor1, Actor2, Actor3" → 3)
   - Opcional: `lead_actor_name` (primer actor, para consultas posteriores)

3. **One-Hot Encoding:**
   - `listed_in` → géneros separados (Drama, Action, Comedy, etc.)
   - Cada género es una columna booleana (0 o 1)

4. **Eliminación de ruido:**
   - Descartar `title` (es lo que queremos recomendar, no una feature)
   - Descartar `description` (requeriría NLP, fuera del alcance)
   - Descartar `director` (demasiados valores únicos, > 4000)
   - Descartar `country` (demasiados valores únicos)

5. **Escalado:**
   - `StandardScaler` sobre todas las features numéricas
   - **Después** del One-Hot Encoding

6. **PCA (reducción dimensional):**
   - Objetivo: reducir dimensionalidad sin perder mucha información
   - Reportar: varianza explicada (e.g., "95% con 10 componentes")
   - Explicación simple: "Combinamos features para evitar ruido"

**¿Qué NO hacer?**
- No duplicar preprocesamiento (no procesar dos veces)
- No hardcodear números (e.g., "silhouette = 0.52" sin calcular)
- No perder `show_id` (mantenerlo como índice)

---

### 3. Modelos: Comparativa Técnica

#### KMeans

**Expectativas:**
- Método del codo: gráfico de inercia vs. k (k = 3 a 10)
- Silhouette Score calculado con `silhouette_score()` de sklearn
- Decisión razonada: "Elijo k=5 porque el codo es aquí" o "el silhouette es máximo"
- **NO acepta:** "silhouette de mi modelo es 0.52" sin mostrar código

#### Clustering Jerárquico

**Expectativas:**
- Dendrograma visualizado (altura de corte clara)
- Si se prueba `linkage` (ward, complete, average), explicar diferencia
- Número de clusters elegido desde el dendrograma

#### DBSCAN

**Expectativas:**
- Parámetros `eps` y `min_samples` justificados
- Reporte: "encontré X clusters y Y puntos de ruido"
- Análisis: ¿es DBSCAN adecuado aquí? (cluster globular vs. DBSCAN basado en densidad)

---

### 4. Resultados: Visualización y Justificación

**Tabla resumen esperada:**

| Modelo | K/Clusters | Silhouette | Interpretabilidad | Recomendación |
|--------|-----------|------------|-------------------|---------------|
| KMeans | 5 | 0.62 | Alta | ✓ Elegido |
| Jerárquico | 5 | 0.58 | Media | - |
| DBSCAN | 7 + ruido | 0.55 | Baja | - |

**¿Qué buscar?**
- Gráficos que apoyen decisiones (codo, silueta, dendrograma)
- Explicación de por qué se elige un modelo sobre otros
- Coherencia entre análisis y conclusión

---

### 5. Recomendador Final: El "Producto"

**Prueba:**

```python
# Entrada
show_id_target = 's5485'

# Salida
# Debe ser un DataFrame con exactamente 10 películas
# Columnas: show_id, title
# Todas deben ser type='Movie' (NO series)
```

**Verificaciones:**
- ¿s5485 existe en el dataset?
- ¿Es Movie o TV Show?
- ¿El recomendador retorna exactamente 10 películas?
- ¿Todas son de tipo Movie?
- ¿El método es coherente con el modelo elegido?

**Típico error:** Filtro incorrecto que deja series en los resultados.

---

## Rúbrica Resumen para Calificación

| Criterio | Excelente (90-100) | Bueno (75-89) | Aceptable (60-74) | Deficiente (<60) |
|----------|-------------------|--------------|------------------|------------------|
| **AED** | Análisis completo, gráficos claros, todas las preguntas contestadas | Análisis casi completo, 1-2 gráficos, faltan detalles | AED básico, pocos gráficos | AED incompleto, sin gráficos |
| **Preprocesamiento** | Pipeline coherente, ingeniería clara, sin duplicados, justificado | Pipeline claro, algún duplicado menor, casi justificado | Preprocesamiento básico, algunos duplicados | Preprocesamiento desordenado, confuso |
| **Modelos** | 3+ modelos bien implementados, métricas reales, comparativa clara | 3 modelos implementados, métricas calculadas, comparativa buena | 2-3 modelos, métricas parcialmente reales | <2 modelos o métodos incompletos |
| **Visualizaciones** | 4+ gráficos informativos, tabla resumen clara | 3-4 gráficos, tabla presente | 2-3 gráficos, tabla mínima | <2 gráficos, sin tabla |
| **Recomendador** | 10 películas exactas, todas Movie, método coherente | 10 películas, casi todas Movie, método claro | 10 películas, algunas series, método unclear | <10 o muchas series |
| **Conclusión** | Justificación clara, reflexión profunda, futuro | Justificación presente, reflexión básica | Conclusión superficial | Sin conclusión |

---

## Checklist para la Retroalimentación

- [ ] ¿El pipeline de preprocesamiento es coherente?
- [ ] ¿Se usaron métricas reales (no hardcodeadas)?
- [ ] ¿Se comparan al menos 3 modelos?
- [ ] ¿El recomendador filtra correctamente (solo Movies)?
- [ ] ¿La justificación del modelo elegido es clara?
- [ ] ¿El show_id s5485 se usa correctamente?

---

## Ejemplos de Retroalimentación

### Positiva
*"Excelente pipeline. Veo que detectaste la cardinalidad alta de directores y decidiste descartarla. El KMeans con k=5 está bien justificado desde el codo. El recomendador filtra correctamente."*

### Constructiva
*"El preprocesamiento está bien, pero veo que escalaste antes de PCA. Recuerda que PCA ya captura varianza; escalar primero ayuda. También me gustaría ver cálculos reales de silhouette, no aproximaciones manuales."*

---

## Notas Finales

1. **Flexibilidad:** No existe una solución "única correcta". Acepta variaciones razonadas (e.g., k=4 vs. k=5 si están ambas justificadas).

2. **Énfasis en coherencia:** Lo importante es que el estudiante entienda POR QUÉ hace cada paso, no solo QUE lo hace.

3. **Documentación:** La claridad de explicaciones vale casi tanto como el código correcto.

