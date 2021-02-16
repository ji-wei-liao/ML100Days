import pandas as pd
stock_data1=pd.read_csv('STOCK_DAY_0050_202009.csv')
#print (stock_data1)

stock_data2=pd.read_csv('STOCK_DAY_0050_202010.csv')
#print (stock_data2)

stock_data=pd.concat([stock_data1,stock_data2],axis=0,join='inner')
#print(stock_data)

stock_idx=stock_data.loc[(stock_data.open<stock_data.close)]

print(stock_idx)