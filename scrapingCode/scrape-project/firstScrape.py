from bs4 import BeautifulSoup as bs
import re

source = open('DivarText.html','r',encoding='utf-8').read()

soup = bs(source,'html.parser')
extract = soup.find_all('div',attrs={'class':"kt-post-card__info"})
soup = bs(str(extract),'html.parser')
titles = soup.find_all('h2' ,attrs={'class':"kt-post-card__title"})

#<div class="kt-post-card__info">
#   <h2 class="kt-post-card__title">سویت اجاره ای پارکینگ دارشهر درود دررود</h2>
#   <div class="kt-post-card__description">۲ اتاق, تا ۱۴ نفر</div>
#   <div class="kt-post-card__description">از ۶۰۰,۰۰۰ تومان</div>
#   <div class="kt-post-card__bottom">
#       <span class="kt-post-card__red-text">پله شده</span>
#       <span class="kt-post-card__bottom-description kt-text-truncate" title="مشاور سید مجید موسوی باباصالح در نیشابور">مشاور سید مجید موسوی باباصالح در نیشابور</span>
#   </div>
# </div>




#print(extract,'\n--------------')
print(titles)
