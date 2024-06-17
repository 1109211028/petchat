import requests
from bs4 import BeautifulSoup
print('特技玩家=7147')
print('劇場版 排球少年!! 垃圾場的決戰=7142')
print('機動戰士鋼彈SEED FREEDOM=7152')
print('非紳士特攻隊=7138')
print('哥吉拉與金剛：新帝國=7078')
print('功夫熊貓4=7133')
print('我在這裡等你=7208')
print('莎莉=7136')
# movienum = input("請輸入電影代號：")

url = f"https://www.vscinemas.com.tw/vsweb/film/detail.aspx?id={movienum}"



response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all('section', class_="movieDetail")

for movie in movies:
    name = movie.find('div',class_="titleArea")
    name = name.text
    info = movie.find('div',class_="infoArea")
    info =info.text
    version = movie.find('div',class_="movieVersion")
    version = version.text
    print(name,info,version)
