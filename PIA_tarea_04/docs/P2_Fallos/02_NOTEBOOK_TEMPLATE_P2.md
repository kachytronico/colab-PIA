# Notebook template P2 - Fallos de producto

## (Opcional) Carga de datos modo examen

Codigo minimo sugerido:
```python
# 1) Clonar repo si no existe
# if not os.path.exists("PIA_04_datasets"):
#     !git clone https://github.com/kachytronico/PIA_04_datasets

# 2) Buscar datasets.zip
# !find . -name "datasets.zip"

# 3) Descomprimir
# !unzip -o "ruta/encontrada/datasets.zip" -d "PIA_04_datasets/unzip"

# 4) Localizar fallos_producto.csv sin rutas rigidas
# import os
# csv_path = None
# for root, _, files in os.walk("."):
#     if "fallos_producto.csv" in files:
#         csv_path = os.path.join(root, "fallos_producto.csv")
#         break
# if csv_path is None:
#     raise FileNotFoundError("fallos_producto.csv no encontrado")
# df_fallos = pd.read_csv(csv_path)
# df_fallos.head()
```
Comentario breve a completar tras ejecutar:
- Anotar la ruta detectada y confirmar que el CSV se carga correctamente.

---

## Realiza un AED sobre el conjunto de datos.

Codigo minimo sugerido:
```python
# df_fallos.info()
# df_fallos.head()
# df_fallos.isna().mean().sort_values(ascending=False)
```
Comentario breve a completar tras ejecutar:
- Resumir tamaño, tipos y presencia de nulos.

## Estadisticos iniciales. 0.2 puntos

Codigo minimo sugerido:
```python
# df_fallos.describe(include="all").T
```
Comentario breve a completar tras ejecutar:
- Destacar rangos, medias y posibles valores extremos.

## Distribuciones de las variables numericas del conjunto de datos. 0.3 puntos

Codigo minimo sugerido:
```python
# df_fallos.select_dtypes(include="number").hist(bins=30, figsize=(12, 8))
# plt.suptitle("Distribuciones numericas")
```
Comentario breve a completar tras ejecutar:
- Mencionar sesgos, colas o outliers visibles.

## Matriz de correlacion. 0.5 puntos

Codigo minimo sugerido:
```python
# corr = df_fallos.select_dtypes(include="number").corr()
# sns.heatmap(corr, cmap="coolwarm", center=0)
```
Comentario breve a completar tras ejecutar:
- Señalar correlaciones altas y posibles redundancias.

---

## Realiza el preprocesamiento de datos de tu problema.

Codigo minimo sugerido:
```python
# Definir columnas numericas y categoricas
# cat_cols = ["product_code", "attribute_0", "attribute_1"]
# num_cols = [c for c in df_fallos.columns if c not in cat_cols + ["failure", "id"]]
```
Comentario breve a completar tras ejecutar:
- Justificar columnas excluidas y estrategia general.

## Reserva un conjunto de datos para validacion y otro para testeo. 0.5 puntos

Codigo minimo sugerido:
```python
# df_labeled = df_fallos[df_fallos["failure"].notna()].copy()
# df_unlabeled = df_fallos[df_fallos["failure"].isna()].copy()
# X = df_labeled.drop(columns=["failure"])
# y = df_labeled["failure"]
# X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
# X_valid, X_test, y_valid, y_test = train_test_split(X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42)
```
Comentario breve a completar tras ejecutar:
- Anotar tamaños y confirmar que valid/test salen solo de labeled.

## Columnas inutiles, valores sin sentido y atipicos. 1 puntos

Codigo minimo sugerido:
```python
# Decidir si eliminar "id" (identificador) y justificar
# X_train = X_train.drop(columns=["id"], errors="ignore")
# X_valid = X_valid.drop(columns=["id"], errors="ignore")
# X_test = X_test.drop(columns=["id"], errors="ignore")
# df_unlabeled = df_unlabeled.drop(columns=["id"], errors="ignore")
# Reglas de valores imposibles / atipicos (solo con train)
```
Comentario breve a completar tras ejecutar:
- Describir reglas de limpieza aplicadas y su motivo.

## Tratamiento de valores nulos. 0.5 puntos

Codigo minimo sugerido:
```python
# num_pipe = Pipeline(steps=[
#     ("imputer", SimpleImputer(strategy="median")),
#     ("scaler", StandardScaler())
# ])
# cat_pipe = Pipeline(steps=[
#     ("imputer", SimpleImputer(strategy="most_frequent")),
#     ("onehot", OneHotEncoder(handle_unknown="ignore"))
# ])
# preprocessor = ColumnTransformer([
#     ("num", num_pipe, num_cols),
#     ("cat", cat_pipe, cat_cols)
# ])
```
Comentario breve a completar tras ejecutar:
- Indicar porcentaje de nulos y metodo elegido.

## Analisis de variabilidad. 0.5 puntos

Codigo minimo sugerido:
```python
# selector = VarianceThreshold(threshold=0.0)
# X_train_sel = selector.fit_transform(X_train_proc)
# X_valid_sel = selector.transform(X_valid_proc)
# X_test_sel = selector.transform(X_test_proc)
```
Comentario breve a completar tras ejecutar:
- Indicar si se eliminaron columnas por baja varianza.

## Columnas categoricas. 0.5 punto

Codigo minimo sugerido:
```python
# Confirmar que OneHotEncoder se ajusta solo con train
# X_train_proc = preprocessor.fit_transform(X_train)
# X_valid_proc = preprocessor.transform(X_valid)
# X_test_proc = preprocessor.transform(X_test)
# X_unlabeled_proc = preprocessor.transform(df_unlabeled.drop(columns=["failure"], errors="ignore"))
```
Comentario breve a completar tras ejecutar:
- Anotar el numero de columnas tras el encoding.

## Reduccion de la dimensionalidad. 1 punto

Codigo minimo sugerido:
```python
# pca = PCA(n_components=0.90, random_state=42)
# X_train_pca = pca.fit_transform(X_train_proc)
# X_valid_pca = pca.transform(X_valid_proc)
# X_test_pca = pca.transform(X_test_proc)
# X_unlabeled_pca = pca.transform(X_unlabeled_proc)
```
Comentario breve a completar tras ejecutar:
- Indicar varianza explicada y numero de componentes.

---

## Realiza un etiquetado automatico. 1 punto

Codigo minimo sugerido:
```python
# base_model = KNeighborsClassifier()  # o LogisticRegression(max_iter=1000)
# max_iters = 10
# unlabeled_counts = []
# X_train_aug, y_train_aug = X_train_pca, y_train.copy()
# X_unl = X_unlabeled_pca
# for _ in range(max_iters):
#     base_model.fit(X_train_aug, y_train_aug)
#     proba = base_model.predict_proba(X_unl)
#     max_proba = proba.max(axis=1)
#     pseudo_mask = max_proba >= 0.90
#     if pseudo_mask.sum() == 0:
#         break
#     y_pseudo = proba[pseudo_mask].argmax(axis=1)
#     X_train_aug = np.vstack([X_train_aug, X_unl[pseudo_mask]])
#     y_train_aug = np.concatenate([y_train_aug, y_pseudo])
#     X_unl = X_unl[~pseudo_mask]
#     unlabeled_counts.append(X_unl.shape[0])
# # Graficar descenso de unlabeled
# plt.plot(unlabeled_counts)
# plt.title("Unlabeled restantes por iteracion")
```
Comentario breve a completar tras ejecutar:
- Describir cuantas filas se pseudo-etiquetaron y por que se paro.

---

## Entrena y optimiza distintos modelos supervisados.

Codigo minimo sugerido:
```python
# Definir 3 modelos distintos y sus grids
# Usar train ampliado (reales + pseudo)
# Usar valid para seleccionar hiperparametros
```
Comentario breve a completar tras ejecutar:
- Comparar metricas y justificar la seleccion final.

## Modelo 1. 1 punto

Codigo minimo sugerido:
```python
# GridSearchCV / RandomizedSearchCV con el modelo 1
# Evaluar en valid
```
Comentario breve a completar tras ejecutar:
- Indicar mejores parametros y metricas.

## Modelo 2. 1 punto

Codigo minimo sugerido:
```python
# GridSearchCV / RandomizedSearchCV con el modelo 2
# Evaluar en valid
```
Comentario breve a completar tras ejecutar:
- Indicar mejores parametros y metricas.

## Modelo 3. 1 punto

Codigo minimo sugerido:
```python
# GridSearchCV / RandomizedSearchCV con el modelo 3
# Evaluar en valid
```
Comentario breve a completar tras ejecutar:
- Indicar mejores parametros y metricas.

---

## Crea un modelo ensemble y explica el criterio que utilizas. 1 punto

Codigo minimo sugerido:
```python
# Soft voting ponderado por metrica en valid
# weights = [w1, w2, w3]
# ensemble = VotingClassifier(estimators=[...], voting="soft", weights=weights)
# ensemble.fit(X_train_aug, y_train_aug)
# valid_pred = ensemble.predict(X_valid_pca)
```
Comentario breve a completar tras ejecutar:
- Explicar el criterio de pesos y la mejora frente a modelos individuales.

---

## Evaluacion final (solo test_labeled)

Codigo minimo sugerido:
```python
# test_pred = ensemble.predict(X_test_pca)
# print(classification_report(y_test, test_pred))
# print("Accuracy:", accuracy_score(y_test, test_pred))
```
Comentario breve a completar tras ejecutar:
- Si accuracy ~0.55, concluir que hace falta mas etiquetado manual.
