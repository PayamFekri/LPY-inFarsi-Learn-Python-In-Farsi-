import pandas as pd 

df = pd.DataFrame(
    {
    "name" : ['payam','alii','khakham','bandar'],
    "id" :   [1322,    9923,  3452,     4576],
    "number":[915,      912,   914,      917]
    }
)
print(df)
print(df.describe(include=('object','number'))) # =df.describe(include='all')
print(df["id"])
a = pd.Series(['ahmad','hossein', 'yaghoub'], name = "father name")
print(a)