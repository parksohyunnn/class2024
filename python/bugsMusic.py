import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

res = req.get("https://music.bugs.co.kr/chart")
# print(res.text)
# print(res.status_code)
soup = bs(res.text, "lxml")
# print(soup)

# 데이터 선택
ranking = soup.select(".ranking > strong")
title = soup.select(".title > a ")
artist = soup.select(".artist > a:nth-child(1)")

# print(len(ranking))
# print(len(title))
# print(len(artist))

# 데이터 저장(자바스크립트 언어)
# rankingList = []
# titleList = []
# artistList = []

# for i in range(len(ranking)) :
#     rankingList.append(ranking[i].text)
#     titleList.append(title[i].text)
#     artistList.append(artist[i].text)

# # print(titleList)

# data = {"rank" : rankingList, "title" : titleList, "artist" :artistList}
# print(pd.DataFrame(data))

# 데이터 저장(파이썬 언어)
rankingList=[r.text.strip()for r in ranking]
titleList=[t.text.strip()for t in title]
artistList=[a.text.strip()for a in artist]

# 데이터 프레임
chart_df = pd.DataFrame({
    'Ranking' : rankingList,
    'Title' : titleList,
    'Artist' :artistList
})

# JSON 파일로 저장
chart_df.to_json("busChart100.json", force_ascii=False, orient="records")
