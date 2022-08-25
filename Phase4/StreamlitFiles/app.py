import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt

st.write('# Hello World!')

st.write('## Hello You!')

df = pd.read_csv('../data/Austin_Animal_Center_Intakes_080422.csv')

st.write(df.head())

column = st.selectbox(
    label='This chooses what column to visualize',
    options=['Animal Type', 'Intake Type']
)

if st.button(label='Click to Visualize'):

    to_plot = df[column].value_counts()

    fig, ax = plt.subplots()
    ax.plot(to_plot.values, to_plot.index)
    #ax.plot(to_plot.values, to_plot.index)
    st.pyplot(fig)