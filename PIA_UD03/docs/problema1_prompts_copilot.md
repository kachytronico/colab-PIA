# Prompts Recomendados para Copilot - Problema 1 Netflix

Este documento contiene prompts simples y específicos para pedir ayuda a GitHub Copilot de forma efectiva. Úsalos cuando necesites revisar, arreglar o mejorar tu código.

---

## 1️⃣ Revisión Rápida por Rúbrica

**Situación:** Quieres saber rápidamente qué está bien y qué falta.

```
Revisa este notebook del Problema 1 (Netflix) con la checklist de la rúbrica.
Dime qué está bien y qué falta. No propongas refactors grandes, solo mejoras mínimas.

Usa como referencia:
- AED: info, head, nulos, gráficos, verificar s5485 es Movie
- Preproceso: pipeline único, sin duplicados, 1 nulo, One-Hot de géneros, escalado, PCA
- Modelos: KMeans, Jerárquico, DBSCAN (métricas reales, no manuales)
- Resultados: gráficos de codo/silueta/dendrograma, tabla comparativa, explicación de por qué se elige el modelo
- Recomendador: 10 películas exactas, todas Movie, s5485 debe existir
```

**Lo que conseguirás:** Una lista rápida de qué funciona y qué arreglar.

---

## 2️⃣ Arreglo Mínimo: 10 PELÍCULAS Exactas

**Situación:** Tu recomendador devuelve 10 elementos, pero algunos son series (TV Show).

```
Mi recomendador actualmente retorna 10 elementos, pero algunos son TV Show, no Movie.
Quiero que devuelva exactamente 10 PELÍCULAS (type='Movie') similares a s5485.
Dime el cambio mínimo de código para filtrar solo películas.

Mi filtro actual es: [copia el código que usas para filtrar]

¿Cómo lo arreglo con cambio mínimo?
```

**Lo que conseguirás:** El código exacto para filtrar solo películas.

---

## 3️⃣ Detección de Preprocesamiento Duplicado

**Situación:** Sospechas que preproce sas datos dos veces.

```
Busca en mi notebook si tengo preprocesamiento duplicado.
Es decir, busca dónde:
- Relleño nulos dos veces
- Hago One-Hot Encoding dos veces
- Escalo dos veces

Dime en qué línea/celda aparecen los duplicados.
¿Cuál debo mantener? ¿Cuál debo comentar/eliminar para dejar un solo pipeline?
```

**Lo que conseguirás:** Identificación clara de duplicados y recomendación de cuál conservar.

---

## 4️⃣ Convertir Valores Hardcodeados a Cálculos Reales

**Situación:** Tienes valores "manuales" que no vienen de cálculos.

```
Busca en mi código si hay valores hardcodeados, como:
- silhouette = 0.52 (escrito a mano, sin calcular)
- k = 5 (asignado sin método del codo)
- Cualquier número que no salga de una fórmula

Para cada uno encontrado, dime cómo convertirlo a un cálculo real.
Ejemplo: 
  ANTES: silhouette = 0.52
  DESPUÉS: silhouette = silhouette_score(X_scaled, labels)
```

**Lo que conseguirás:** Código con métricas calculadas automáticamente.

---

## 5️⃣ Reorganizar Estructura del Notebook

**Situación:** Tu notebook está desordenado, sin secciones claras.

```
Reorganiza mi notebook en estas secciones, SIN cambiar la lógica del código:

1. Objetivo
2. Configuración (librerías)
3. AED (análisis exploratorio)
4. Preprocesamiento
5. Modelos (KMeans, Jerárquico, DBSCAN)
6. Visualizaciones
7. Recomendador
8. Conclusiones

Añade títulos claros (markdown) en cada sección, pero mantén el código igual.
```

**Lo que conseguirás:** Estructura clara y legible.

---

## 6️⃣ Agregar Gráfico Faltante

**Situación:** Falta un gráfico (codo, silueta, dendrograma).

```
Tengo entrenado un modelo KMeans con k de 3 a 10.
Calculo silhouette_score para cada k.
Quiero un gráfico que muestre Silhouette vs. k.

Código actual: [copia las líneas donde calculas silhouette para cada k]

Genera el gráfico con matplotlib. Que sea claro, con etiquetas en ejes.
```

**Lo que conseguirás:** Código para visualizar una métrica.

---

## 7️⃣ Verificar que s5485 es Movie

**Situación:** Quieres una verificación automática.

```
Quiero una celda de código que:
1. Verifique que 's5485' existe en el dataset
2. Verifique que su tipo es 'Movie' (no 'TV Show')
3. Si pasa ambas: imprimir "✅ s5485 es una película válida"
4. Si falla: imprimir un error explicativo

Código:
```

**Lo que conseguirás:** Verificación robusta.

---

## 8️⃣ Explicación Breve de por Qué Elegir un Modelo

**Situación:** Necesitas una conclusión coherente.

```
Mis 3 modelos tienen:
- KMeans: silhouette 0.62, k=5
- Jerárquico: silhouette 0.58, k=5
- DBSCAN: silhouette 0.55, 7 clusters + 200 ruido

¿Por qué debo elegir KMeans para hacer recomendaciones?
Dame 3-4 líneas de explicación clara.
```

**Lo que conseguirás:** Justificación clara y concisa.

---

## 9️⃣ Corregir Error en One-Hot Encoding

**Situación:** El One-Hot de géneros tiene un problema.

```
Hago One-Hot Encoding de listed_in con:
[copia tu código]

El problema es: [describe el problema: índices mal, NaN, columnas raras, etc.]

¿Cómo lo corrijo mínimamente?
```

**Lo que conseguirás:** Corrección enfocada.

---

## 🔟 Revisar Pipeline de Preprocesamiento

**Situación:** Quieres verificar que el pipeline sea coherente.

```
Aquí está mi pipeline de preprocesamiento:
1. Cargo df
2. Establecer show_id como índice
3. Rellenar nulos con "Unknown"
4. Crear num_cast
5. One-Hot de listed_in
6. Descartar columnas: title, description, director, country
7. StandardScaler
8. PCA

¿Este orden es coherente? ¿Debo cambiar algo?
¿O está listo para pasar a los modelos?
```

**Lo que conseguirás:** Validación del flujo.

---

## 1️⃣1️⃣ Implementar NearestNeighbors para Recomendador

**Situación:** Necesitas buscar los 10 vecinos más cercanos.

```
Tengo un dataset preprocesado (X_scaled) con 8000 filas.
Tengo un modelo KMeans entrenado (kmeans).
Quiero encontrar las 10 películas más similares a s5485.

Genera código que:
1. Encuentre s5485 en el dataset
2. Use NearestNeighbors para encontrar los 10 vecinos más cercanos
3. Filtre solo películas (type='Movie')
4. Retorne show_id e title
```

**Lo que conseguirás:** Implementación del recomendador.

---

## 1️⃣2️⃣ Crear Tabla Comparativa de Modelos

**Situación:** Quieres una tabla resumen profesional.

```
Tengo 3 modelos entrenados:
- kmeans (k=5, silhouette=0.62)
- hierarchical (k=5, silhouette=0.58)
- dbscan (7 clusters + 200 ruido, silhouette=0.55)

Crea una tabla (DataFrame) que compare:
| Modelo | Clusters | Silhouette | Interpretabilidad | Recomendación |
|--------|----------|------------|-------------------|---------------|

Llénala con mis datos. Que sea clara.
```

**Lo que conseguirás:** Tabla profesional.

---

## Cómo Usar Estos Prompts

1. **Copia el prompt** que se ajuste a tu necesidad
2. **Reemplaza** `[cosas entre corchetes]` con tu contexto real
3. **Pega en GitHub Copilot** (Chat o Inline)
4. **Lee la respuesta** y adapta según lo que necesites

---

## Tips Generales

✅ **SÍ hacer:**
- Ser específico: "mi silhouette es X" es mejor que "mi métrica está mal"
- Pegar código real, no pseudocódigo
- Decir QUÉ quieres, no CÓMO hacerlo (déjalo a Copilot)

❌ **NO hacer:**
- Prompts vagos: "arregla todo"
- Pedir refactors masivos: Copilot hará cambios que no entiendas
- Ignorar cambios propuestos: revisa y entiende antes de copiar

---

## Si Nada Funciona

Si a pesar de estos prompts algo no funciona:

1. Aíslalo en una celda simple
2. Describe exactamente qué esperas y qué obtienes
3. Pide: "¿Por qué [resultado actual] en lugar de [resultado esperado]?"

