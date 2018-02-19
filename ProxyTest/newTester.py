from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

class ChromeTest():

    def test(self):
        input_file = open("filtered.txt", "r")
        i = 0
        for proxy in input_file:
            driverLocation = "C:/Users/Jacob/Documents/chromedriver.exe" #/Users/danielguzman/Documents/workspace/chromedriver"
            os.environ["webdriver.chrome.driver"] = driverLocation

            options = webdriver.ChromeOptions()
            options.add_argument('--proxy-server=%s' % proxy)
            options.add_experimental_option("detach", True)
            options.set_headless(True)

            driver = webdriver.Chrome(driverLocation, chrome_options=options)
            driver.get("http://www.ip-adress.eu/")
            if not(driver.page_source.__contains__("ERR")): print(i, ":", driver.current_url, " Success:", proxy)

            i = i + 1

c = ChromeTest()
c.test()