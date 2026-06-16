import streamlit as st
import pandas as pd
import plotly.express as px

from utils.config import *
from utils.components import *

def show(df_filtered):
    st.title("⚔️ ¿Qué impulsa las valoraciones?")

    st.markdown("""
    Exploramos qué factores están más relacionados con las valoraciones de los juegos de mesa.

    El objetivo es identificar las características que parecen influir en la percepción de calidad y reconocimiento crítico.
    """)

    st.divider()

    # ==================================================
    # CATEGORÍAS
    # ==================================================

    categories = [
        "Cat:Thematic",
        "Cat:Strategy",
        "Cat:War",
        "Cat:Family",
        "Cat:CGS",
        "Cat:Abstract",
        "Cat:Party",
        "Cat:Childrens"
    ]

    results = []

    for cat in categories:

        results.append({
            "Category": cat.replace("Cat:", ""),
            "AvgRating": df_filtered[df_filtered[cat] == 1]["BayesAvgRating"].mean()
        })

    category_df = pd.DataFrame(results)

    best_category = category_df.loc[
        category_df["AvgRating"].idxmax(),
        "Category"
    ]

    best_rating = category_df["AvgRating"].max()

    worst_category = category_df.loc[
        category_df["AvgRating"].idxmin(),
        "Category"
    ]

    # ==================================================
    # LAYOUT CATEGORÍAS + INSIGHTS
    # ==================================================

    left, right = st.columns([3, 1])

    with left:

        st.subheader("🐉 Valoración media por categoría")

        fig = px.bar(
            category_df.sort_values("AvgRating"),
            x="AvgRating",
            y="Category",
            orientation="h",
            color_discrete_sequence=[SECONDARY_COLOR]
        )

        fig.update_layout(**PLOTLY_LAYOUT)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("📌 Hallazgos clave")

        st.success(
            f"""
            Categoría líder:

            **{best_category}**

            Rating medio:

            **{best_rating:.2f}**
            """
        )

        st.info(
            f"""
            Categoría con menor valoración:

            **{worst_category}**
            """
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.warning(
                    """
                    Las diferencias entre categorías
                    son mayores que las observadas
                    entre segmentos de jugadores.
                    """
                )

        st.divider()

    # ==================================================
# COMPLEJIDAD VS VALORACIÓN
# ==================================================

    fig = px.scatter(
        df_filtered,
        x="GameWeight",
        y="BayesAvgRating",
        opacity=0.35,
        color_discrete_sequence=[TERTIARY_COLOR]
    )

    fig.update_layout(**PLOTLY_LAYOUT)

    left, right = st.columns([3, 1])

    with left:

        st.subheader("🧠 Complejidad frente a valoración")

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("📌 Hallazgo")

        st.info(
            """
            Los juegos más complejos tienden a recibir mejores valoraciones.

            Existe una relación positiva, aunque no es suficiente para explicar por sí sola el éxito de un juego.
            """
        )

    st.divider()

# ==================================================
# EVOLUCIÓN DE LAS VALORACIONES
# ==================================================

    rating_period = (
        df_filtered.groupby(
            pd.cut(
                df_filtered["YearPublished"],
                bins=[1950, 1970, 1990, 2010, 2022]
            )
        )["BayesAvgRating"]
        .mean()
        .reset_index()
    )

    rating_period["Period"] = [
        "1950-1970",
        "1970-1990",
        "1990-2010",
        "2010-2021"
    ]

    fig = px.bar(
        rating_period,
        x="Period",
        y="BayesAvgRating",
        color_discrete_sequence=[PRIMARY_COLOR]
    )

    fig.update_layout(**PLOTLY_LAYOUT)

    left, right = st.columns([3, 1])

    with left:

        st.subheader("📈 Valoraciones por periodo histórico")

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("📌 Hallazgo")

        st.success(
            """
            Los juegos modernos reciben valoraciones medias superiores a las de décadas anteriores.

            Esto puede reflejar mejoras en el diseño o un posible sesgo de supervivencia.
            """
        )

    st.divider()

    st.markdown("### 🎯 Conclusión ejecutiva")

    st.success(
        """
        Las categorías de juego parecen influir más en las valoraciones
        que factores como el número de jugadores o la duración.

        Los juegos de estrategia dominan las valoraciones mientras que
        la complejidad muestra una relación positiva moderada con el rating.

        Además, los juegos publicados en décadas recientes reciben
        valoraciones significativamente más altas.
        """
    )