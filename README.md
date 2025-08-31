# Dashboard de Análisis Financiero para acciones de Apple (AAPL)

## Descripción General
Este proyecto consiste en un dashboard interactivo para el análisis financiero de las acciones de Apple (AAPL). Utiliza datos históricos de precios y volúmenes de negociación para proporcionar visualizaciones y análisis detallados, así como un modelo de machine learning para la predicción de precios futuros.

## Tecnologías Utilizadas
- **Python**: Lenguaje de programación principal.
- **Streamlit**: Framework para crear aplicaciones web interactivas.
- **Pandas**: Biblioteca para el análisis de datos.
- **Plotly**: Biblioteca para la creación de gráficos interactivos.
- **Scikit-learn**: Biblioteca para machine learning.
- **Jupyter Notebook**: Entorno para la creación de documentos que contienen código en vivo, ecuaciones, visualizaciones y texto narrativo.

## Estructura del Proyecto

```
.
├── README.md
├── app.py
├── data
│   ├── AAPL_bruto.csv
│   └── AAPL_limpio.csv
├── modelo_regresion.joblib
├── notebooks
│   ├── 01_Obtencion_y_Carga.ipynb
│   ├── 02_Limpieza_y_Analisis.ipynb
│   └── 03_Modelo_ML.ipynb
├── requirements.txt
└── train_model.py
```

## Instalación
Para ejecutar este proyecto, sigue estos pasos:

1. Clona el repositorio en tu máquina local.
```bash
git clone https://github.com/HenryD11703/analisis-financiero.git
cd analisis-financiero
```

2. Crea y activa un entorno virtual:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecuta la aplicación Streamlit:
```bash
streamlit run app.py
```
