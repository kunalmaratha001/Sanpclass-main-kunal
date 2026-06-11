import streamlit as st

st.write("Available secrets:", list(st.secrets.keys()))
st.stop()