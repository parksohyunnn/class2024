import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

head = {'User-Agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
res = req.get("https://music.apple.com/kr/playlist/%EC%98%A4%EB%8A%98%EC%9D%98-top-100-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/pl.d3d10c32fbc540b38e266367dc8cb00c", headers=head)
# print(res.text)
# print(res.status_code)

soup = bs(res.text, "lxml")
# print(soup)


#데이터 선택
ranking = soup.select("tbody .rank")
title = soup.select(".songs-list-row__song-name-wrapper .svelte-154tqzm > .songs-list-row__song-name .svelte-154tqzm")
artist = soup.select(".songs-list-row__by-line svelte-154tqzm songs-list-row__by-line__mobile > span > a:nth-child(1)")

# print(len(ranking))
print(len(title)) 
# print(len(artist))

# 데이터 저장(파이썬 언어)
# rankingList=[r.text.strip()for r in ranking]
# titleList=[t.text.strip()for t in title]
# artistList=[a.text.strip()for a in artist]

# # 데이터 프레임
# chart_df = pd.DataFrame({
#     'Ranking' : rankingList,
#     'Title' : titleList,
#     'Artist' :artistList
# })

# # JSON 파일로 저장
# chart_df.to_json("melonChart100.json", force_ascii=False, orient="records")
