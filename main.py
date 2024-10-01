import streamlit as st

a = [3.45, 6.90, 7.97, 9.67, 5.98, 0.56, 5.5, 3.67]

st.title("My test App")
st.write("My plots")
st.line_chart(a)