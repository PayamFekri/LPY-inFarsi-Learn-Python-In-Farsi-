import re


#1. re.IGNORECASE یا re.I
# بی‌توجهی به کوچکی/بزرگی حروف (Case-insensitive)
text = "Hello world"
match = re.search(r"hello", text, re.IGNORECASE)
print('1',(match))
print(bool(match),'\n')


#2.re.MULTILINE یا re.M
# فعال کردن رفتار چندخطی — ^ و $ برای هر خط
text = """first line
second line"""
# فقط وقتی ^ روی هر خط عمل کنه، second پیدا میشه
match = re.findall(r"^second", text, re.MULTILINE)
print('2',match,'\n')


#3.re.DOTALL یا re.S
#علامت . همه‌چیز از جمله newline رو هم شامل میشه
text = "Hello\nWorld"
match = re.search(r"Hello.*World", text, re.DOTALL)
print(bool(match))  #(بدون DOTALL فقط "Hello" رو می‌گیره)
print('3',match,'\n')


#4.re.VERBOSE یا re.X
#نوشتن regex با کامنت و فاصله برای خوانایی بهتر
pattern = re.compile(r"""
    \d{3}     # Area code
    -         # Hyphen
    \d{3}
    -\d{4}    # Line number
""", re.VERBOSE)
match = pattern.fullmatch("123-456-7890")
print(bool(match))
print('4',match,'\n')


#5.re.ASCII یا re.A
#محدود کردن تطبیق به کاراکترهای ASCII فقط
text = "à"  # یک حرف یونیکد

# \w با re.ASCII فقط A-Z, a-z, 0-9 و _ رو شامل میشه
match = re.match(r"\w", text, re.ASCII)
print(bool(match))
print('5',match,'\n')

#6.ترکیب چند فلگ با | (OR)
pattern = re.compile(r"hello.*world", re.IGNORECASE | re.DOTALL)
text = "HELLO\nworld"
print(bool(pattern.search(text)))
print('6',(pattern.search(text)))