# ==================================================
# IMPORTS
# ==================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.config import *
from utils.styles import load_css
from utils.components import *
from views import resumen
from views import valoraciones
from views import exito
from views import sesgos

# ==================================================
# CONFIGURACIÓN DE LA PÁGINA
# ==================================================

st.set_page_config(
    page_title="¿Qué hace que un juego de mesa tenga éxito?",
    page_icon="assets/meeple.svg",
    layout="wide"
)

load_css()

# ==================================================
# CARGA DE DATOS
# ==================================================

@st.cache_data
def load_data():
    df = pd.read_csv("data/games_clean.csv")
    df = df[df["YearPublished"] >= 1950]
    return df

df = load_data()

# ==================================================
# CABECERA
# ==================================================

header_col1, header_col2 = st.columns([0.6,6.4])

with header_col1:
    st.image(
        "assets/meeple.svg",
        width=110
    )

with header_col2:

    st.title("¿Qué hace que un juego de mesa tenga éxito?")

    st.caption(
        "1950–2021 • Datos de BoardGameGeek"
    )

    st.markdown("""
    Análisis de los factores que explican el éxito comercial
    y el reconocimiento crítico de los juegos de mesa modernos.

    **Proyecto de análisis basado en datos de BoardGameGeek.**
    """)

st.divider()

# ==================================================
# FILTROS GLOBALES
# ==================================================

st.sidebar.markdown("<br>", unsafe_allow_html=True)

st.sidebar.title("Filtros")

# FILTRO DE AÑO

year_range = st.sidebar.slider(
    "Año de publicación",
    1950,
    int(df["YearPublished"].max()),
    (
        1950,
        int(df["YearPublished"].max())
    )
)

# FILTRO DE CATEGORÍA

category_options = {
    "Todas": None,
    "Strategy": "Cat:Strategy",
    "Thematic": "Cat:Thematic",
    "Family": "Cat:Family",
    "War": "Cat:War",
    "Party": "Cat:Party",
    "Abstract": "Cat:Abstract",
    "CGS": "Cat:CGS",
    "Childrens": "Cat:Childrens"
}

selected_category = st.sidebar.selectbox(
    "Categoría",
    list(category_options.keys())
)

# APLICAR FILTROS

df_filtered = df[
    (df["YearPublished"] >= year_range[0])
    &
    (df["YearPublished"] <= year_range[1])
]

if selected_category != "Todas":

    category_column = category_options[selected_category]

    df_filtered = df_filtered[
        df_filtered[category_column] == 1
    ]

st.sidebar.divider()

st.sidebar.metric(
    "♟️ Juegos analizados",
    f"{len(df_filtered):,}"
)

# ==================================================
# NAVEGACIÓN
# ==================================================

st.sidebar.divider()

page = st.sidebar.radio(
    "Ir a",
    [
        "Resumen Ejecutivo",
        "¿Qué impulsa las valoraciones?",
        "Éxito comercial vs éxito crítico",
        "Gobernanza y sesgos"
    ]
)

st.sidebar.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.sidebar.columns([1,2,1])

with col2:
    st.image(
        "assets/meeple.svg",
        width=70
    )

# ==================================================
# PÁGINA 1 - RESUMEN EJECUTIVO
# ==================================================

if page == "Resumen Ejecutivo":
    resumen.show(df_filtered)

# ==================================================
# PÁGINA 2 - ¿QUÉ IMPULSA LAS VALORACIONES?
# ==================================================

elif page == "¿Qué impulsa las valoraciones?":
    valoraciones.show(df_filtered)


# ==================================================
# PÁGINA 3 - ÉXITO COMERCIAL VS ÉXITO CRÍTICO
# ==================================================

elif page == "Éxito comercial vs éxito crítico":
    exito.show(df_filtered)

# ==================================================
# PÁGINA 4 - GOBERNANZA Y SESGOS
# ==================================================

elif page == "Gobernanza y sesgos":
    sesgos.show(df_filtered)