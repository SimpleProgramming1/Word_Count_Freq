


from bs4 import BeautifulSoup
import urllib.request

page= urllib.request.urlopen('https://statecancerprofiles.cancer.gov/quick-profiles/index.php?statename=newjersey')

soup=BeautifulSoup(page,'html.parser')


print(soup)



import nltk
from nltk.tokenize import word_tokenize




text=soup.get_text(strip=True)

print(text)




word_tokens=word_tokenize(text)

print(word_tokens)




cts=nltk.FreqDist(word_tokens)

cts.plot(20)




