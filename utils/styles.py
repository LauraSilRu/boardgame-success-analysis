import streamlit as st
from utils.config import *
import base64

def get_base64_image(image_path):

    with open(image_path, "rb") as img_file:
        return base64.b64encode(
            img_file.read()
        ).decode()
    
parchment_bg = get_base64_image(
    "assets/parchment.jpg"
)

def load_css():
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>

    h1, h2, h3 {

        font-family: 'Cinzel', serif !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <style>

    .stApp {{

        background-image:
            linear-gradient(
                rgba(246,241,221,0.40),
                rgba(246,241,221,0.40)
            ),
            url("data:image/jpeg;base64,{parchment_bg}");

        background-size: cover;

        background-attachment: fixed;

        background-position: center;
    }}

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <style>

        .main {{
            background-color: {BACKGROUND_COLOR};
        }}

        .block-container {{
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }}

        h1 {{
            color: {PRIMARY_COLOR};
            font-weight: 700;
        }}

        h2, h3 {{
            color: {PRIMARY_COLOR};
        }}

        [data-testid="stMetricValue"] {{
            color: {PRIMARY_COLOR};
            font-size: 2rem;
            font-weight: 700;
        }}

        [data-testid="stMetricLabel"] {{
            font-size: 1rem;
            font-weight: 600;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <style>

    /* ==================================================
    LAYOUT GENERAL
    ================================================== */

    .main {
        padding-top: 1rem;
    }

    .block-container {
        padding-top: 2rem;
    }

    h1, h2, h3 {
        color: #1E3A5F;
    }

    /* ==================================================
    SIDEBAR
    ================================================== */

    [data-testid="stSidebar"] {

        background: linear-gradient(
            180deg,
            #16304D 0%,
            #1E3A5F 50%,
            #2B4C7E 100%
        );

        border-right: 1px solid rgba(255,255,255,0.08);
    }

    /* Texto general sidebar */

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {

        color: white !important;
    }

    /* Selectbox */

    [data-testid="stSidebar"] [data-baseweb="select"] {

        background: white !important;

        border-radius: 12px;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] * {

        color: #1E3A5F !important;
    }

    /* Slider */

    [data-testid="stSidebar"] .stSlider {

        padding-top: 10px;
    }

    /* Separadores */

    [data-testid="stSidebar"] hr {

        border: none !important;

        height: 1px !important;

        background: rgba(255,255,255,0.15) !important;
    }

    /* ==================================================
    KPI CARDS
    ================================================== */

    div[data-testid="stMetric"] {

        background: linear-gradient(
            135deg,
            #1E3A5F,
            #355C8A
        );

        padding: 20px;

        border-radius: 18px;

        box-shadow:
            0px 4px 12px rgba(0,0,0,0.12);

        text-align: center;
    }

    [data-testid="stMetricLabel"] {

        visibility: visible !important;

        justify-content: center !important;

        width: 100% !important;
    }

    [data-testid="stMetricLabel"] p {

        color: rgba(255,255,255,0.95) !important;

        font-size: 15px !important;

        font-weight: 600 !important;

        text-align: center !important;

        white-space: normal !important;

        overflow: visible !important;

        text-overflow: unset !important;
    }

    [data-testid="stMetricValue"] {

        color: white !important;

        font-size: 2.5rem !important;

        font-weight: 700 !important;

        justify-content: center !important;
    }

    # /* ==================================================
    #    GRÁFICOS
    #    ================================================== */

    # [data-testid="stPlotlyChart"] {

    #     background: white;

    #     border-radius: 20px;

    #     padding: 15px;

    #     box-shadow:
    #         0px 4px 12px rgba(0,0,0,0.08);
    # }

    /* ==================================================
    ALERTAS / INSIGHTS
    ================================================== */

    [data-testid="stAlert"] {

        background: #F6F1DD;

        border-left: 5px solid #C9A227;

        border-radius: 18px;

        box-shadow:
            0px 4px 12px rgba(0,0,0,0.08);
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>

    /* Oculta anclas de Streamlit */

    h1 a,
    h2 a,
    h3 a {

        display: none !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>

    [data-testid="stSidebar"] .stSelectbox p {
        color: #1E3A5F !important;
        opacity: 1 !important;
    }

    [data-testid="stSidebar"] .stSelectbox svg {
        color: #1E3A5F !important;
    }

    /* ==================================================
    TABLAS
    ================================================== */

    [data-testid="stTable"] table {

        background-color: rgba(244,236,210,0.95);

        border-radius: 12px;

        overflow: hidden;

        border-left: 4px solid #D4A017;

        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    [data-testid="stTable"] th {

        background-color: #2D4A66 !important;

        color: white !important;

        font-weight: 700 !important;

        text-align: left !important;
    }

    [data-testid="stTable"] td {

        background-color: rgba(244,236,210,0.95) !important;

        color: #2D4A66 !important;
    }

    </style>
    """, unsafe_allow_html=True)

    pass