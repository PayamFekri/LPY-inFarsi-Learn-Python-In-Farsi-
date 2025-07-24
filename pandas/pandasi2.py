#join in pandas:join,merge,concatination
#innner join , outer join ,  left join , right join
#زمانی میخواهیم عملیات ترکیب را در اندیس ها انجام دهیم بهتر است از جوین استفاده کنیم
import pandas as pd
df1 = pd.DataFrame({
    'key' :['k0','k1','k2','k3','k4','k5'],
    'A' :  ['A0','A1','A2','A3','A4','A5']
})

df2 = pd.DataFrame({
    'key' :['k0','k1','k2'],
    'B' :  ['B0','B1','B2']
})
print(df1.join(df2,lsuffix='_caller' , rsuffix='_other'))
print(df1.join(df2.set_index('key'),on='key'))
print('-----------------------------')
# Merge function
#دقیقا ستون چپ و راست را که روی ان عملیات می کنیم می توان در آن انتخاب کرد 
dfm1 = pd.DataFrame({
    'L-key' :['A','B','C','F'],
    'Value' :  [1,2,3,4]
})

dfm2 = pd.DataFrame({
    'R-key' :['A','B','C','D'],
    'Value' :  [4,5,6,7]
})
print(dfm1.merge(dfm2,left_on='L-key' , right_on='R-key',how='inner'))#inner join - default
print('---')
print(dfm1.merge(dfm2,left_on='L-key' , right_on='R-key',how='left'))#left join
print('---')
print(dfm1.merge(dfm2,left_on='L-key' , right_on='R-key',how='right'))#right join
print('-----------------------------')
#concat function - چسباندن(الحاق)
#concatination : in concat we do NOT have #left or #right join
#just have #inner or #outer(default) join
dfc1 = pd.DataFrame({
    'key' :['B','B','A','C'],
    'Value1' :  [1,2,3,4]
})

dfc2 = pd.DataFrame({
    'key' :['A','B','D'],
    'Value2' :  [1,2,3]
})

print(pd.concat([dfc1,dfc2]))

#-------------------------------------------
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
