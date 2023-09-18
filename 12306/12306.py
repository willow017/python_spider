import requests

url = "https://kyfw.12306.cn/otn/index/initMy12306Api"

headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Cookie": "JSESSIONID=B8B0E0048E00E9CBDA090653F98B6EF6; tk=w3lPonV2q4_PTo-BeJdPVc4q1lk12B5fSHqnNQ45d1d0; BIGipServerotn=3973513482.50210.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGpServerpassport=803733770.50215.0000; route=c5c62a339e7744272a54643b3be5bf64; fo=9fr78n063nd7erwzX2ONeo8rBqdaNzKxTgNWye4RbGCPI4r4b6KM3QoG0gPklwRVo8a0rbRrM6kyBmCtlLGZfMz-xzOAzIaCMW0u4K7Bo_6khsIrHrrzkNHKME9583m502abAqu15HIl2GZL-4xGiDokbYHvOM7qKhbAZ3VjLUsdXY1d2R_Le95DZBP2BZLhKx9jBzdWipS9JtSY; uKey=45e37c27b3bbeb1ddb48b39a0a4528fb72b99aa0d42bd92b168f45ab6d3f3c97",
        "Host": "kyfw.12306.cn",
        "Origin": "https://kyfw.12306.cn",
        "Referer": "https://kyfw.12306.cn/otn/view/index.html",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"macOS\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

res = requests.post(url=url, headers=headers)

print(res.text)