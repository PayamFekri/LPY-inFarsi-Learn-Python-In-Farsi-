from bs4 import BeautifulSoup as bs

source = open('tables.html','r').read()
soup = bs(source,'html.parser')
title = soup.find('title').get_text()
print(title)
print('--------------------------------')

meta = soup.find('meta',attrs={'name':'keywords'})
print('1',meta)
print('2',meta['content'])

print('--------------------------------')
script = soup.find_all('script',src=True)
print('1',script)
script_without_src = soup.find_all('script',src=False)
print('1"',script_without_src)
print('--------------------------------')
meta2 = soup.find_all('meta',content=True)
for m in meta2:
    print(m['content'])
    
print('--------------------------------')
table = soup.find('table').find('tbody').find_all('tr')
            #table(tbody(tr))
            #az table , tbody ro peyda kon, az tbody ,tr ha ro peyda kon.
            #table , tbody , tr attribute hastand 
for i in table:
    print(i,'\n\n')

for t in table:
    td = t.find_all('td')
    print(td)

for t in table:
    td = t.find_all('td')
    print(td)
    id_ = td[0].getText()
    firstname = td[1].getText()
    lastname = td[2].getText()
    username = td[3].getText()
    print(
        'ID: ',id_,'\n'
        'FirstName: ',firstname,'\n'
        'LastName: ',lastname,'\n'
        'UserName: ',username,'\n'
    )

print('--------------------------------')
source = open('products.html','r').read()
soup = bs(source,'html.parser')

li = soup.find('ul',attrs={'class':"nav" ,'id':'side-menu'}).find_all('li')

for l in li:
    a= l.find('a')
    link = a['href']
    text = a.get_text().strip()
    print(text,':',link,'\n')