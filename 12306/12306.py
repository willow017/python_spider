import requests

url = "https://kyfw.12306.cn/otn/resources/login.html"

res = requests.get(url=url)

print(url)