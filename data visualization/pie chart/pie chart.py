import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os
df=pd.read_csv('/content/corona_virus.csv')
countries=df.drop('Date',axis=1)
for country in countries.columns:
    fig=px.pie(df,values=country,names='Date',title='Count Infected of '+country)
    fig.show()