import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('processed_daat3.csv', sep=',')  

print(df)

st.header("Exploratory Data Analysis")
# Histogram of car prices
fig = px.histogram(df, x='price', title='Histogram of Car Prices')  
st.plotly_chart(fig)

#Scatterplot
fig = px.scatter(df, x='odometer', y='price', title='Scatterplot of Price vs. Odometer')  
st.plotly_chart(fig)



if st.checkbox('Show Histogram'):
    fig = px.histogram(df, x='model_year')
    st.plotly_chart(fig)



