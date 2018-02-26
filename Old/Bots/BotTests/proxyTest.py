import urllib
import time
candidate_proxies = ['67.227.107.158:15192','64.106.111.132']
for proxy in candidate_proxies:
    print ("Trying HTTP proxy %s" % proxy)
    try:
        result = urllib.urlopen("http://www.google.com", proxies={'http': proxy})
        print ("Got URL using proxy %s" % proxy)
        break
    except:
        print ("Trying next proxy in 5 seconds")
        time.sleep(5)