import streamlit as st
import pandas as pd
import datetime
import json
import os.path

from interfermetry_app import streamlit_interf_app
from lookuptable_app import streamlit_lut_app
from unwarp_app import streamlit_unwarp_app

if "page" not in st.session_state:
    st.session_state.page = "Page Interf"

root_path = st.sidebar.text_input("input a rootpath to create a insar report")

options = st.sidebar.selectbox(
    'select window',
    ('Page Interf','Page LookupTab','Page Unwarp'),
    key="page")

if st.session_state.page == "Page Interf":
    streamlit_interf_app(root_path+"/interferometry")


elif st.session_state.page == "Page LookupTab":
   streamlit_lut_app(root_path + "/lookuptable")

elif st.session_state.page == "Page Unwarp":
    streamlit_unwarp_app(root_path + "/unwarp")

st.divider()

st.write("insar project report, @ litan, {}.".format(datetime.datetime.now().strftime('%Y-%m-%d')))