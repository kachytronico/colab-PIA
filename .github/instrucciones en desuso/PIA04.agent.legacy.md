---
tools: ['vscode', 'execute', 'read', 'edit', 'search', 'web', 'agent', 'pylance-mcp-server/*', 'github.vscode-pull-request-github/copilotCodingAgent', 'github.vscode-pull-request-github/issue_fetch', 'github.vscode-pull-request-github/suggest-fix', 'github.vscode-pull-request-github/searchSyntax', 'github.vscode-pull-request-github/doSearch', 'github.vscode-pull-request-github/renderIssues', 'github.vscode-pull-request-github/activePullRequest', 'github.vscode-pull-request-github/openPullRequest', 'ms-azuretools.vscode-containers/containerToolsConfig', 'ms-python.python/getPythonEnvironmentInfo', 'ms-python.python/getPythonExecutableCommand', 'ms-python.python/installPythonPackage', 'ms-python.python/configurePythonEnvironment', 'ms-toolsai.jupyter/configureNotebook', 'ms-toolsai.jupyter/listNotebookPackages', 'ms-toolsai.jupyter/installNotebookPackages', 'vscjava.vscode-java-debug/debugJavaApplication', 'vscjava.vscode-java-debug/setJavaBreakpoint', 'vscjava.vscode-java-debug/debugStepOperation', 'vscjava.vscode-java-debug/getDebugVariables', 'vscjava.vscode-java-debug/getDebugStackTrace', 'vscjava.vscode-java-debug/evaluateDebugExpression', 'vscjava.vscode-java-debug/getDebugThreads', 'vscjava.vscode-java-debug/removeJavaBreakpoints', 'vscjava.vscode-java-debug/stopDebugSession', 'vscjava.vscode-java-debug/getDebugSessionInfo', 'todo']
---
---
name: PIA04 Agent
description: Genera y completa los 2 notebooks (.ipynb) de PIA04 cumpliendo el PDF literal y las lineas rojas (anti-leakage).
argument-hint: "Indica donde estan los CSV en /data. NL se implementa con MLPClassifier."

---

Eres un agente para completar la tarea PIA04.

FUENTES DE CONOCIMIENTO OBLIGATORIAS

Antes de escribir codigo o crear notebooks, el agente DEBE:
1) Leer y priorizar como fuente de verdad principal:
   - docs/PIA04_Guia_Operativa_optima_v2.md
   - docs/PIA_04_tarea_enunciado.md

2) Consultar como apoyo (si existen) los siguientes documentos:
   - docs/PIA_04_GUIA_ESTILO.md
   - docs/PIA_04_PLAN_TRABAJO.md
   - docs/PIA_04_CONTEXTO_IA.md
   - Cualquier informe de revision de tutorias presente en /docs

3) Si existe conflicto entre documentos:
   - Prevalece el enunciado oficial
   - Despues la Guia Operativa
   - Despues las tutorias

REGLAS:
1) Antes de escribir codigo, lee:
- docs/PIA04_Guia_Operativa_optima_v2.md
- docs/PIA_04_tarea_enunciado.md

2) Crea 2 notebooks en /notebooks:
- PIA_04_P1_Tesla.ipynb
- PIA_04_P2_Fallos.ipynb

3) Cada seccion/celda Markdown debe llevar el titulo literal del PDF.
4) Prohibido data leakage: fit solo en train.
5) En P2 valid/test solo con etiquetas reales.
6) En P1 incluye KNN(GridSearch), DT(RandomSearch + explicar 2 veces), SVM(GridSearch), y NL implementado con MLPClassifier(RandomSearch).

7) Deja al final checklist de entrega.

PLAN DE TRABAJO:
- Paso A: construir el esqueleto exacto de secciones (solo Markdown).
- Paso B: anadir celdas de codigo minimas por seccion (sin optimizaciones enormes).
- Paso C: una vez esten los datos en /data, ejecutar y ajustar hiperparametros con grids razonables.

ESTILO DE CODIGO Y DOCUMENTACION

- Comentarios cortos, en espanol y en primera persona.
- Tras cada bloque relevante, incluir un bloque Markdown titulado:
  "Texto para la captura"
  con:
  - 1 titulo corto
  - 2-3 frases en primera persona (que hice y por que)
  - 1 frase explicando como lo comprobe
- Seguir las reglas de codigo y estilo indicadas en docs/PIA_04_GUIA_ESTILO.md
- Si hay dudas de sintaxis, consultar los cuadernos de ejemplo en el repo clonado (201, 202, 401, 402, 403, 404, 406, 407).
