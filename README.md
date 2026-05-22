# Ayudante

Repositorio de ayuda para EDA y Machine Learning.

## Contenido

- **visualizaciones/**
  - `correlacion.py` — `heatmap_corr(df)`: heatmap de correlación triangular con seaborn.
  - `regresiones.py` — `par_real_predicho(y_test, y_pred)`: gráfico real vs. predicho con bisectriz. `par_real_predicho_res(y_test, y_pred)`: diagnóstico de residuos con KDE y normal teórica.
- **ml/**
  - `importancias.py` — `grafica_importancias(model)`: barras de importancia de características para modelos con `feature_importances_`.

## Instalación

### Desde GitHub

```bash
git clone <url-del-repositorio>
cd ayudante
pip install .
```

### En modo editable (recomendado para desarrollo)

```bash
git clone <url-del-repositorio>
cd ayudante
pip install -e .
```

## Uso

```python
from visualizaciones.correlacion import heatmap_corr
from visualizaciones.regresiones import par_real_predicho, par_real_predicho_res
from ml.importancias import grafica_importancias
```

## Dependencias

numpy, pandas, matplotlib, seaborn, scipy