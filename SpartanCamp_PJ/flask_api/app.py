import requests


# APIURLを指定し、Json形式で値を取得する
res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=1560055")

# print(res.text["status"])
# print(type(res.text))  # str型

# Json形式に変換
json = res.json()
print(json["results"][0]["address1"])
print(json["results"][0]["address2"])
# print(type(res.json()))  # dict型
