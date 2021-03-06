# -*- coding: utf-8 -*-
"""Predict Future Prices Using Facebook Prophet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H1r3uJbFVYqtWBrLES-vUl2tslaUm8oA

# PREDICTING FUTURE PRODUCT PRICES USING FACEBOOK PROPHET

# TASK 2: IMPORT LIBRARIES AND DATASET

- install fbprophet package:

   `  pip install fbprophet`
     
- If encounter an error, try: 

    `conda install -c conda-forge fbprophet`
"""

# import libraries 
import pandas as pd  #  Pandas for data manipulation using dataframes
import numpy as np   #  Numpy for data statistical analysis 
import matplotlib.pyplot as plt # matplotlib for data visualisation
import random
import seaborn as sns
from fbprophet import Prophet
from fbprophet.plot import plot

# dataframes creation for both training and testing datasets 
df_avocado=pd.read_csv("https://raw.githubusercontent.com/tsheng0315/Projects-on-CV/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/data/avocado.csv")

"""- Date: The date of the observation
- AveragePrice: the average price of a single avocado
- type: conventional or organic
- year: the year
- Region: the city or region of the observation
- Total Volume: Total number of avocados sold
- 4046: Total number of avocados with PLU 4046 sold
- 4225: Total number of avocados with PLU 4225 sold
- 4770: Total number of avocados with PLU 4770 sold
"""

# Let's view the head of the training dataset
df_avocado.head()

# Let's view the last elements in the training dataset
df_avocado.tail(10)

df_avocado.describe()

df_avocado.info()

# check the existence of null element in table
df_avocado.isnull().sum()

"""# TASK #3: EXPLORE DATASET"""

# sort the records according to data
df_avocado.sort_values('Date',inplace=True)

# Plot date and average price
plt.figure(figsize=(8,8))
plt.plot(df_avocado['Date'], df_avocado['AveragePrice'])
plt.show()

# Plot distribution of the average price
# plt.figure(figsize=(10,17)).show()
# plt.figure(figsize=(15,8))

g=sns.displot(data=df_avocado,x="AveragePrice",kde=True)
g.set_axis_labels("Average Price", "Count")
g.set_titles("penguins")
g.fig.set_size_inches(10,6)
plt.show()

# Plot a violin plot of the average price vs. avocado type
g=sns.violinplot(data=df_avocado,x='type',y="AveragePrice")
plt.show()

# Bar Chart to indicate the number of regions 

sns.set(font_scale=0.7) 
plt.figure(figsize=[25,6])
sns.countplot(x = 'region', data = df_avocado)
plt.xticks(rotation = 45)

# Bar Chart to indicate the count in every year to see whether data equally recorded among years or not
sns.set(font_scale=1.5) 
plt.figure(figsize=[10,6])
sns.countplot(x = 'year', data = df_avocado)
plt.xticks(rotation = 45)
plt.show()

df_avocado['type']=='conventional'

# plot the avocado prices vs. regions for conventional avocados
conventional=sns.catplot(x='AveragePrice', y='region',hue='year',data=df_avocado[df_avocado['type']=='conventional'],height=20,legend=True)

# plot the avocado prices vs. regions for organic avocados

conventional=sns.catplot(x='AveragePrice', y='region',hue='year',data=df_avocado[df_avocado['type']=='organic'],height=20,legend=True)

"""# TASK 4: PREPARE THE DATA BEFORE APPLYING FACEBOOK PROPHET TOOL"""

df_avocado

df_avocado_prophet=df_avocado[['Date','AveragePrice']]
df_avocado_prophet

type(df_avocado['Date'])

df_avocado_prophet=df_avocado_prophet.rename(columns={'Date':'ds','AveragePrice':'y'})
df_avocado_prophet

"""# TASK 5: UNDERSTAND INTUITION BEHIND FACEBOOK PROPHET

# TASK 6: DEVELOP MODEL AND MAKE PREDICTIONS - PART A
"""

# fit model with trainning data
m=Prophet()
m.fit(df_avocado_prophet)

# Forcasting into the future
# By default it will also include the dates from the history, so we will see the model fit as well.
future=m.make_future_dataframe(periods=365)
future

forecast = m.predict(future)
forecast

fig=m.plot(forecast,xlabel='Date',ylabel='Price')

fig2=m.plot_components(forecast)

"""# TASK 7: DEVELOP MODEL AND MAKE PREDICTIONS (REGION SPECIFIC) - PART B"""

# dataframes creation for both training and testing datasets 
df_avocado

# Select specific region
df_avocado_west=df_avocado[df_avocado['region']=='West']

df_avocado_west=df_avocado_west.sort_values('Date')

# plot to give a general idea of what the trend is. 
plt.plot(df_avocado_west['Date'],df_avocado_west['AveragePrice'])

df_avocado_west=df_avocado_west.rename(columns={'Date':'ds','AveragePrice':'y'})
df_avocado_west



m = Prophet()
m.fit(df_avocado_west)
# Forcasting into the future
future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)

figure = m.plot(forecast, xlabel='Date', ylabel='Price')
# the price will actually go up here in west of US

figure3 = m.plot_components(forecast)