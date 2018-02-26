import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import os
from selenium.webdriver.common.action_chains import ActionChains
import speedtest

driverLocation = "/Users/danielguzman/Documents/workspace/chromedriver"
os.environ["webdriver.chrome.driver"] = driverLocation
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % "45.73.191.169:40693")
options.add_experimental_option("detach", True)
options.add_argument('usr-data-dir=Macintosh HD/Users/danielguzman/Library/Application Support/Google/Chrome/Default')
# options.set_headless(True)

driver = webdriver.Chrome(driverLocation, chrome_options=options)
wait = WebDriverWait(driver, 1000)
driver.get("http://ipecho.net/plain")
s = speedtest.Speedtest()
s.get_best_server()

print(s.download())
print(s.upload())
