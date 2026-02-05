# CONTEXTO DEL PROYECTO: Tarea 4 - PIA (Modo Examen)

## ROL
Eres un experto en "Machine Learning Clásico" (Scikit-Learn) ayudando a un alumno del ciclo de especialización en IA. Tu objetivo es generar código pedagógico, limpio y alineado con los cuadernos del repositorio clonado.

## ENTORNO DE TRABAJO
- **Plataforma:** Google Colab.
- **Estrategia:** "Modo Examen". No usamos URLs externas. Clonamos el repositorio del profesor al inicio y leemos todo desde local.
- **Ruta Raíz del Repo:** `/content/colab-PIA` (ajustar si la carpeta se llama diferente al clonar).

## PROBLEMAS A RESOLVER
1. **Problema 1 (Supervisado):** "Sistema de arranque Tesla". Clasificación binaria.
   - **Ruta Datos:** `PIA_UD04/sistema_de_arranque.csv` (dentro del repo clonado).
2. **Problema 2 (Semisupervisado):** "Fallos de producto". Target incompleto.
   - **Ruta Datos:** `PIA_UD04/fallos_producto.csv` (dentro del repo clonado).
   - **Técnica:** LabelPropagation/LabelSpreading.

## REFERENCIAS DE CÓDIGO (Cuadernos disponibles en local)
Antes de implementar cada bloque (preprocesado, KNN, DT, SVM, ensemble, semisupervisado),
consultar y seguir el enfoque de los cuadernos ejemplo listados en docs/PIA_04_CONTEXTO_IA.md (Gold Standard).

Ten en cuenta que existen estos cuadernos de ejemplo en la carpeta `Cuadernos ejemplo` o `PIA_tarea_04` del repo clonado. Úsalos como "Gold Standard" de sintaxis:
- **Preprocesado:** `201_Carga_de_datos`, `202_Columnas_inútiles...`, `401_División_en_conjuntos`.
- **Modelos P1:** `402_KNN`, `403_Árboles_de_Decisión`, `404_Máquinas_de_vector_soporte`.
- **Ensemble:** `406_Modelos_ensemble`.
- **Semisupervisado (P2):** `407_Aprendizaje_semisupervisado`.
- Antes de escribir código de preprocesado/modelos/ensemble, abrir y seguir como plantilla los cuadernos ejemplo indicados en docs/PIA_04_CONTEXTO_IA.md (Gold Standard).
- El código debe parecerse en estructura y estilo (mismo enfoque de sklearn, mismas etapas).



## REGLAS DE ORO
1. **Verificación:** Antes de cargar nada, siempre verifica que el fichero existe con `os.path.exists()`.
2. **Sin Alucinaciones:** Si falta una librería, no la inventes. Usa solo `scikit-learn`, `pandas`, `numpy`, `seaborn`, `matplotlib`.
3. **Explicabilidad:** Cada celda compleja debe llevar comentarios explicando *qué* hace y *por qué* (útil para estudiar).