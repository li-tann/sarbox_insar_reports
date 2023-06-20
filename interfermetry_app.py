import streamlit as st
import pandas as pd
import datetime
import json
import os.path

def streamlit_interf_app(root_path:str):

    st.title("registration & Interference")
    if not os.path.exists(root_path):
        st.warning("{} is unexisted.".format(root_path))
        return

    st.header("registration")

    st.write("include registration points, polynomial formula & rmse")

    st.subheader("registration points")
    df = pd.read_csv(root_path+"/registration_report_points.csv")
    st.dataframe(df)  # Same as st.write(df)

    st.subheader("registration polymonial json")
    f = open(root_path+'/regist_polynomial.json', 'r')
    content = f.read()
    a = json.loads(content)
    azi_cof = a["cofficient"]["azimuth"]
    sr_cof = a["cofficient"]["slant_range"]

# 公式太长, 可能要考虑换行
    st.write("the registration polymonial from master to slave is,")
    azimuth_latex = "\delta_{{azi}}={0:.4f}+{1:.2e}*azi +{2:.2e}*sr+{3:.2e}*azi^2+{4:.2e}*sr^2+{5:.2e}*azi*sr".format(azi_cof[0], azi_cof[1], azi_cof[2], azi_cof[3], azi_cof[4], azi_cof[5])
    # print(azimuth_latex)
    st.latex(azimuth_latex)

    slant_range_latex = "\delta_{{sr}}={0:.4f}+{1:.2e}*azi +{2:.2e}*sr+{3:.2e}*azi^2+{4:.2e}*sr^2+{5:.2e}*azi*sr".format(azi_cof[0], azi_cof[1], azi_cof[2], azi_cof[3], azi_cof[4], azi_cof[5])
    # print(azimuth_latex)
    st.latex(slant_range_latex)

    st.write("the rmse about registration polymonial from master to slave is,")
    st.json(a["rmse"])

    st.header("interference")

    st.write("include interference & coherence map and statistic chart")

    st.subheader("image of interference")

    st.write("there is a interference thumb map")

    st.subheader("image of coherence")

    st.write("there is a coherence thumb map")

    st.write("there is a coherence percentage chart")