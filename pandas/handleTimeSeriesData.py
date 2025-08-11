#handle Time Series Data
import pandas as pd
import matplotlib.pyplot as plt
tsdb = pd.read_csv('timeseries.csv')
print(tsdb) 
tsdb =tsdb.rename(columns={'Date':'datetime'})

tsdb['datetime'] = pd.to_datetime(tsdb['datetime'])
print('-------\n',tsdb['datetime'])
min = tsdb['datetime'].min()#کمترین زمان را برمیگرداند
max = tsdb['datetime'].max()
print('-------\n',max - min)#کل طول زمان
tsdb['month']  = tsdb['datetime'].dt.month#ستون اضافه می کنیم برای نمایش ماه 
print('-------\n',tsdb)
print(tsdb.groupby([tsdb['datetime'].dt.weekday])['A'])
fig , axs = plt.subplots(figsize = (5,2))
plt.xlabel('time')
plt.ylabel('TSDB')
print(tsdb.groupby([tsdb['datetime'].dt.weekday])['A'].mean().plot(kind='bar',ax= axs))
#plt.show()
tsdb.pivot(index='datetime', columns='A',values='B')
#plt.show()
monthly_resampled_data = tsdb.close.resample('M').mean() 
print('-------\n',monthly_resampled_data)