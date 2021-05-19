import streamlit as st

st.title("This is a webpage")

title = st.text_input("Title")

description = st.text_area("Description")

col1,col2,col3,col4 = st.beta_columns(4)
with col1:
    st.text('   ')
with col2:
    st.text(' ')
with col3:
    mmg = st.button("Paste Bin",help="This will move your file to paste bin")
with col4:
    st.text(' ')

