import streamlit as st


st.header('THE BUTTON')

if st.button('HIPPO'):
    st.write('HIPPO')
else:
    st.write('RHINO')