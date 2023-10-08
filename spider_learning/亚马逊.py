import requests
url = "https://www.amazon.cn/dp/B07FQKB4TM/459-5174030-3098254?_encoding=UTF8&ref_=sa_menu_kindle_l3_ki"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
