# namedtuple :  استفاده می‌کنیم تا داده‌های کوچک و ثابت‌مان را “نام‌گذاری” کنیم تا کد هم تمیزتر باشد و هم کار با آن راحت‌تر.
# namedtuple : We use namedtuple to "name" our small, constant data to make the code both cleaner and easier to work with.from collections import namedtuple
from collections import namedtuple
Point = namedtuple('Point', 'x y')
p = Point(1, y=2)# Point(x=1, y=2)
print(p[0])             # 1
print(p.x)              # 1
print(getattr(p, 'y'))  # 2
print(p._fields)        # Or: Point._fields #('x', 'y')
