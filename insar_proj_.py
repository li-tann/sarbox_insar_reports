import streamlit as st
import pandas as pd
import json

if "page" not in st.session_state:
    st.session_state.page = "Page Interf"

options = st.sidebar.selectbox(
    'select window',
    ('Page Interf','Page LookupTab','Page Unwarp'),
    key="page")

if st.session_state.page == "Page Interf":
    st.header("Interference")
    st.subheader("registration points")
    df = pd.read_csv("D:/1_Data/ALOS2/sarbox/interferometry/registration_report_points.csv")

    st.dataframe(df)  # Same as st.write(df)

    st.subheader("registration polymonial json")
    f = open('D:/1_Data/ALOS2/sarbox/interferometry/regist_polynomial.json', 'r')
    content = f.read()
    a = json.loads(content)
    st.json(a["cofficient"])
    st.json(a["rmse"])
    st.subheader("registration report")
    st.subheader("interference coherence value")

elif st.session_state.page == "Page LookupTab":
    st.header("LookupTab")

elif st.session_state.page == "Page Unwarp":
    st.header("Unwarp")

st.write("InSAR Project")