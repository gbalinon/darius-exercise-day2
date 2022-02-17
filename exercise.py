import streamlit as st
import pandas as pd
import numpy as np
import time
import seaborn as sns
import matplotlib.pyplot as plt

st.write("Select task from the sidebar")

@st.cache
def get_input():
    data = pd.read_csv("diamonds_regression.csv")
    return data

df = get_input()

chart_data = df[['carat', 'price']]

#@st.cache
def plot_line_sns():
    fig = plt.figure(figsize=(10, 4))
    sns.lineplot(x = "carat", y = "price", data = chart_data)
    st.pyplot(fig)


#@st.cache
def plot_pair_sns():
    columns = ['carat', 'price']
    fig2 = sns.pairplot(df[['carat', 'price']])
    st.pyplot(fig2)

if st.sidebar.checkbox ("show data frame"):
    df
    
if st.sidebar.checkbox ("show line graph"):
    plot_line_sns()
    
if st.sidebar.checkbox ("show pair plot"):
    plot_pair_sns()
    

