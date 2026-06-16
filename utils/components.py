import streamlit as st

def section_header(title):

    st.markdown(
        f"""
        <h2 style="
            color:#1E3A5F;
            margin-bottom:20px;
        ">
            {title}
        </h2>
        """,
        unsafe_allow_html=True
    )
    
def insight_card(title, text):

    st.markdown(
        f"""
        <div style="
            background:white;
            border-radius:18px;
            padding:20px;
            box-shadow:0px 4px 12px rgba(0,0,0,0.08);
            margin-bottom:15px;
        ">

            <h4 style="
                color:#1E3A5F;
                margin-top:0;
            ">
                {title}
            </h4>

            <p style="
                color:#374151;
                line-height:1.5;
            ">
                {text}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )