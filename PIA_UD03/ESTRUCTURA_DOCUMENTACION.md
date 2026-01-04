# 📋 Estructura de Documentación - Problema 1 Netflix

## ✅ Documentos Creados

He creado una **estructura completa de documentación** para que entiendas y evalúes el Problema 1 de Netflix. Aquí está el contenido:

---

## 📁 Árbol de Carpetas

```
colab-PIA/PIA_UD03/
├── .github/
│   └── instructions/
│       └── pia03_problema1.instructions.md          ← Instrucciones para Copilot
├── docs/
│   ├── problema1_enunciado_y_rubrica.md             ← Qué se pide (rúbrica)
│   ├── problema1_guia_tutor.md                      ← Guía para evaluar
│   ├── problema1_checklist_validacion.md            ← Checklist de auto-revisión
│   └── problema1_prompts_copilot.md                 ← 12 prompts listos para usar
└── PIA03_Tarea_Aprendizaje_NO_supervisado_y_por_refuerzo.ipynb
```

---

## 📄 Descripción de Cada Documento

### 1️⃣ `.github/instructions/pia03_problema1.instructions.md`
**Para:** GitHub Copilot (y como referencia de desarrollo)

**Contiene:**
- Objetivo principal y contexto del proyecto
- Requisitos de la rúbrica (6 categorías)
- Checklist de coherencia técnica
- Directrices de estilo
- Prompts recomendados para Copilot

**Cuándo usarlo:** Cada vez que necesites que Copilot entienda el contexto completo.

---

### 2️⃣ `docs/problema1_enunciado_y_rubrica.md`
**Para:** Estudiante (tú) y tutor

**Contiene:**
- Enunciado claro del problema
- Rúbrica completa con pesos porcentuales (100 puntos)
  - AED: 15%
  - Preprocesamiento: 25%
  - Modelos: 35%
  - Visualizaciones: 15%
  - Recomendador: 10%
- Tabla de criterios por sección
- Notas importantes (qué NO hacer)
- Referencias

**Cuándo usarlo:** Para entender exactamente qué evalúa el tutor.

---

### 3️⃣ `docs/problema1_guia_tutor.md`
**Para:** Tutor (y estudiante interesado en cómo se evalúa)

**Contiene:**
- Resumen de puntos clave de evaluación
- Errores comunes y cómo detectarlos
- Estrategia esperada para preprocesamiento
- Tabla resumen (Excelente/Bueno/Aceptable/Deficiente)
- Ejemplos de retroalimentación (positiva y constructiva)
- Checklist para el tutor

**Cuándo usarlo:** Para entender la perspectiva del evaluador.

---

### 4️⃣ `docs/problema1_checklist_validacion.md`
**Para:** Estudiante (auto-evaluación antes de entregar)

**Contiene:**
- 50+ ítems organizados por tema
  - Objetivo final: 10 películas exactas
  - Preparación de datos
  - Ingeniería de características
  - Escalado y PCA
  - Modelos (KMeans, Jerárquico, DBSCAN)
  - Visualizaciones
  - Recomendador
  - Documentación
- Escala de puntuación rápida
- Verificación final antes de entregar

**Cuándo usarlo:** Antes de enviar tu solución. Marca cada casilla según lo completes.

---

### 5️⃣ `docs/problema1_prompts_copilot.md`
**Para:** Estudiante (con ejemplos listos para copiar/pegar)

**Contiene:**
- 12 prompts específicos y listos para usar
  1. Revisión por rúbrica
  2. Arreglo de 10 películas
  3. Detección de preprocesamiento duplicado
  4. Convertir hardcodeados a cálculos reales
  5. Reorganizar estructura del notebook
  6. Agregar gráfico faltante
  7. Verificar s5485
  8. Explicación de modelo elegido
  9. Corregir One-Hot Encoding
  10. Revisar pipeline
  11. Implementar NearestNeighbors
  12. Crear tabla comparativa

- Tips generales de uso
- "Si nada funciona" (estrategia de fallback)

**Cuándo usarlo:** Cuando necesites pedir ayuda a Copilot. Solo copia/pega y adapta `[brackets]`.

---

## 🚀 Cómo Usar Estos Documentos

### Fase 1: Preparación (AHORA)
1. Lee [problema1_enunciado_y_rubrica.md](docs/problema1_enunciado_y_rubrica.md) para entender qué se pide
2. Mantén [problema1_checklist_validacion.md](docs/problema1_checklist_validacion.md) abierto
3. Comienza a implementar tu solución

### Fase 2: Desarrollo (Durante)
1. Cada sección que termines, marca en el checklist
2. Si tienes dudas, usa un prompt de [problema1_prompts_copilot.md](docs/problema1_prompts_copilot.md)
3. Copilot tendrá el contexto completo de [.github/instructions/pia03_problema1.instructions.md](.github/instructions/pia03_problema1.instructions.md)

### Fase 3: Auto-revisión (Antes de entregar)
1. Completa el checklist al 100%
2. Lee la sección "Última verificación" del checklist
3. Si todo es SÍ, ¡listo para entregar!

### Fase 4: Evaluación (Tutor)
1. Tutor usa [problema1_guia_tutor.md](docs/problema1_guia_tutor.md) como referencia
2. Compara tu solución contra la rúbrica de [problema1_enunciado_y_rubrica.md](docs/problema1_enunciado_y_rubrica.md)
3. Da retroalimentación

---

## 💡 Ventajas de Esta Estructura

✅ **Claridad:** Cada documento tiene un propósito específico  
✅ **Coherencia:** Todos usan los mismos conceptos y términos  
✅ **Escalabilidad:** Fácil de extender si el proyecto crece  
✅ **Reutilizable:** Copilot y tutor entienden el contexto  
✅ **Auto-evaluación:** Checklist detallado para el estudiante  
✅ **Prompts listos:** No tienes que inventar cómo pedir ayuda  

---

## 🎯 Siguiente Paso

Ahora puedes:

1. **Revisar tu implementación actual** contra la rúbrica
2. **Usar los prompts** para pedir mejoras específicas a Copilot
3. **Marcar el checklist** conforme avanzas

¿Quieres que empiece a revisar tu notebook ahora?

