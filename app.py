## Load packages 
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

## Load data
df = pd.read_csv('processed_daat3.csv', sep=',')  
print(df)

### Introduction: The dataset includes car sales advertisements.

st.header("Exploratory Data Analysis")

# Histogram of car prices
hist_price = px.histogram(data3, x='price', title='Histogram of Car Prices')
hist_price.show()


# Histogram of odometer readings
hist_odometer = px.histogram(data3, x='odometer', title='Histogram of Odometer Readings')
hist_odometer.show()


# Scatter plot of price vs odometer
scatter_price_odometer = px.scatter(data3, x='odometer', y='price', title='Scatterplot of Price vs Odometer')
scatter_price_odometer.show()

# Scatter plot of price vs model year
scatter_price_year = px.scatter(data3, x='model_year', y='price', title='Scatterplot of Price vs Model Year')
scatter_price_year.show()

# Count plot for car conditions
hist_condition = px.histogram(data3, x='condition', title='Car Condition Distribution')
hist_condition.show()

# Count plot for fuel type
hist_fuel = px.histogram(data3, x='fuel', title='Fuel Type Distribution')
hist_fuel.show()

# Count plot for transmission types
hist_transmission = px.histogram(data3, x='transmission', title='Transmission Type Distribution')
hist_transmission.show()


# Boxplot of price by condition
box_price_condition = px.box(data3, x='condition', y='price', title='Price by Car Condition')
box_price_condition.show()

# Boxplot of price by fuel type
box_price_fuel = px.box(data3, x='fuel', y='price', title='Price by Fuel Type')
box_price_fuel.show()

# Boxplot of price by transmission
box_price_transmission = px.box(data3, x='transmission', y='price', title='Price by Transmission')
box_price_transmission.show()


# Correlation matrix 
corr_matrix = data3[['price', 'odometer', 'model_year', 'cylinders', 'days_listed']].corr()

# Heatmap matrix
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


if st.checkbox('Show Histogram'):
    fig = px.histogram(df, x='model_year')
    st.plotly_chart(fig)



