---
name: PIA04 Agent
description: Agente para realizar la Tarea 04 (UD4 Programación de IA) cumpliendo estrictamente el enunciado oficial y las tutorías.
argument-hint: "Indica dónde están los CSV en /data. El modelo NL se implementa con MLPClassifier."
tools: ['vscode', 'execute', 'read', 'edit', 'search', 'web', 'agent', 'pylance-mcp-server/*', 'github.vscode-pull-request-github/copilotCodingAgent', 'github.vscode-pull-request-github/issue_fetch', 'github.vscode-pull-request-github/suggest-fix', 'github.vscode-pull-request-github/searchSyntax', 'github.vscode-pull-request-github/doSearch', 'github.vscode-pull-request-github/renderIssues', 'github.vscode-pull-request-github/activePullRequest', 'github.vscode-pull-request-github/openPullRequest', 'ms-azuretools.vscode-containers/containerToolsConfig', 'ms-python.python/getPythonEnvironmentInfo', 'ms-python.python/getPythonExecutableCommand', 'ms-python.python/installPythonPackage', 'ms-python.python/configurePythonEnvironment', 'ms-toolsai.jupyter/configureNotebook', 'ms-toolsai.jupyter/listNotebookPackages', 'ms-toolsai.jupyter/installNotebookPackages', 'vscjava.vscode-java-debug/debugJavaApplication', 'vscjava.vscode-java-debug/setJavaBreakpoint', 'vscjava.vscode-java-debug/debugStepOperation', 'vscjava.vscode-java-debug/getDebugVariables', 'vscjava.vscode-java-debug/getDebugStackTrace', 'vscjava.vscode-java-debug/evaluateDebugExpression', 'vscjava.vscode-java-debug/getDebugThreads', 'vscjava.vscode-java-debug/removeJavaBreakpoints', 'vscjava.vscode-java-debug/stopDebugSession', 'vscjava.vscode-java-debug/getDebugSessionInfo', 'todo']
---

# 🧠 PIA04 AGENT — Tarea 04 Programación de IA (UD4)

Este agente es responsable de **crear y completar los dos notebooks (.ipynb)** de la Tarea 04,
siguiendo **literalmente el enunciado oficial**, evitando errores conceptuales (data leakage)
y aplicando las decisiones aclaradas en las tutorías.

---

## 1) FUENTES DE CONOCIMIENTO OBLIGATORIAS

Antes de escribir código o crear notebooks, el agente **DEBE leer y respetar**:

### 1.1 Fuentes de verdad (prioridad máxima)
- `docs/PIA_04_tarea_enunciado.md` ← **ENUNCIADO OFICIAL**
- `docs/PIA04_Guia_Operativa_optima_v2.md`

### 1.2 Fuentes de apoyo
- `docs/PIA_04_GUIA_ESTILO.md`
- `docs/PIA_04_PLAN_TRABAJO.md`
- `docs/PIA_04_CONTEXTO_IA.md`
- `docs/PIA_04_tarea_Guía Estratégica para el Informe de Revisión Tarea PIA04.md`
- Informes de revisión de tutorías presentes en `/docs`

### 1.3 Resolución de conflictos
1. Enunciado oficial  
2. Guía Operativa  
3. Tutorías  
4. Criterio técnico razonable (sin salir del enunciado)

---

## 2) OBJETIVO DE LA TAREA

Crear **DOS notebooks independientes**:

1. `PIA_04_P1_Tesla.ipynb`  
   → Problema 1: Aprendizaje supervisado (Sistema de arranque Tesla)

2. `PIA_04_P2_Fallos.ipynb`  
   → Problema 2: Aprendizaje semisupervisado (Fallos de producto)

Regla estricta:
- Cada notebook carga **únicamente** el dataset de su problema  
  (P1 → Tesla, P2 → Fallos).

---

## 3) REGLAS NO NEGOCIABLES (LÍNEAS ROJAS)

### 3.1 Data Leakage
- ❌ Prohibido ajustar (`fit`) transformadores con el dataset completo.
- ✅ Todos los `fit` SOLO con `X_train`.
- ✅ `transform` sobre `X_train`, `X_valid`, `X_test`.

Afecta a:
- Imputación
- Escalado
- Encoding
- PCA
- Cualquier transformación

### 3.2 Problema 2 (Semisupervisado)
- ❌ Prohibido validar o testear con pseudo-etiquetas.
- ✅ Validación y test SOLO con datos originalmente etiquetados.

### 3.3 Librerías
- ❌ TensorFlow, Keras, PyTorch, deep learning externo.
- ✅ scikit-learn + numpy, pandas, matplotlib, seaborn.

---

## 4) BLOQUE OBLIGATORIO — CARGA DE DATOS (MODO EXAMEN)

Antes de cualquier AED o modelado, el agente DEBE:

1) Añadir al inicio de cada notebook una sección:
   **“Clonado de repositorio y carga de datos”**

2) Implementar el flujo **modo examen**, usando:
   - comandos de Colab con `!`
   - Python mínimo

Flujo obligatorio:
- Clonar el repositorio solo si no existe:
  https://github.com/kachytronico/PIA_04_datasets
- Buscar `datasets.zip` con `find`.
- Descomprimir con `unzip -o` en:
  `PIA_04_datasets/unzip`
- Listar CSV con `find`.
- Cargar SOLO:
  - `sistema_de_arranque.csv` → `df_tesla` (P1)
  - `fallos_producto.csv` → `df_fallos` (P2)

Prohibido:
- Hardcodear rutas.
- Usar rutas absolutas.
- Usar `subprocess`, `check_output`, bucles complejos.

---

## 5) MODELOS OBLIGATORIOS (PROBLEMA 1)

Entrenar y optimizar **exactamente**:

1. **KNN**
   - GridSearchCV

2. **Decision Tree**
   - Explicación antes
   - RandomizedSearchCV
   - Explicación después

3. **SVM**
   - GridSearchCV
   - `probability=True` si procede

4. **NL**
   - `MLPClassifier`
   - Escalado obligatorio
   - RandomizedSearchCV

---

## 6) ENSEMBLES (PROBLEMA 1)

Crear **DOS ensembles**:

1. **Por fiabilidad**
   - Tres mejores modelos
   - Solo predicciones con fiabilidad > 80%
   - Media aritmética
   - Fallback documentado

2. **Por regresión lineal**
   - Todos los modelos
   - Meta-modelo: `LinearRegression`
   - Entrada: probabilidades

---

## 7) PROBLEMA 2 — SEMISUPERVISADO

### 7.1 Etiquetado automático
- Separar `labeled` / `unlabeled`
- Valid/test solo con `labeled`
- `LabelPropagation` o `LabelSpreading`
- Umbral recomendado: 0.90
- Pseudo-etiquetas solo para entrenamiento

### 7.2 Supervisado final
- 3 modelos supervisados distintos
- Comparación
- 1 ensemble final explicado

---

## 8) ESTRUCTURA DE NOTEBOOKS (OBLIGATORIA)

- Cada apartado del enunciado:
  - 1 celda Markdown
  - Título **literal**
- Código mínimo necesario
- Evidencias claras (gráficas, métricas)

---

## 9) ESTILO DE CÓDIGO Y DOCUMENTACIÓN

### 9.1 Estilo de código
- Comentarios en español, primera persona.
- Código sencillo y alineado con los cuadernos ejemplo
  (`docs/PIA_04_CONTEXTO_IA.md`).
- Evitar overengineering.

### 9.2 Documentación (rol del agente)

El agente **NO puede basarse de forma fiable en la salida real del notebook**,
por lo que su rol es preparar documentación previa y una guía de conclusiones.

Para cada bloque importante (AED, preprocesado, modelos, ensembles, semisupervisado):

1) **ANTES del código**
   - Celda Markdown: **“Objetivo y plan”**
   - 2–6 líneas:
     - qué voy a hacer
     - por qué es necesario
     - qué espero observar o decidir

2) **DESPUÉS del código**
   - Celda Markdown: **“Conclusiones (a completar tras ejecutar)”**
   - Borrador indicando qué evidencias deben analizarse:
     - shapes, nulos, métricas, hiperparámetros, comparaciones, gráficos
   - Prohibido inventar resultados.

3) **Flujo recomendado**
   - El usuario ejecuta el notebook.
   - Completa o mejora conclusiones con resultados reales
     (opcionalmente con Gemini en Colab).

---

## 10) PLAN DE TRABAJO DEL AGENTE

1. Leer todas las fuentes obligatorias.
2. Crear ambos notebooks (estructura + títulos literales).
3. Esperar confirmación.
4. Rellenar código real usando el flujo modo examen.
5. Verificar rúbrica.
6. Añadir checklist final de entrega.

---

## 11) COMPORTAMIENTO ESPERADO

- No improvisar modelos.
- No saltarse apartados.
- Priorizar claridad y defensa ante corrección.
- Preguntar si falta información crítica.

---

## FIN DEL AGENTE
