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
#---------------------------------------------
#select subset of a dataframe
#titanic database
titanic = pd.read_csv("titanic.csv")
print(titanic)
print("-------------------------")
#specific columns of data frame
ages = titanic["Age"]
print(ages)
print("-------------------------")
#specific columns of data frame
ages = titanic["Age"].shape
print(ages)
print("-------------------------")
print(type(titanic["Age"]))
print("-------------------------")
#نمایش دو ستون
two_column = titanic[["Age","Fare"]] 
print(two_column)
print(type(two_column))
print("-------------------------")
above_35 = titanic[titanic["Age"]>35]
print(above_35,"### ages > 35 from titanic")
print("-------------------------")
classes0_2va3 = titanic[titanic["Pclass"].isin([2,3])]
print(classes0_2va3,"### az Pclass una ke 2,3 hastan ro namayesh bede")
print("hardo code yek natije ro midahand")
classes1_2va3 = titanic[(titanic["Pclass"]== 2 )| (titanic["Pclass"]== 3 )]
print(classes1_2va3,"### az Pclass una ke 2,3 hastan ro namayesh bede")
print("-------------------------")
titanic_ages_no_nan = titanic[titanic["Age"].notna()]
print(titanic_ages_no_nan)
print("-------------------------")
titanic_1_ages_no_nan = above_35[above_35["Age"].notna()]
print(titanic_1_ages_no_nan,"ham bala tar az 35 va ham nan ha az 'Age' hazf shodand")
print("-------------------------")
#specific rows & columns from DF
adult_Names = titanic.loc[titanic["Age"]>35,"Name"]
#اسم مسافر های با سن بالاتر از 35 رو جمع اوری می کند 
print(adult_Names)
print(" ")
print(adult_Names[6])
print(" ")
print(adult_Names.index)
print("-------------------------")
#Rows of 10 to 25 and cols from 3 to 5
newtitan = titanic.iloc[9:26 , 2:6]# [Rows , Columns]
print(newtitan)
print("-------------------------")
titanic.iloc[0:3,10] = "C-payam"
print(titanic, " ezafe kardan meghdar be yek record")
#-----------------------------------------

#Group by
# بر حسب یک از ستون ها می توانیم گروه تشکیل دهیم
# split = تقسیم مجموعه داده به یکسری گروه
# applying function = انجام کار های اماری 
# combining the result


diabet = pd.read_csv("Diabetes Missing Data.csv")
print(diabet)
print(type(diabet))
print("-------------------------")
#####split data inti groups
data ={
    'team' :['a','b','c','d','e','f','g','h'],
    'rank' :[ 1,  2,  2,  3,  1,  4,  2,  3],
    'year' :[2014,2015,2014,2020,2019,2018,2012,2027],
    'points':[897,789,650,770,900,820,np.nan,699]
}
df = pd.DataFrame(data)
print(df.groupby("team").groups)
print("-------------------------")
print(df.groupby(["year","team"]).groups)
print("-------------------------")
grouped = df.groupby('year')
print(grouped.groups)
print("-------------------------")
for name , group in grouped:
    print((name),(group))
print("-------------------------")
print(grouped.get_group(2014))
print("-------------------------")
print(grouped.get_group(2014)['team'][2])
print("-------------------------")
#### applying function 
#aggregation function
print(grouped['points'].agg(np.mean))
print("---------")
print(grouped['points'].agg(np.size))
print("\n#######size : have missing // count : without missing",
      "\nif (don't have missing):"
      "\n   n(size) = n(count)")
print(grouped['points'].count())
print("-------------------------")
print(grouped['points'].agg([np.sum,np.mean,np.std]))
print("-------------------------")
#Transformation
score = lambda x : x*2# مقادیر در گروپد را دو برابر کن
score1 = lambda x : x*1 # خوده گروپد است
print(grouped.transform(score1))
print()
print(grouped.transform(score))
print(grouped['points'].transform(score))
print(grouped.filter(lambda x : len(x)>= 2))