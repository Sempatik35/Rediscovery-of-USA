#- Gerekli modülleri projeye dahil ediyoruz CMD açıp pip install beautifulsoup4 ardından 
#- pip install requests yazarak modülleri kurabilirsiniz


import requests
from bs4 import BeautifulSoup

url = "http://www.koeri.boun.edu.tr/scripts/lst0.asp"  #Son deprem bilgilerini buradan APİ mantığıyla çekiyoruz

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")
pre = soup.find("pre")
text = pre.text
liste = text.split("\n")
print("\n.".join(liste[4:8]))
