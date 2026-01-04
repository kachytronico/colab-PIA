---
description: "PIA UD03 - Problema 1 Netflix: Recomendador de películas por clustering"
applyTo: "**/*"
---

# Objetivo Principal
Implementar un **sistema de recomendación de películas Netflix** basado en clustering no supervisado.

**Requisito específico:** Recomendar EXACTAMENTE **10 películas similares** al `show_id: s5485`, filtrando solo películas (Movie), no series.

---

## Contexto del Proyecto

**Dataset:** Netflix Titles (Kaggle - 8807 registros)
**Alumno:** Alfredo Ledesma Ruiz
**Módulo:** PIA - Unidad 3 (Aprendizaje No Supervisado)

---

## Requisitos de la Rúbrica (Problema 1)

### 1. Análisis Exploratorio de Datos (AED) ✓
- [ ] `info()` del dataset original
- [ ] `head()` para ver primeras filas
- [ ] Conteo de nulos (análisis de calidad)
- [ ] Análisis de valores únicos y cardinalidad (especialmente `director`, `listed_in`, `cast`)
- [ ] Al menos **1 gráfico** para ilustrar distribución o características
- [ ] Verificación de que `show_id` s5485 existe y es Movie

### 2. Preprocesamiento e Ingeniería de Características ✓
- [ ] **Manejo de nulos:** Rellenar `cast` y `director` con "Unknown" (no borrar filas)
- [ ] **Ingeniería de Cast:**
  - `num_cast`: contar actores (numérico)
  - `lead_actor_name`: primer actor (opcional, solo consulta)
- [ ] **Géneros (listed_in):** One-Hot Encoding con `get_dummies()`
- [ ] **Tipo (type):** Encoding de Movie/TV Show (o descartar antes de scalado)
- [ ] **Eliminación de ruido:** Borrar `title`, `description`, `director`, `country` (no mejoran clustering)
- [ ] **Escalado:** `StandardScaler` antes de clustering
- [ ] **PCA (reducción dimensional):** Explicar varianza explicada (e.g., 95%)
- [ ] **Coherencia:** UN SOLO pipeline limpio (no duplicados)

### 3. Modelos de Clustering ✓
Se deben entrenar y evaluar al menos 3 modelos:
- [ ] **KMeans:** 
  - Cálculo del número óptimo de clusters (método del codo)
  - Silhouette Score **calculado real**, no hardcodeado
  - Explicación de por qué se elige ese k
- [ ] **Clustering Jerárquico (Agglomerative):**
  - Dendrograma visualizado
  - Distinción entre linkage methods (si aplica)
- [ ] **DBSCAN:**
  - Explicación de eps y min_samples
  - Número de clusters y puntos de ruido reportados
- [ ] **(Opcional) BIRCH:** Si se implementa, incluir en evaluación

### 4. Resultados y Visualizaciones ✓
- [ ] **Gráfico de codo** (KMeans)
- [ ] **Silueta score** por modelo (gráfico o tabla)
- [ ] **Dendrograma** (Jerárquico)
- [ ] **Comparativa de modelos** (tabla resumen)
- [ ] Explicación clara de **por qué se elige el modelo final** para recomendar

### 5. Recomendador Final ✓
- [ ] **Entrada:** `show_id = 's5485'`
- [ ] **Búsqueda:** encontrar punto más cercano en el modelo elegido
- [ ] **Retorno:** exactamente **10 películas** (no series)
- [ ] **Salida:** DataFrame con `show_id` e `title` visible
- [ ] **Verificación:** todos sean tipo Movie

### 6. Conclusiones y Referencias ✓
- [ ] Explicación breve del método elegido
- [ ] Reflexión sobre similitud y recomendaciones
- [ ] **Citas:** Dataset (Kaggle), scikit-learn, si aplica

---

## Checklist de Coherencia Técnica

### Preprocesamiento
- [ ] `show_id` es índice desde el inicio (se mantiene recuperable)
- [ ] No hay preprocesamiento duplicado (un solo bloque coherente)
- [ ] Nulos tratados de forma consistente
- [ ] Escalado aplicado DESPUÉS de One-Hot Encoding
- [ ] PCA aplicado sobre datos escalados

### Modelos
- [ ] Todos los modelos reciben la MISMA matriz de características (post-PCA/escalado)
- [ ] Silhouette scores son **cálculos reales** (no valores manuales)
- [ ] No hay hardcoding de métricas o constantes "mágicas"
- [ ] Nombres y parámetros coherentes con documentación sklearn

### Recomendador
- [ ] Usa NearestNeighbors o búsqueda equivalente
- [ ] Filtra SOLO Movie (type == 'Movie')
- [ ] Retorna exactamente 10 resultados
- [ ] show_id es recuperable como índice o columna

---

## Directrices de Estilo

### Código
- **Indentación:** 2 espacios (Python/YAML)
- **Variables:** snake_case (`num_cast`, `lead_actor_name`, `df_clean`)
- **Claridad:** comentarios en español, simples y directos
- **Documentación:** Explicación de cada sección antes de ejecutarla

### Escritura
- Explicaciones en **español**, nivel comprensible
- Si propones cambios de código: proporciona el **bloque exacto** y dónde insertarlo
- Evita refactors masivos; prefiere mejoras mínimas y coherentes

---

## Prompts Recomendados para Copilot

1. **Revisión rápida:** "Revisa si cumplo la rúbrica. Checklist de lo que está bien y qué falta."
2. **Arreglo 10 películas:** "Quiero recomendar exactamente 10 PELÍCULAS (no series). ¿Cuál es el cambio mínimo?"
3. **Coherencia de preprocesado:** "¿Tengo preprocesamiento duplicado? Dime qué conservar."
4. **Valores hardcodeados:** "Busca silhouette u otros valores a mano. Cámbialos por cálculo real."
5. **Estructura del notebook:** "Reorganiza en secciones (Objetivo → AED → Preproceso → Modelos → Resultados → Recomendador → Conclusión)."

---

## Notas Importantes

- **No borres filas con nulos:** Solo rellena con "Unknown" o calcula variables derivadas.
- **Mantén show_id como índice:** Fundamental para recuperar títulos al final.
- **Un solo pipeline:** Evita procesar dos veces. Define claramente dónde comienza y termina.
- **Prueba con s5485:** Verifica que exista, sea Movie, y que el recomendador devuelva 10 películas.
- **Justifica cada decisión:** ¿Por qué ese k de clusters? ¿Por qué ese modelo? Explica brevemente.