#matplotlib in pandas 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data_scat = {
    'Unemployment_rate' :[6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2]
    ,'Stock_index_Price' : [1500,1520, 1525,1523,1515,1540,1545,1560,1555,1565]
}
df1 = pd.DataFrame(data_scat,columns=['Unemployment_rate','Stock_index_Price'])
#df1.plot(x= 'Unemployment_rate', y = 'Stock_index_Price' ,kind = 'scatter' )
#plt.show()
#df1.plot(x= 'Unemployment_rate', y = 'Stock_index_Price' ,kind = 'line' )
#-----------------------
data_bar = {
    'Country' : ['USA', 'Canada' , 'Germany' , 'UK', 'France'],
    'GDP_per_Country' : [45000,42000,52000,49000,47000]
}
df2 = pd.DataFrame(data_bar,columns=['Country','GDP_per_Country'])
#df2.plot(x="Country",y='GDP_per_Country', kind='bar')
#plt.show()
#-----------------------
df4 = pd.DataFrame({'mass': [0.330, 4.87 , 5.97],
                    'radius': [2439.7, 6051.8, 6378.1]},
                  index=['Mercury', 'Venus', 'Earth'])
#plot = df4.plot.pie(y='mass', figsize=(5, 5))

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
#plt.pie(y, labels = mylabels, explode = myexplode,shadow = True)#explode : باعث جداسازی بخش اپلز میشود
#plt.show()

data_stacker =  {
    'DATE' : ['1.1','2.1','3.5','5.2','7.12' , '12.27', '6.23','10.10','3.10', '11.15','9.7']
    ,'TYPE' : ['A','B','C','A','B','C','B','A','B','B','C']
    ,'SALES' : [1000,200,300,400,1000,700,200,300,700,400,500]
}

df5 = pd.DataFrame(data_stacker,columns=['DATE','TYPE','SALES'])
print(df5)
print('------------------------')
#df5.plot(kind="bar",x = "DATE" , y="SALES")
df5.groupby(["DATE" , "TYPE"]).sum().unstack().plot(kind="bar",y = "SALES",width=1)
a = df5.groupby(["DATE" , "TYPE"]).sum().unstack().fillna(0)
print(a)
fig , ax =plt.subplots()
colors = ["#F0E68C","#D3D3D3","#87CEFA"] 
print(a.columns)
plt.show()

#-----------------------------------------
#handle Time Series Data
import pandas as pd
import matplotlib.pyplot as plt
tsdb = pd.read_csv('timeseries.csv')
print(tsdb) 
tsdb =tsdb.rename(columns={'Date':'datetime'})
print('-------\n',tsdb)
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