# 📚 Resumen de Estudio - Clustering y Aprendizaje No Supervisado
**Alumno:** Alfredo Ledesma Ruiz  
**Tarea:** PIA UD03 - Sistema de Recomendación Netflix  
**Propósito:** Resumen para preparación de examen

---

## 📖 Índice
1. [Aprendizaje No Supervisado](#1-aprendizaje-no-supervisado)
2. [Preprocesamiento de Datos](#2-preprocesamiento-de-datos)
3. [Reducción de Dimensionalidad (PCA)](#3-reducción-de-dimensionalidad-pca)
4. [Algoritmos de Clustering](#4-algoritmos-de-clustering)
5. [Métricas de Evaluación](#5-métricas-de-evaluación)
6. [Sistema de Recomendación](#6-sistema-de-recomendación)
7. [Fórmulas y Conceptos Clave](#7-fórmulas-y-conceptos-clave)
8. [Buenas Prácticas](#8-buenas-prácticas)

---

## 1. Aprendizaje No Supervisado

### ¿Qué es?
- **Definición:** Técnica de machine learning donde el algoritmo aprende patrones en datos **sin etiquetas previas**.
- **Objetivo:** Descubrir estructuras ocultas, agrupar datos similares, reducir dimensionalidad.

### Diferencia con Aprendizaje Supervisado
| Supervisado | No Supervisado |
|-------------|----------------|
| Datos con etiquetas (y conocida) | Datos sin etiquetas |
| Predicción/Clasificación | Descubrimiento de patrones |
| Ejemplo: Spam/No spam | Ejemplo: Agrupar clientes similares |

### Tipos principales
1. **Clustering:** Agrupar datos similares
2. **Reducción de dimensionalidad:** Simplificar datos manteniendo información
3. **Detección de anomalías:** Encontrar datos atípicos

---

## 2. Preprocesamiento de Datos

### 2.1 Análisis Exploratorio de Datos (AED)

**Pasos aplicados:**
```python
# 1. Información básica
df.info()           # Tipos de datos, nulos
df.head()           # Primeras filas
df.describe()       # Estadísticas básicas

# 2. Análisis de nulos
df.isnull().sum()   # Contar nulos por columna

# 3. Cardinalidad (valores únicos)
df['columna'].nunique()
```

**Decisiones tomadas:**
- ✅ Rellenar nulos con "Unknown" (no borrar filas)
- ✅ Identificar columnas de alta cardinalidad (director: 4500+ valores únicos)
- ✅ Detectar listas dentro de columnas (géneros separados por comas)

### 2.2 Ingeniería de Características

**Técnicas aplicadas:**

#### A) One-Hot Encoding (variables categóricas)
```python
# Para géneros (multi-etiqueta)
generos = df['listed_in'].str.get_dummies(sep=', ')
# Resultado: columnas binarias (0/1) por cada género
```

**Cuándo usar:**
- Variables categóricas sin orden
- Múltiples valores por registro (multi-hot)

**Ventaja:** El algoritmo entiende categorías como números  
**Desventaja:** Aumenta dimensionalidad (muchas columnas nuevas)

#### B) Frequency Encoding (alta cardinalidad)
```python
# Para actores (4500+ actores únicos)
actor_counts = df['lead_actor'].value_counts()
df['lead_actor_freq'] = df['lead_actor'].map(actor_counts)
```

**Cuándo usar:**
- Alta cardinalidad (evita "explosión" de columnas)
- La frecuencia es informativa (actores estrella)

#### C) Feature Engineering numérico
```python
# Crear nueva variable: cantidad de actores
df['num_cast'] = df['cast'].apply(lambda x: len(x.split(',')))
```

**Ventaja:** Captura información sin aumentar mucho la dimensionalidad

### 2.3 Escalado de Datos

**StandardScaler (estandarización):**
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
```

**Fórmula:**
```
z = (x - μ) / σ
```
- μ = media
- σ = desviación estándar
- Resultado: media = 0, desviación = 1

**¿Por qué es necesario?**
- KMeans usa distancias euclidianas
- Sin escalar: variables con rangos grandes dominan
- Ejemplo: `release_year` (1900-2020) vs `is_tv_show` (0-1)

**¡IMPORTANTE!** Siempre escalar **antes** de PCA y clustering.

---

## 3. Reducción de Dimensionalidad (PCA)

### ¿Qué es PCA?
**Principal Component Analysis (Análisis de Componentes Principales)**

- Técnica para reducir número de variables (columnas)
- Mantiene la máxima información posible
- Crea nuevas variables (componentes principales) que son combinaciones lineales de las originales

### ¿Cómo funciona?
1. Encuentra la dirección de mayor varianza en los datos
2. Proyecta los datos en esa dirección (componente principal 1)
3. Encuentra la siguiente dirección perpendicular con mayor varianza (componente 2)
4. Repite hasta tener tantos componentes como se necesite

### Implementación
```python
from sklearn.decomposition import PCA

# Mantener 90% de la varianza
pca = PCA(n_components=0.90)
df_pca = pca.fit_transform(df_scaled)

# Ver varianza explicada
print(f"Varianza explicada: {pca.explained_variance_ratio_.sum()}")
```

**En nuestra tarea:**
- Entrada: 46 columnas
- Salida: 35 componentes principales
- Varianza conservada: 91.43%

### Ventajas de PCA
✅ Reduce "maldición de la dimensionalidad"  
✅ Elimina ruido y correlaciones  
✅ Acelera algoritmos (menos columnas)  
✅ Mejora visualización (2D o 3D)

### Desventajas
❌ Componentes principales no son interpretables (combinaciones matemáticas)  
❌ Pierde algo de información

---

## 4. Algoritmos de Clustering

### 4.1 K-Means

**Concepto:**
- Algoritmo de partición
- Divide datos en K grupos (clusters)
- Cada cluster tiene un **centroide** (centro)

**Cómo funciona:**
1. Elige K puntos aleatorios como centroides iniciales
2. Asigna cada punto al centroide más cercano
3. Recalcula centroides (promedio de puntos asignados)
4. Repite pasos 2-3 hasta convergencia

**Implementación:**
```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=32, random_state=42, n_init=10)
kmeans.fit(df_pca)
labels = kmeans.labels_  # Etiquetas de cluster por cada punto
```

**Parámetros importantes:**
- `n_clusters`: Número de grupos (K)
- `random_state`: Semilla para reproducibilidad
- `n_init`: Número de inicializaciones (elige la mejor)

**Ventajas:**
✅ Rápido y eficiente  
✅ Escalable a grandes datos  
✅ Centroides interpretables  

**Desventajas:**
❌ Hay que elegir K manualmente  
❌ Sensible a inicialización  
❌ Asume clusters esféricos (forma circular)  
❌ Sensible a outliers

**Método del Codo:**
```python
# Probar diferentes valores de K
for k in range(2, 64):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    inercia.append(kmeans.inertia_)  # Suma de distancias al centroide

# Graficar y buscar el "codo" (donde la curva se aplana)
```

### 4.2 Agrupamiento Jerárquico (Agglomerative)

**Concepto:**
- Construye una jerarquía de clusters
- **Enfoque bottom-up:** Empieza con cada punto como cluster y va fusionando

**Cómo funciona:**
1. Cada punto es un cluster individual
2. Fusiona los 2 clusters más cercanos
3. Repite hasta tener K clusters (o uno solo)

**Implementación:**
```python
from sklearn.cluster import AgglomerativeClustering

jerarquico = AgglomerativeClustering(n_clusters=32)
labels = jerarquico.fit_predict(df_pca)
```

**Visualización: Dendrograma**
```python
from scipy.cluster.hierarchy import dendrogram, linkage

Z = linkage(data, method='ward')
dendrogram(Z)
```

**Métodos de enlace (linkage):**
- `ward`: Minimiza varianza (el usado en nuestra tarea)
- `single`: Distancia mínima entre clusters
- `complete`: Distancia máxima entre clusters
- `average`: Distancia promedio entre clusters

**Ventajas:**
✅ No requiere especificar K de antemano  
✅ Genera dendrograma (visualización útil)  
✅ Mejor con clusters no esféricos  

**Desventajas:**
❌ Más lento que K-Means  
❌ No escalable a muchos datos  
❌ Decisiones irreversibles (no puede "desfusionar")

### 4.3 DBSCAN (Density-Based Spatial Clustering)

**Concepto:**
- Clustering basado en **densidad**
- No requiere especificar K
- Detecta **outliers** (puntos de ruido)

**Cómo funciona:**
1. Define un radio `eps` alrededor de cada punto
2. Si hay `min_samples` puntos dentro del radio → punto **core**
3. Puntos alcanzables desde core → mismo cluster
4. Puntos aislados → **ruido** (etiqueta -1)

**Implementación:**
```python
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=3, min_samples=5)
labels = dbscan.fit_predict(df_pca)

# Contar ruido
n_noise = list(labels).count(-1)
```

**Parámetros:**
- `eps`: Radio de vecindad (distancia máxima)
- `min_samples`: Mínimo de puntos para formar cluster

**Ventajas:**
✅ No requiere K  
✅ Detecta clusters de forma arbitraria  
✅ Identifica outliers  

**Desventajas:**
❌ Difícil elegir `eps` y `min_samples`  
❌ No funciona bien en alta dimensionalidad  
❌ Problemas con densidades variables

**En nuestra tarea:**
- Generó 121 clusters (demasiada fragmentación)
- Por eso se descartó

### 4.4 BIRCH (Modelo Opcional)

**Concepto:**
- **B**alanced **I**terative **R**educing and **C**lustering using **H**ierarchies
- Diseñado para grandes datasets
- Construye un árbol de características (CF Tree)

**Implementación:**
```python
from sklearn.cluster import Birch

birch = Birch(n_clusters=32)
labels = birch.fit_predict(df_pca)
```

**Ventajas:**
✅ Muy eficiente en memoria  
✅ Maneja grandes volúmenes de datos  

**Desventajas:**
❌ Solo funciona con distancia euclidiana  
❌ Sensible a orden de datos

---

## 5. Métricas de Evaluación

### 5.1 Coeficiente de Silueta (Silhouette Score)

**¿Qué mide?**
- Calidad del clustering
- Qué tan bien está un punto en su cluster vs otros clusters

**Fórmula:**
```
s(i) = (b(i) - a(i)) / max(a(i), b(i))
```
- `a(i)`: Distancia promedio al resto de puntos **en su cluster**
- `b(i)`: Distancia promedio al cluster **más cercano**

**Rango de valores:**
- **+1**: Punto perfectamente asignado
- **0**: Punto en el borde entre clusters
- **-1**: Punto mal asignado

**Implementación:**
```python
from sklearn.metrics import silhouette_score

score = silhouette_score(data, labels)
print(f"Silueta: {score:.4f}")
```

**Interpretación:**
- 0.7 - 1.0: Excelente
- 0.5 - 0.7: Buena estructura
- 0.25 - 0.5: Estructura débil pero razonable
- < 0.25: No hay estructura clara

**En nuestra tarea:**
- Jerárquico: 0.4397 (mejor)
- K-Means: 0.4095 (segundo)
- DBSCAN: 0.4026
- BIRCH: 0.3236

### 5.2 Inercia (Inertia)

**¿Qué mide?**
- Compactación de clusters
- Suma de distancias al cuadrado de cada punto a su centroide

**Fórmula:**
```
Inercia = Σ(distancia(punto_i, centroide_cluster_i)²)
```

**Características:**
- Siempre disminuye al aumentar K
- Se usa en el **método del codo**

**Interpretación:**
- Valores bajos = clusters compactos
- Buscar el "codo" donde deja de bajar significativamente

---

## 6. Sistema de Recomendación

### 6.1 K-Nearest Neighbors (KNN)

**Concepto:**
- Encuentra los K puntos más cercanos a un punto dado
- Usa distancias (euclidiana, Manhattan, etc.)

**Implementación:**
```python
from sklearn.neighbors import NearestNeighbors

# 1. Crear modelo
nn = NearestNeighbors(n_neighbors=11, metric='euclidean')

# 2. Entrenar con datos del cluster
nn.fit(datos_cluster)

# 3. Buscar vecinos
distancias, indices = nn.kneighbors(punto_objetivo)
```

**Estrategia en nuestra tarea:**
1. **Filtrar por cluster:** Solo películas del mismo cluster que el objetivo
2. **Filtrar por tipo:** Solo Movies (no TV Shows)
3. **KNN:** Buscar las 10 más cercanas en distancia euclidiana

**Distancia Euclidiana:**
```
d = √[(x₁-x₂)² + (y₁-y₂)² + ... + (xₙ-yₙ)²]
```

### 6.2 Ventajas de clustering + KNN
✅ Reduce espacio de búsqueda (más rápido)  
✅ Agrupa películas similares primero  
✅ KNN solo busca dentro del cluster (más preciso)

---

## 7. Fórmulas y Conceptos Clave

### Distancia Euclidiana
```
d(p,q) = √[Σ(pᵢ - qᵢ)²]
```

### Estandarización (StandardScaler)
```
z = (x - μ) / σ
μ = media
σ = desviación estándar
```

### Varianza Explicada (PCA)
```
Varianza explicada = Σ(varianza componentes) / Σ(varianza total)
```

### Coeficiente de Silueta
```
s(i) = (b(i) - a(i)) / max(a(i), b(i))
```

### Inercia (K-Means)
```
J = ΣΣ ||xᵢ - μⱼ||²
```
- xᵢ: punto i
- μⱼ: centroide del cluster j

---

## 8. Buenas Prácticas

### Preprocesamiento
✅ Siempre revisar nulos **antes** de borrar  
✅ Rellenar con "Unknown" mejor que eliminar filas  
✅ Frequency encoding para alta cardinalidad  
✅ One-Hot solo para cardinalidad baja-media  
✅ Escalar **antes** de clustering  

### Selección de K
✅ Usar método del codo (inercia)  
✅ Usar coeficiente de silueta  
✅ Probar potencias de 2 (8, 16, 32, 64)  
✅ Buscar equilibrio: no muy pocos, no demasiados  

### PCA
✅ Aplicar después de escalar  
✅ Mantener 90-95% de varianza  
✅ Documentar cuántos componentes se generan  

### Evaluación
✅ Comparar múltiples algoritmos  
✅ Usar silueta, no solo inercia  
✅ Visualizar resultados (dendrograma, gráficos de barras)  
✅ Justificar elección del modelo  

### Recomendador
✅ Filtrar por cluster primero (eficiencia)  
✅ Aplicar filtros de negocio (tipo Movie)  
✅ Verificar que objetivo exista en datos  
✅ Manejar casos edge (cluster con <10 elementos)  

---

## 9. Términos Clave del Examen

| Término | Definición |
|---------|-----------|
| **Clustering** | Agrupar datos similares sin etiquetas previas |
| **Centroide** | Centro de un cluster (punto promedio) |
| **Inercia** | Suma de distancias al cuadrado dentro de clusters |
| **Silueta** | Métrica de calidad de clustering (-1 a +1) |
| **PCA** | Reducción de dimensionalidad manteniendo varianza |
| **One-Hot Encoding** | Convertir categorías a columnas binarias |
| **Escalado** | Normalizar datos a misma escala |
| **Dendrograma** | Árbol jerárquico de fusiones de clusters |
| **Outlier** | Punto atípico, alejado del resto |
| **KNN** | Algoritmo de vecinos más cercanos |
| **Supervised Learning** | Aprendizaje con etiquetas (y conocida) |
| **Unsupervised Learning** | Aprendizaje sin etiquetas (descubrir patrones) |
| **Feature Engineering** | Crear nuevas variables a partir de datos |
| **High Cardinality** | Muchos valores únicos en una columna |
| **Curse of Dimensionality** | Problemas con muchas dimensiones |

---

## 10. Preguntas Típicas de Examen

### 1. ¿Cuándo usar K-Means vs Jerárquico?
**K-Means:**
- Datos grandes (millones de registros)
- Necesitas velocidad
- Clusters esféricos

**Jerárquico:**
- Datos pequeños-medianos (<10,000 registros)
- Quieres dendrograma
- Clusters de forma irregular

### 2. ¿Por qué escalar los datos?
Porque algoritmos de clustering usan **distancias**. Sin escalar, variables con rangos grandes dominan el cálculo.

### 3. ¿Qué hace PCA?
Reduce dimensiones creando **nuevas variables (componentes)** que son combinaciones de las originales, manteniendo máxima varianza.

### 4. ¿Cómo elegir K en K-Means?
1. Método del codo (buscar inflexión en gráfico de inercia)
2. Coeficiente de silueta (probar varios K y elegir máximo)
3. Conocimiento del dominio

### 5. ¿Qué indica una silueta de 0.4?
Estructura **razonable** pero no excelente. Los clusters están definidos pero hay cierto solapamiento.

---

## 11. Checklist Pre-Examen

- [ ] Sé explicar qué es aprendizaje no supervisado
- [ ] Conozco la diferencia entre clustering y clasificación
- [ ] Puedo explicar cómo funciona K-Means
- [ ] Entiendo el método del codo
- [ ] Sé qué es el coeficiente de silueta y su rango
- [ ] Puedo explicar para qué sirve PCA
- [ ] Conozco cuándo usar One-Hot vs Frequency Encoding
- [ ] Sé por qué es necesario escalar datos
- [ ] Puedo comparar K-Means vs Jerárquico vs DBSCAN
- [ ] Entiendo qué es un dendrograma
- [ ] Sé explicar distancia euclidiana
- [ ] Conozco ventajas y desventajas de cada algoritmo

---

## 📌 Resumen Ultra-Rápido

**Flujo completo:**
1. **AED** → Entender datos
2. **Preprocesamiento** → Limpiar, codificar, feature engineering
3. **Escalar** → StandardScaler (media 0, std 1)
4. **PCA** → Reducir dimensiones (90% varianza)
5. **Elegir K** → Método del codo + silueta
6. **Clustering** → Probar KMeans, Jerárquico, DBSCAN
7. **Evaluar** → Comparar siluetas
8. **Recomendar** → Filtrar cluster + KNN

**Los 3 algoritmos obligatorios:**
- **K-Means**: Rápido, centroides, K manual
- **Jerárquico**: Dendrograma, no escala, flexible
- **DBSCAN**: Detecta ruido, densidad, difícil ajustar

**Métrica principal:** Coeficiente de Silueta (0 a 1, mayor mejor)

---

**¡Buena suerte en el examen! 🚀**
