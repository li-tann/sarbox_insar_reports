import streamlit as st
import pandas as pd
import datetime
import json
import os.path

from interfermetry_app import streamlit_interf_app
from lookuptable_app import streamlit_lut_app

if "page" not in st.session_state:
    st.session_state.page = "Page Interf"

root_path = st.sidebar.text_input("input a rootpath to create a insar report")

options = st.sidebar.selectbox(
    'select window',
    ('Page Interf','Page LookupTab','Page Unwarp'),
    key="page")

if not os.path.exists("D:/1_Data/ALOS2/sarbox/interferometry"):
    print("is not exists")


if st.session_state.page == "Page Interf":
    streamlit_interf_app(root_path+"/interferometry")


elif st.session_state.page == "Page LookupTab":
   streamlit_lut_app(root_path + "/lookuptable")

elif st.session_state.page == "Page Unwarp":
    st.title("Phase Unwarp")

st.divider()

st.write("insar project report, @ litan, {}.".format(datetime.datetime.now().strftime('%Y-%m-%d')))