import streamlit as st
import pandas as pd
import datetime
import json
import os.path

def streamlit_interf_app(root_path:str):

    st.title("registration & interfermetry")
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

    azimuth_latex='''
    \\begin{{aligned}}
    \\delta_{{a}} =& {0:+.4f}   \\\\
                     & {1:+.2e}*a \\\\
                     & {2:+.2e}*r  \\\\
                     & {3:+.2e}*a^2 \\\\
                     & {4:+.2e}*r^2 \\\\
                     & {5:+.2e}*a*r
    \\end{{aligned}}
    '''.format(azi_cof[0], azi_cof[1], azi_cof[2], azi_cof[3], azi_cof[4], azi_cof[5])
    st.latex(azimuth_latex)

    slant_range_latex='''
    \\begin{{aligned}}
    \\delta_{{r}} =& {0:+.4f}   \\\\
                     & {1:+.2e}*a \\\\
                     & {2:+.2e}*r  \\\\
                     & {3:+.2e}*a^2 \\\\
                     & {4:+.2e}*r^2 \\\\
                     & {5:+.2e}*a*r
    \\end{{aligned}}
    '''.format(sr_cof[0], sr_cof[1], sr_cof[2], sr_cof[3], sr_cof[4], sr_cof[5])
    st.latex(slant_range_latex)

    st.write("the rmse about registration polymonial from master to slave is,")
    st.json(a["rmse"])

    st.header("interfermetry")

    st.write("include interfermetry & coherence map and statistic chart")

    st.subheader("image of interfermetry")

    st.write("there is a interfermetry thumb map")

    st.subheader("image of coherence")

    st.write("there is a coherence thumb map")

    st.write("there is a coherence percentage chart")