import pandas as  pd
import numpy as np

#یک کتابخانه ایجاد کنیم کلا
df = pd.DataFrame(
    {
        "Name" : ["Hamid","ALi","Marzie"],
        "Age"  : [  22,    30,     18   ],
        "Sex"  : ["male","male","female"]
    }
)

(df.describe(include='number'))#for numberical data

(df.describe(include='all'))#for both numberical and textual data

(df["Name"])

#یک ستون بسازیم در حالت کلی
a = pd.Series([34,23,56], name = "integer number")

(df['Age'].max())
(df.describe()) #summary description

s = pd.Series(np.random.randn(10))
(s)
s[::2] = np.nan
(s[::2],'ineeeweeeeeeeeeeeeee')

print(s.describe())

b = pd.DataFrame(np.random.randn(10,5),columns=['a','b','c','d','e'])
(b)
(b.describe())

f = pd.Series(['a','a','a','a','a','b','b',np.nan,'d']).describe()
print(f)
print("-----------------------")
#argmin and argmax in numpy = idxmin and idxmax in pandas
s1 = pd.Series(np.random.randn(5))
print(s1)
print(s1.idxmax(),s1.idxmin())#اندیس بزرگترین و کوچکترین را برمیگرداند

print("-----------------------")
df1 = pd.DataFrame(np.random.randn(5,3),columns=['A','B','C'])
print(df1)
print(df1.idxmin(axis=0))# کمترین عدد رو در هر ستووون بدست بیار
print(df1.idxmax(axis=1))#بزرگترین عدد رو در هر سطررر بدست بیار
#---------------------------------------

afg = pd.read_csv("afghan bank.csv")
print(afg)
print("--------------------------------")
print(afg.iloc[15])
print("--------------------------------")
print(afg[5:10])
print("--------------------------------")
print(afg.tail(4))
print("--------------------------------")
#assign() : merging the result of the calculation to the DF
print(afg.assign(col_b_d = afg["birth rate"]/ afg["death rate"]))# همه ستون را اول و همه ستون دوم را می گیرد و بعد بر هم تقسیم می کند
print("beyn 2 merge ")
print(afg.assign(col_b_d = lambda x : (x["birth rate"]/ x["death rate"])))# سطر به سطر درایه ها را بر هم تقسیم می کند 
# دو دستور بالا یک نتیجه را می دهند 
print("--------------------------------")
#ًQuery over the DataSet
print(afg.query("GDP>15856600000"))
print("--------------------------------")
print(afg.query("GDP>15856600000").assign(
    GDP_tarakomJamiiat = lambda x : (x["GDP"]/x["tarakom jamiat"])
        )
      )
print("--------------------------------")
print(afg.query("GDP>15856600000").assign(
    GDP_tarakomJamiiat = lambda x : (x["GDP"]/x["tarakom jamiat"]),
    useInternet_unempolyment= lambda x :(x["use internet"]/x["Unemployment"])
        )
    )
print("--------------------------------")
new_afghan = afg.query("GDP>15856600000").assign(
    GDP_tarakomJamiiat = lambda x : (x["GDP"]/x["tarakom jamiat"]),
    useInternet_unempolyment= lambda x :(x["use internet"]/x["Unemployment"])
        ).plot(kind="scatter" ,x = "GDP_tarakomJamiiat" , y = "useInternet_unempolyment")#اینجا باید یک نمودار نقطه ای بما بدهد که محور x , y آن مشخص است
print(new_afghan)
print("--------------------------------")
df = pd.DataFrame(
    {
        "Name" : ["Hamid","ALi","Marzie"],
        "Age"  : [  22,    30,     18   ],
        "Sex"  : ["male","male","female"]
    }
)
#برای سیو کردن یک دیتا فریم
#df.to_csv("mydf.csv")
#df.to_csv("mydf.csv",index=False) اندیس هاس اضافه را دیگر ندارد
dfa = pd.DataFrame(
    {
    "A" : [1,2,3],
    "B" : [4,5,6]
    }
)
print(dfa)
print("--------------------------------")
dfaPLUS = dfa.assign(C = lambda x : x["A"]+ x["B"],D = lambda x : x["A"]+ x["C"])
print(dfaPLUS)
print("--------------------------------")
#--------------------------------------------
#missing value 
#مقداری در دیتا ست که ما نداریم
missing_values = [" "]
diabet =pd.read_csv("diabet.csv",na_values= missing_values)
print(diabet)
print("-------------------------")
print("bayad az comment code ha ro kharej koniii ta natije neshun dade beshe")
#two solution for handle missing values : 
#1-remove the row/s which has/have missing values
#2-filling out the missing values
######diabet.dropna(axis=0, inplace=True,how="any" )
#inplace :همین تغییرات رو روی همین دیتا فریم ایجاد کن
#how="any" : سطری رو پاک کن که حداقل یک nan  داشته باشد
#how="all" : هر سطری که همه مقادیر ان nan دارد رار حذف کن 
#axis = 0 :  سطر 
#axis = 1 :  ستون
#print(diabet)# nan دار ها حذف شدند
print("-------------------------")
print("bayad az comment code ha ro kharej koniii ta natije neshun dade beshe")
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

