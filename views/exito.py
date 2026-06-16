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

    # ==================================================
    # VALIDACIÓN CON JUEGOS RECIENTES
    # ==================================================

    st.divider()

    st.subheader("🔄 Validación con juegos recientes (2022-2025)")

    st.markdown("""
    Como validación adicional, se revisaron los títulos más destacados
    publicados después de 2021 para comprobar si las tendencias observadas
    siguen vigentes en la actualidad.
    """)

    left, center, right = st.columns([3, 1.2, 3])

    # TOP VALORADOS

    with left:

        st.markdown("#### ⭐ Más valorados")

        recent_rated = pd.DataFrame({
            "Juego": [
                "SETI",
                "Dune: Imperium Uprising",
                "Arcs",
                "Earth",
                "Harmonies",
                "Sky Team",
                "Nucleum",
                "Forest Shuffle",
                "Bomb Busters",
                "Finspan"
            ]
        })

        st.table(recent_rated)

    # HALLAZGO

    with center:

        st.success(
            """
            🔄 Hallazgo

            Muchos de los títulos
            mejor valorados también
            aparecen entre los más
            populares.

            Esto sugiere una mayor
            convergencia entre éxito
            crítico y comercial que
            en los juegos clásicos.
            """
        )

    # TOP POSEÍDOS

    with right:

        st.markdown("#### 👥 Más poseídos")

        recent_owned = pd.DataFrame({
            "Juego": [
                "Ark Nova",
                "Earth",
                "Dune: Imperium Uprising",
                "Sky Team",
                "Forest Shuffle",
                "Harmonies",
                "Heat",
                "The White Castle",
                "Nucleum",
                "Challengers!"
            ]
        })

        st.table(recent_owned)

    st.info(
        """
        Juegos como Earth, Dune: Imperium Uprising, Sky Team,
        Forest Shuffle, Harmonies y Nucleum aparecen en ambos rankings.

        Esto refuerza parcialmente las conclusiones obtenidas con el dataset histórico
        y sugiere que algunos lanzamientos recientes consiguen simultáneamente
        reconocimiento crítico y éxito comercial.
        """
    )

    st.markdown("### 🎯 Conclusión")

    st.success(
        """
        El análisis muestra que la calidad percibida y el éxito comercial
        están relacionados, pero no son equivalentes.

        Los juegos más accesibles y conocidos suelen alcanzar una mayor
        difusión en el mercado, mientras que los juegos más complejos
        y especializados tienden a concentrar las valoraciones más altas.

        Además, la revisión de títulos publicados entre 2022 y 2025
        sugiere una convergencia creciente entre popularidad y valoración,
        reforzando parcialmente las conclusiones obtenidas con el dataset histórico.
        """
    )