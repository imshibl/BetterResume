import streamlit as st

st.set_page_config(page_title="Better Resume", page_icon=":memo:", layout="wide")
# favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)


st.title("Better Resume")
st.header("Resume Builder")
pdf_file = st.file_uploader("Select your Resume", type=["pdf"])
