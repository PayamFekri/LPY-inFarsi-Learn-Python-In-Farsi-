#OrderedDict
'''
چه زمانی از OrderedDict استفاده کنیم؟
اگر کد شما فقط نیاز دارد که آیتم‌ها را به همان ترتیبی که وارد شده‌اند بخواند، از همان dict معمولی استفاده کنید (چون سریع‌تر است و حافظه کمتری می‌گیرد).

اما در این موارد از OrderedDict استفاده کنید:

وقتی ترتیب آیتم‌ها در مقایسه (Comparison) حیاتی است.
وقتی نیاز دارید ترتیب را جابجا کنید (مثلاً در ساخت سیستم‌های Cache که باید آیتم‌های قدیمی را به انتها بفرستید تا حذف شوند - الگوی LRU).
وقتی می‌خواهید کدتان برای نسخه‌های بسیار قدیمی پایتون هم کار کند.
'''

from collections import OrderedDict
od1 = OrderedDict([('a', 1), ('b', 2)])
programmers = OrderedDict()
programmers['Tim'] = ['python', 'javascript']
programmers['Sarah'] = ['C++']
programmers['Bia'] = ['Ruby', 'Python', 'Go']

print(f'{programmers}\n {od1}')