import streamlit as st
import pandas as pd
import plotly.express as px

from utils.config import *
from utils.components import *

def show(df_filtered):
    # ==================================================
    # TARJETAS KPI
    # ==================================================

    st.subheader("👑 Resumen Ejecutivo")

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "♟️ Juegos",
            f"{len(df_filtered):,}"
        )

    with col2:
        st.metric(
            "⭐ Valoración media",
            round(df_filtered["BayesAvgRating"].mean(), 2)
        )

    with col3:
        st.metric(
            "🧠 Complejidad",
            round(df_filtered["GameWeight"].mean(), 2)
        )

    with col4:
        st.metric(
            "⏱️ Duración",
            round(df_filtered["MfgPlaytime"].median(), 0)
        )

    with col5:
        st.metric(
            "👥 Propietarios",
            f"{int(df_filtered['NumOwned'].mean()):,}"
        )
        
    st.markdown("<br>", unsafe_allow_html=True)
# ==================================================
# VISIÓN GENERAL DEL MERCADO
# ==================================================

    left, right = st.columns([3, 1])

    with left:

        games_since_1950 = (
            df_filtered
            .groupby("YearPublished")
            .size()
            .reset_index(name="Games")
        )

        fig = px.bar(
            games_since_1950,
            x="YearPublished",
            y="Games",
            title="Evolución de las publicaciones de juegos de mesa",
            color_discrete_sequence=[PRIMARY_COLOR]
        )

        fig.update_layout(
    **PLOTLY_LAYOUT,
    height=500
)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.success("""
        🧙 Crecimiento del mercado

        Las publicaciones anuales se han multiplicado desde la década de 1990.
        """)

        st.info("""
        ⭐ Popularización del hobby

        Los juegos de mesa modernos muestran un crecimiento sostenido durante las últimas décadas.
        """)

        st.warning("""
        👑 Categoría líder

        Los juegos de estrategia obtienen las valoraciones medias más altas del conjunto analizado.
        """)