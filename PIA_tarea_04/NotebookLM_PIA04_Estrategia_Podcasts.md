# NotebookLM (PIA04 UD4) — Estrategia + Prompts para podcasts de estudio (v1 · 2026-02-07)

## Objetivo
Generar **audios largos y detallados** (“podcasts”) que expliquen **cómo se resolvió cada problema** (P1 y P2) y **la base teórica** de cada decisión, usando exclusivamente tus fuentes.

---

## 1) Qué documentos subir (y cómo organizarlos)

### A) Recomendación clave
Crea **2 notebooks en NotebookLM** (mínimo), uno por problema.  
Razón: si metes demasiadas fuentes a la vez, el audio tiende a quedarse superficial.

### Notebook 1 — “PIA04_UD4_P1_Tesla”
Sube estas fuentes (en este orden):
1. `PIA_04_P1_Ledesma_Alfredo.ipynb - Colab.pdf`  (la evidencia ejecutada)
2. `PIA_04_tarea_enunciado.md` (rúbrica/qué pedían)
3. `PIA_UD4_teoria.pdf` (marco teórico)
4. `PIA04_UD4_Documento_Maestro.md` (tu explicación integrada)
5. *(opcional)* `PIA04_Guia_Unificada_Estrategica_Operativa.md` (checklists y líneas rojas)

### Notebook 2 — “PIA04_UD4_P2_Fallos”
Sube estas fuentes (en este orden):
1. `PIA_04_P2_Ledesma_Alfredo.ipynb - Colab.pdf`
2. `PIA_04_tarea_enunciado.md`
3. `PIA_UD4_teoria.pdf`
4. `PIA04_UD4_Documento_Maestro.md`
5. *(opcional)* `PIA04_Guia_Unificada_Estrategica_Operativa.md`

> Nota: prioriza la versión **PDF** del notebook porque suele leerse mejor como “fuente” (outputs incluidos).

---

## 2) Ajustes recomendados en NotebookLM (antes de generar audio)

En **Studio → Audio Overview**:
- Formato recomendado para estudiar: **Deep Dive**.
- Idioma: **Español** (European o LatAm).
- Longitud: si te deja elegir **Longer**, úsala. Si no aparece, divide en “Parte 1 / Parte 2”.
- Prompt personalizado: pega uno de los prompts de abajo.

Extra:
- Genera también un audio en formato **Critique** para que te “audite” el trabajo y te marque riesgos (leakage, uso de test, etc.).

---

## 3) Prompts listos para pegar (Audio Overview)

### 3.1 P1 (Tesla) — Deep Dive · Parte 1 (AED + Preprocesado)
**Pega tal cual:**
"""
Quiero un podcast largo y didáctico (nivel universitario) sobre el PROBLEMA 1 (Tesla).
Estructura obligatoria:
1) Contexto del problema y objetivo de negocio (qué es la variable target y qué significa).
2) AED: qué miré y por qué (nulos, distribuciones, correlación, desbalanceo). Menciona salidas concretas del notebook.
3) Preprocesado: explica cada decisión con base teórica:
   - split train/valid/test y por qué (generalización)
   - tratamiento de nulos (por qué mediana / moda)
   - categóricas y OneHot
   - escalado (por qué es crítico para KNN/SVM/MLP)
   - reducción de dimensionalidad (PCA): qué hace, cuándo conviene y trade-offs
4) Señala “líneas rojas” de fuga de datos y cómo se evitaron.
Cierra con un resumen de 10 puntos (checklist) para repetir el proceso en el futuro.
Tono: profesor + mentor. Muy detallado. No inventes métricas: usa solo lo que esté en los outputs.
"""

### 3.2 P1 (Tesla) — Deep Dive · Parte 2 (Modelos + Ensembles + conclusiones)
"""
Quiero un podcast largo y técnico (nivel examen) sobre el PROBLEMA 1 (Tesla), centrado en modelos y ensembles.
Estructura:
1) Baselines: qué son y por qué se hacen.
2) KNN + GridSearch: qué hiperparámetros importan y cómo interpretar best_params/best_score.
3) DT + RandomSearch + explicación antes/después: profundidad, sobreajuste y criterios.
4) SVM + GridSearch: C/gamma, margen, kernels, sensibilidad a escala.
5) NL (MLP) + RandomSearch: arquitectura, activación, regularización, por qué puede no mejorar.
6) Ensembles:
   - criterio de fiabilidad >80%: por qué puede mejorar o no
   - criterio “Regresión Lineal” como meta-modelo (stacking): qué significa el vector de pesos y cómo interpretarlo
7) Conclusiones finales: qué modelo elegiría y por qué; riesgos; mejoras futuras.
Incluye mini-resúmenes cada 10 minutos y un recap final de 12 puntos.
No inventes resultados; cita outputs reales.
"""

### 3.3 P2 (Fallos) — Deep Dive · Parte 1 (Semisupervisado + anti-leakage)
"""
Quiero un podcast largo y muy pedagógico sobre el PROBLEMA 2 (Fallos de producto), explicando el enfoque semisupervisado.
Estructura:
1) Qué es aprendizaje semisupervisado y por qué aplica aquí (muchos NaN en failure).
2) Separación temprana labeled vs unlabeled: por qué es crítica para evitar data leakage.
3) Split SOLO dentro de labeled (train/valid/test): regla de oro y cómo se verifica.
4) Preprocesado: imputación, OneHot para 3 categóricas y escalado; explica el porqué teórico.
5) Reducción dimensionalidad: explica por qué TruncatedSVD es adecuado tras OneHot (matriz sparse) y qué significa elegir n_components.
6) Métricas bajo desbalanceo: por qué accuracy engaña y por qué mirar balanced_accuracy/F1.
Incluye analogías y ejemplos para fijar conceptos. No inventes cifras.
"""

### 3.4 P2 (Fallos) — Deep Dive · Parte 2 (Self-training + 3 modelos + ensemble + conclusiones)
"""
Podcast largo sobre el PROBLEMA 2 (Fallos), centrado en el bucle de auto-etiquetado y el modelado final.
Estructura:
1) Self-training paso a paso: modelo base, predict_proba, umbral 0.90, mover pseudo-etiquetas, criterio de parada.
2) Riesgos: error amplification y por qué un umbral alto reduce ruido.
3) Qué se observó en tu ejecución: cuántas pseudo-etiquetas se añadieron y qué implica.
4) Entrenamiento de 3 modelos supervisados con train ampliado: cómo se optimizan (CV) sin tocar test.
5) Ensemble final: soft voting ponderado; cómo se eligen pesos usando valid (explicación matemática simple).
6) Evaluación final en test real (una sola vez): interpretación de accuracy vs balanced_accuracy y qué significa para el negocio.
7) Conclusión “trampa”: si el rendimiento es modesto, la conclusión correcta es que se necesita más etiquetado manual.
Cierra con un checklist de 15 puntos para repetir este pipeline semisupervisado sin errores.
"""

### 3.5 Audio “Critique” (auditoría de calidad)
"""
Quiero un audio en formato CRITIQUE sobre este notebook: identifica fallos graves o riesgos.
Prioriza:
- data leakage (fit con dataset completo, valid/test usados en entrenamiento o en decisiones)
- títulos de rúbrica no literales o secciones faltantes
- uso indebido de test antes del final
- errores típicos con OneHot + PCA/SVD
Da recomendaciones mínimas (no reescribir todo), indicando qué cambiar y por qué.
"""

---

## 4) Prompts útiles DESPUÉS del audio (en el chat del notebook)
1) “Dame un esquema de estudio en 2 niveles (títulos + subpuntos) y enlaza cada punto con citas a las fuentes.”
2) “Crea 25 preguntas tipo examen (10 fáciles, 10 medias, 5 difíciles) con respuesta breve.”
3) “Genera flashcards (pregunta/respuesta) de: leakage, PCA vs SVD, GridSearch vs RandomSearch, balanced accuracy, stacking.”
4) “Resume en 1 página: qué decisiones tomé y cuál era la alternativa y por qué la descarté.”

---

## 5) Cómo conseguir audios muy largos (si el selector de “Longer” no aparece)
- Divide por “Partes”: Parte 1 (AED+prepro), Parte 2 (modelos+ensembles), Parte 3 (conclusiones+errores).
- Genera 2–4 audios por problema en lugar de uno solo.

