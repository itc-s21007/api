import requests as req

prefectures = input("1~47番までの都道府県が選べます")
aaaa = input("出生数・死亡数/転入数・転出数が０〜４番で選べます")


Keys = "GQmhBRHJFmTjP1Evf8OcLxmCh04Kb9cljuCoqrFd"
headers = {"X-API-KEY": Keys}
url = (
    f"https://opendata.resas-portal.go.jp/api/v1/population/sum/estimate?prefCode={prefectures}"
)


res = req.get(url, headers=headers)
data = res.json()
print(data["result"]["data"][int(aaaa)])
