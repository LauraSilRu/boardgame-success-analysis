import streamlit as st

from utils.config import *
from utils.components import *

def show(df_filtered):
    st.title("📜 Gobernanza y sesgos")

    st.markdown("""
    Los análisis anteriores muestran patrones interesantes, pero también es importante entender las limitaciones del dataset.

    En esta sección identificamos posibles sesgos que pueden afectar a la interpretación de los resultados.
    """)

    st.divider()

    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:
        st.metric(
            "Valores nulos Family",
            "15k+"
        )

    with kpi2:
        st.metric(
            "Valores nulos LanguageEase",
            "6k+"
        )

    with kpi3:
        st.metric(
            "Valores nulos ComAgeRec",
            "5.5k+"
        )

    st.markdown("<br>", unsafe_allow_html=True)

# ==================================================
# PRIMERA FILA
# ==================================================

    left, right = st.columns(2)

    with left:

        st.warning(
            """
                👥 SESGO DE LA COMUNIDAD

    Categoría	-> Rating

    Strategy -> 6.16

    Thematic ->	6.02

    Childrens ->	5.51

    Pregunta:

    *¿Son realmente peores los juegos infantiles?*

    Probablemente no.

    Lo que ocurre es que BoardGameGeek está compuesto mayoritariamente por:

    * Jugadores adultos
    * Aficionados frecuentes
    * Gente interesada en juegos más complejos

    Por tanto, el dataset puede sobrevalorar juegos de estrategia y temática frente a juegos infantiles o familiares debido al perfil de los usuarios que participan en la plataforma.
            """
        )

    with right:

        st.warning(
            """
            ⏱️ SESGO TEMPORAL O DE SUPERVIVENCIA

    Los juegos más recientes reciben mejores valoraciones.

    Pero aquí hay dos explicaciones posibles:

    * Explicación A: Los juegos modernos son mejores

    La industria ha evolucionado:

    * Mejores mecánicas
    * Más playtesting
    * Más experiencia de diseño
    * Mayor profesionalización

    Por tanto, los juegos modernos podrían ser realmente mejores.

    *Explicación B:* Sesgo de supervivencia

    Los juegos de 1955 ¿Cuáles siguen apareciendo hoy en BoardGameGeek?

    Probablemente los más conocidos, populares o publicitados

    Mientras que miles de juegos con menor inversión o menos populares o con temáticas que no se ajustaban a las tendencias de la época han desaparecido.

    Eso hace que los periodos antiguos estén filtrados naturalmente.

    Por tanto, la diferencia puede estar influida por un sesgo de supervivencia, ya que muchos títulos antiguos con escasa relevancia comercial han desaparecido del mercado o reciben poca atención dentro de la comunidad actual.
            """
        )

    st.divider()

    # ==================================================
    # SEGUNDA FILA
    # ==================================================

    left, right = st.columns(2)

    with left:

        st.warning(
            """
            👑 SESGO DE POPULARIDAD

    Las variables más relacionadas con las valoraciones son:

    • NumWish → 0.77
    • NumOwned → 0.64
    • NumUserRatings → 0.63

    Pregunta:

    *¿Los juegos reciben mejores valoraciones porque son mejores o porque son más conocidos?*

    No podemos saberlo.

    Pero sí sabemos que tienen mejores ratings:

    * Juegos más poseídos
    * Juegos más votados

    Los juegos más populares reciben más atención por parte de la comunidad, lo que puede influir en sus valoraciones y favorecer a títulos ya consolidados.
            """
        )

    with right:

        st.warning(
            """
            🧙 SESGO POR DATOS FALTANTES

    *Family*

    Más de 15.000 nulos.

    Esto significa que muchos juegos no pertenecen a una familia/franquicia o esa información no fue registrada.

    Por tanto, no sería recomendable sacar conclusiones sobre franquicias o familias de juegos usando este dataset.

    *LanguageEase*

    Casi 6.000 nulos.

    Además esta variable depende de aportaciones de la comunidad.

    Por tanto, los análisis relacionados con accesibilidad lingüística podrían no representar adecuadamente todos los juegos.

    *ComAgeRec*

    Más de 5.500 nulos.

    La edad recomendada por la comunidad no está disponible para todos los juegos.

    Por tanto, las comparaciones entre la edad recomendada por fabricantes y comunidad deben interpretarse con cautela, al no presentarse en todos los juegos y estar basado en un número desconocido de opiniones.
            """
        )

        st.markdown("## 🎯 Conclusión ejecutiva")


    st.success(
        """
        Los resultados obtenidos son consistentes, pero deben interpretarse teniendo en cuenta las limitaciones del dataset.

        La composición de la comunidad de BoardGameGeek, la popularidad de determinados títulos, los efectos temporales y la existencia de datos faltantes pueden influir en las conclusiones observadas.

        Por ello, los hallazgos identifican tendencias relevantes, aunque no deben interpretarse como relaciones causales definitivas.
        """
    )
