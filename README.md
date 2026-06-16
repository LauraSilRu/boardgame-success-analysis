# Meeple Analytics

## ¿Qué hace que un juego de mesa tenga éxito?

Dashboard interactivo desarrollado con Streamlit para analizar los factores que explican el éxito comercial y el reconocimiento crítico de los juegos de mesa modernos.

Los datos utilizados proceden de BoardGameGeek e incluyen más de 20.000 juegos publicados entre 1950 y 2021.

---

## Objetivos del análisis

- Analizar la evolución histórica del mercado.
- Identificar qué categorías reciben mejores valoraciones.
- Comparar éxito comercial y éxito crítico.
- Detectar posibles sesgos presentes en la comunidad y en los datos.

---

## Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- Plotly

---

## Estructura del proyecto

```text
Meeple Analytics

app.py

assets/
data/
notebooks/

utils/
├── config.py
├── styles.py
└── components.py

views/
├── resumen.py
├── valoraciones.py
├── exito.py
└── sesgos.py
```

## Ejecución

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

---

Proyecto académico desarrollado con fines de análisis de datos y visualización interactiva.