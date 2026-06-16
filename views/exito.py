import streamlit as st
import pandas as pd
import plotly.express as px

from utils.config import *
from utils.components import *

def show(df_filtered):
    st.title("🏰 Éxito comercial vs éxito crítico")

    st.markdown("""
Comparamos dos formas distintas de entender el éxito de un juego de mesa:

- Éxito comercial → número de propietarios.
- Éxito crítico → valoración media de la comunidad.

El objetivo es identificar si ambos conceptos coinciden o representan fenómenos diferentes.
""")

    st.divider()

    # TOP JUEGOS

    top_owned = (
        df_filtered
        .nlargest(
            15,
            "NumOwned"
        )
    )

    top_rated = (
        df_filtered
        .nlargest(
            15,
            "BayesAvgRating"
        )
    )

# ==================================================
# ÉXITO COMERCIAL
# ==================================================

    left, right = st.columns([3, 1])

    with left:

        st.subheader("👥 Más poseídos")

        fig1 = px.bar(
            top_owned.sort_values("NumOwned"),
            x="NumOwned",
            y="Name",
            orientation="h",
            color_discrete_sequence=[PRIMARY_COLOR]
        )

        fig1.update_layout(**PLOTLY_LAYOUT)

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with right:

        st.subheader("📌 Hallazgo clave")

        st.success(
            """
            👥 Popularidad ≠ calidad

            Los juegos más poseídos no son necesariamente los mejor valorados.
            """
        )

        st.info(
            """
            👑 Éxito comercial

            Catan, Pandemic y Ticket to Ride dominan en número de propietarios.
            """
        )

    st.divider()

    # ==================================================
    # ÉXITO CRÍTICO
    # ==================================================

    left, right = st.columns([3, 1])

    with left:

        st.subheader("⭐ Mejor valorados")

        fig2 = px.bar(
            top_rated.sort_values("BayesAvgRating"),
            x="BayesAvgRating",
            y="Name",
            orientation="h",
            color_discrete_sequence=[SECONDARY_COLOR]
        )

        fig2.update_layout(**PLOTLY_LAYOUT)

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    with right:

        st.subheader("📌 Hallazgo clave")

        st.warning(
            """
            ⭐ Reconocimiento crítico

            Gloomhaven, Brass Birmingham y Twilight Imperium lideran las valoraciones.
            """
        )

        st.info(
            """
            Los juegos mejor valorados suelen ser más complejos y especializados que los más populares.
            """
        )

    st.divider()

    st.info(
    """
    Conclusión rápida

    Los juegos más populares suelen ser accesibles y fáciles de aprender,
    mientras que los juegos mejor valorados suelen ser más complejos y especializados.
    """
)

    st.markdown("### 🎯 Conclusión ejecutiva")

    st.success(
        """
        El análisis muestra que la calidad percibida y el éxito comercial
        están relacionados, pero no son equivalentes.

        Los juegos más accesibles y conocidos suelen alcanzar una mayor
        difusión en el mercado, mientras que los juegos más complejos
        y especializados tienden a concentrar las valoraciones más altas.
        """
    )