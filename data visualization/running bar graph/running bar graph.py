import pandas as pd
import os
os.chdir("/content")
data_corona=pd.read_csv("/content/corona_virus.csv")
data_corona.head()
cols=['Date','Total','China','Hong Kong','Macau','Taipei','Japan','South Korea','Viet Nam','Singapore','Australia','Malaysia','Cambodia','Philippines','Thailand','Nepal','Sri Lanka','India','USA','Canada','France','Finland','Germany','UAE']
subsetdf=data_corona[cols]
subsetdf.set_index("Date",inplace=True)
import bar_chart_race as bcr
bcr.bar_chart_race(df=subsetdf,filename=None,figsize=(3.5,3),title='COVID-19 CASES')