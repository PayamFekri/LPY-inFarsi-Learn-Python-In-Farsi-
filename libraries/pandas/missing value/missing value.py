import pandas as  pd
import numpy as np
#----------------------------------------
#missing value 
#مقداری در دیتا ست که ما نداریم
missing_values = [" "]
diabet =pd.read_csv("diabet.csv",na_values= missing_values)

######diabet.dropna(axis=0, inplace=True,how="any" )
print("-------------------------")
# filling with median , mode , mean
#diabet["Diastolic_BP"].fillna(diabet["Diastolic_BP"].median(),inplace=True)
#diabet["Diastolic_BP"].fillna(diabet["Diastolic_BP"].mode(),inplace=True)
#diabet["Diastolic_BP"].fillna(diabet["Diastolic_BP"].mean(),inplace=True)
#print(diabet)
print("-------------------------")
#با یک مقدار دلخواه میسینگ هارو پر کنیم 

#diabet["Diastolic_BP"].fillna(100,inplace=True)
#print(diabet)
print("-------------------------")
#با مقدار بعدیش پر کن 
#back fill
#diabet["Diastolic_BP"].fillna(method= "bfill" , inplace=True)

#-------------------------
#با مقدار قبلیش پر کن 
#forward fill
#diabet["Diastolic_BP"].fillna(method= "ffill" , inplace=True)
#print(diabet)

#linear interpolation = درون یابی خطی
#diabet["Diastolic_BP"].interpolate(method= "linear" , inplace=True)
#print(diabet)

diabet["Diastolic_BP"].interpolate(method= "polynomial",order= 2 , inplace=True)
print(diabet)

print("-------------------------")
#####split data inti groups
