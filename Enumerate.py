# Enumerate :در پایتون،  برای شماره‌گذاری روی اعضای یک iterable استفاده می‌شود و هم‌زمان اندیس/شماره و مقدار را به شما می‌دهد.
# Enumerate: In Python, it is used to number the members of an iterable, giving you the index/number and the value at the same time.
for i, el in enumerate('payam'):
  print(f'{i}, {el}')
  
items = ["apple", "banana", "orange"]
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
    