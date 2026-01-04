# Problema 1: Sistema de Recomendación Netflix

## Enunciado

Desarrollar un **sistema de recomendación de películas** basado en técnicas de clustering no supervisado utilizando el dataset de Netflix Titles de Kaggle.

**Objetivo específico:**  
Recomendar **exactamente 10 películas** similares a un título dado (en este caso, `show_id: s5485`), utilizando múltiples algoritmos de clustering y elegir el más adecuado para realizar las recomendaciones.

---

## Contexto

- **Dataset:** Netflix Titles (~8,800 títulos)
- **Columnas clave:** `show_id`, `type`, `title`, `director`, `cast`, `listed_in` (géneros), `description`, `country`
- **Challenge:** Implementar un pipeline que limpie, prepare y agrupe películas por similitud

---

## Rúbrica de Evaluación

### 1. Análisis Exploratorio de Datos (AED) - 15%

**Criterios:**
- Exploración inicial con `info()` y `head()`
- Análisis de nulos (cantidad y columnas afectadas)
- Análisis de cardinalidad (valores únicos)
- Al menos **1 gráfico** ilustrativo (histogramas, conteos, distribuciones)
- Identificación de columnas problemáticas (`listed_in`, `cast`, `director` como listas)
- Verificación de que el show_id objetivo existe y es Movie

**Puntuación:** Completo AED + gráficos claros = 15/15

---

### 2. Preprocesamiento e Ingeniería de Características - 25%

**Criterios de coherencia:**

| Tarea | Descripción | Peso |
|-------|-------------|------|
| Manejo de nulos | Rellenar con "Unknown" (no borrar filas) | 5% |
| Ingeniería de cast | Crear `num_cast` (contar actores) y opcional `lead_actor_name` | 5% |
| One-Hot Encoding | Separar géneros en `listed_in` con `get_dummies()` | 5% |
| Eliminación de ruido | Descartar `title`, `description`, `director`, `country` | 5% |
| Escalado | `StandardScaler` antes de clustering | 3% |
| PCA | Reducción dimensional con explicación de varianza | 2% |

**Nota importante:** Un pipeline limpio (sin duplicación). El preprocesamiento debe ser coherente de inicio a fin.

---

### 3. Modelos de Clustering - 35%

Se requiere implementar y evaluar **al menos 3 modelos:**

#### 3.1 KMeans (Obligatorio)
- [ ] Determinación del número óptimo de clusters (**método del codo**)
- [ ] Cálculo de **Silhouette Score** (valor real, no manual)
- [ ] Justificación del k elegido
- [ ] **Puntuación:** 12/35

#### 3.2 Clustering Jerárquico (Obligatorio)
- [ ] Dendrograma visualizado
- [ ] Selección del número de clusters desde el dendrograma
- [ ] Explicación del linkage utilizado (si se prueba más de uno)
- [ ] **Puntuación:** 12/35

#### 3.3 DBSCAN (Obligatorio)
- [ ] Justificación de parámetros (`eps`, `min_samples`)
- [ ] Reporte de clusters encontrados y puntos de ruido
- [ ] Análisis de si es adecuado para este dataset
- [ ] **Puntuación:** 11/35

#### 3.4 (Opcional) BIRCH u otro modelo
- Si se incluye, suma puntos extras (+2%)

---

### 4. Resultados y Visualizaciones - 15%

**Obligatorio:**
- [ ] Gráfico de codo (KMeans)
- [ ] Gráfico de Silhouette Score
- [ ] Dendrograma (Jerárquico)
- [ ] Tabla comparativa de modelos (clusters, silhouette, interpretabilidad)
- [ ] Explicación de por qué se elige el modelo final

**Puntuación:** Visualizaciones claras + explicación coherente = 15/15

---

### 5. Recomendador Final - 10%

**Requisitos:**

```python
# Entrada
show_id_target = 's5485'

# Salida esperada
# DataFrame con 10 películas, formato:
# | show_id | title |
# |---------|-------|
# | s5486   | ...   |
# | s5487   | ...   |
# ...
```

**Criterios:**
- [ ] Busca la película objetivo (s5485)
- [ ] Encuentra los 10 vecinos más cercanos en el espacio de clustering
- [ ] **Filtra SOLO películas** (type == 'Movie')
- [ ] Muestra `show_id` e `title` de cada recomendación
- [ ] Explica brevemente por qué se considera "similar"

**Puntuación:** 
- Exactamente 10 películas, todas Movie: 8/10
- Método coherente con el modelo elegido: 2/10

---

## Total: 100%

| Sección | Puntos |
|---------|--------|
| AED | 15 |
| Preprocesamiento | 25 |
| Modelos | 35 |
| Visualizaciones | 15 |
| Recomendador | 10 |
| **Total** | **100** |

---

## Notas Importantes

1. **show_id como índice:** Establece `show_id` como índice desde el AED. Esto evita que interfiera en cálculos y facilita recuperar títulos.

2. **Un solo pipeline:** Define claramente dónde comienza y termina el preprocesamiento. Evita procesar dos veces las mismas columnas.

3. **Valores reales, no manuales:** Silhouette scores, conteos de clusters, etc., deben calcularse automáticamente del modelo, no hardcodeados.

4. **Coherencia técnica:** Todos los modelos deben recibir el mismo conjunto de características (post-PCA, escaladas).

5. **Justificación:** Cada decisión (qué columnas eliminar, qué k elegir, etc.) debe estar razonada.

---

## Referencias

- **Dataset:** [Netflix Titles - Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Scikit-Learn Documentation:** Clustering, PCA, StandardScaler, Silhouette Score
- **Unidad 3 PIA:** Aprendizaje No Supervisado

