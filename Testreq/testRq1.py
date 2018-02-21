import requests
import re

s = requests.Session()
s.proxies = {'http': 'http://212.237.23.60:2000'}

r = s.get('https://www.iplocation.net/find-ip-address')

data = r.text

regex = r"1.2.3.45"  # Proxy IP
regex2 = r"6.7.8.99"  # My IP

matches = re.findall(regex, data)
matches2 = re.findall(regex2, data)

print(matches)
print(matches2)