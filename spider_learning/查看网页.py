import urllib.request
from urllib.robotparser import RobotFileParser

response = urllib.request.urlopen("https://a.com")
print(response.read().decode('utf-8'))

print(type(response))

rp = RobotFileParser()
rp.set_url("https://a.com/robots.txt")
rp.read()
print(rp.can_fetch('*','https://a.com'))
