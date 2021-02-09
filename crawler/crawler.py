import requests
import re
res = requests.get("http://naver.com")
print(res.status_code)

p = re.compile("ca.e")

m = p.match("case")
print(m.group())