import streamlit as st
import pandas as pd
import datetime
import json
import os.path

def streamlit_lut_app(root_path:str):

    st.title("Lookup Table")
    if not os.path.exists(root_path):
        st.warning("{} is unexisted.".format(root_path))
        return

    st.write("lookup table is uncomplete.")
