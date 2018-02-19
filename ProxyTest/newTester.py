from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

class ChromeTest():

    def test(self):
        input_file = open("filtered.txt", "r")

        for proxy in input_file:
            driverLocation = "C:/Users/Jacob/Documents/chromedriver.exe" #/Users/danielguzman/Documents/workspace/chromedriver"
            os.environ["webdriver.chrome.driver"] = driverLocation
            options = webdriver.ChromeOptions()
            options.add_argument('--proxy-server=%s' % proxy)
            options.add_experimental_option("detach", True)

            driver = webdriver.Chrome(driverLocation, chrome_options=options)

            driver.get("http://www.ip-adress.eu/")

c = ChromeTest()
c.test()