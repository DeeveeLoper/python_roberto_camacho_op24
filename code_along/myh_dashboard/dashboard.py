import streamlit as st
from read_data import read_data
from kpis import approved_precentage, number_approved, total_applications

# --- reading data --
df = read_data()

# --- Dashboard components --
#title
st.markdown("## YH Dashboard 2024 application")

st.markdown("This is a simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can be filtered in this dashboard.")

#kpi components (horizontal layout)
st.markdown("## KPIs in Sweden")

labels = ("Total Applications", "Number of approved", "Approved precentage")
kpis = (total_applications, number_approved, approved_precentage)
cols = st.columns(3)

for col, label, kpi in zip(cols, labels, kpis):
    with col:
        st.metric(label, value=kpi)

#data table
st.markdown("## Raw Data")
st.dataframe(df)