## Load packages 
import streamlit as st
import pandas as pd
import plotly.express as px

## Load data
df = pd.read_csv('processed_daat3.csv', sep=',')  

print(df)


st.header("Exploratory Data Analysis")
# Histogram of car prices
fig = px.histogram(df, x='price', title='Histogram of Car Prices')  
st.plotly_chart(fig)
## The histogram presents the distribution of car prices.
## Most vehicles are priced between $5,000 and $10,000.
## The distribution is right-skewed, meaning there are fewer cars in the higher price range, but there is a small portion of  vehicles priced up to $35,000. 

#Scatterplot
fig = px.scatter(df, x='odometer', y='price', title='Scatterplot of Price vs. Odometer')  
st.plotly_chart(fig)
## There is a negative relatonship between price and odometer. As the odometer increases, the car price tends to decrease.



if st.checkbox('Show Histogram'):
    fig = px.histogram(df, x='model_year')
    st.plotly_chart(fig)



