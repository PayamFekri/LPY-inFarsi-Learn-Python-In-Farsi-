#create new columns derived from existing columns
import pandas as pd
titanic = pd.read_csv("titanic.csv")
#reshape the layout Tables
Aq = pd.read_csv("Air_Quality.csv",index_col="Unique ID",parse_dates=True,encoding="unicode_escape")
print(Aq)
print("------------------")
no2_sub = Aq[Aq['Name'] == "Nitrogen dioxide (NO2)"]
print(no2_sub)

print("------------------")
no2_place = no2_sub.sort_index().groupby(["Geo Place Name"]).head(2)# یعنی از هر گروه 2 تا مقدار اولشو که گروه بندی کردی به من بده
print(no2_place)
print("------------------")
#pivot , pivot table , melt for reshaping
place_dataValue=no2_sub.sort_index().pivot(columns= "Geo Place Name", values='Data Value' ).plot()
print(place_dataValue)
print("------------------")
aq0 = Aq.pivot_table(
    values= 'Data Value' ,index= "Geo Place Name" ,columns= 'Name',aggfunc='mean' , margins= True
)
print(aq0)
#aq1 =Aq.groupby(['Name','Geo Place Name']).mean()
#error darad!
print("------ in doo code yeki hastand ###")
#print(aq1)
#aq0 vs aq1 هردو یک جواب را به ما می دهند و تفاوتی باهم ندارند