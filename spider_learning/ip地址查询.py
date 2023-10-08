import requests
url = "https://www.ip138.com/ip.asp?ip="
try:
    r = requests.get(url+'127.0.0.1')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
