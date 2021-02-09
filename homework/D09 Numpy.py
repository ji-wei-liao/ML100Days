import pandas as pd


f=open('boston.csv')
data=pd.read_csv(f,usecols=['CHAS','NOX','RM'])
data.to_excel('boston.xlsx')


