import streamlit as st

def setStyle():

    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    removePadding = """
            <style>
            .css-12oz5g7 {padding-top: 0;}
            </style>
            """
    st.markdown(removePadding, unsafe_allow_html=True)

    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        width: 100%;
        justify-content: start;
    }
    </style>""", unsafe_allow_html=True)

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    btnTransicao = """
                <style>
                button[value="Salvar"] {
                    background-color: coral;
                }
                </style>
                """
    st.markdown(btnTransicao, unsafe_allow_html=True)

    iframe = """
                <style>
                iframe {
                    height 100px;
                }
                </style>
                """
    st.markdown(iframe, unsafe_allow_html=True)