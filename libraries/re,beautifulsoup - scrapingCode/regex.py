#RegEx = regular expresion
import re

text0 = 'onextwoyyythreezzfour'
New_Text0 = re.sub('[xyz]+','-',text0)
            #re.sub(chiaro , ba chi,kodum text?)
print(text0,"\n",New_Text0,'\n')


text1 = 'one-two)three#four'
New_Text1 = re.split('[-#!%$^)(]',text1)
            #re.split(chiaro kharej konam?,az kodum matn?)
print(text1,"\n",New_Text1,'\n')


text2 = 'pentest@gmail.com  payamfekri ai text tex tex tax'
result0 = re.match('([\w\-\.]+)@([a-zA-Z]+\.[a-zA-Z]+)',text2)
            #match: فقط ابتدای رشته را بررسی می‌کند.
print('1',result0)
print('2',result0.group(0))
print('3',result0.group(1),'\n')


text3 = 'payamfekri ai pppp1 PenTest@gmail.com  payamfekri ai'
result0 = re.search('([\w\-\.]+)@([a-zA-Z]+\.[a-zA-Z]+)',text3)
             #search : در کل متن میگرده
             #avalain chiz ro ke dar harja peyda kard barmigardune
res = re.search('([\w\-\.]+)@([a-z]+\.[a-z]+)',text3,flags=re.M)#use flags
print(res)

print('1',result0)
print('2',result0.group(0))
print('3',result0.group(1))
print('4',result0.group(2),'\n')


text4 = open('test.txt','r').read()
result1 = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{2,5}',text4)
            #dar kol text har chand ta mojud basha ro namayesh mide
print(result1,'\n')


text5 = open('test.txt','r').read()
pattern = "Price:\s*\$\d{1,7}-\$\d{1,7}"
pattern1 = "Price:\s*\$(\d{1,7})-\$(\d{1,7})"
result2 = re.findall(pattern,text5)
result3 = re.findall(pattern1,text5)
            #findall output ro be surat list barmigardune
print(result2,'\n',result3)
for min_price, max_price in result3:
    print("From:", min_price, "to:", max_price)
