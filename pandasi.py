#manipulate textual data
import pandas as pd
titanic = pd.read_csv("titanic-string.csv")
print(titanic)
print(titanic['Name'].str.lower())#کوچ کردن حروف
titanic['LAST-NAME'] = titanic['Name'].str.split(',').str.get(0) 
#خط بالا : یک ستون جدید ایجاد کردیم که نام های خانوادگی را در یک ستون مجزا قرار دهد
#get(0) : اولین بخش از سمت چپ رشته تا اولین کاما(,)
print('-----create LAST-NAME column\n',titanic)
edward_S = titanic['Name'].str.contains("Edward")
print('-----find name that is -Edward-\n',
      titanic[edward_S])

print(titanic.loc[titanic['Name'].str.len().idxmax()])
#اون اسمی رو پیدا میکنه که از نظر طول بزرگترین باشه 
#بعد مشخصاتشو نمایش میده


titanic['short-gender'] = titanic['Sex'].replace({'male':'M','female':'F'})
#for preprocessing is the best
print('------\n\n',titanic)
