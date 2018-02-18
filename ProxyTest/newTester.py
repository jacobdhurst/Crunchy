from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

class ChromeTest():

    def test(self):
        proxy = "122.183.137.190:8080"

        driverLocation = "/Users/danielguzman/Documents/workspace/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server=%s' % proxy)
        options.add_experimental_option("detach", True)



        driver = webdriver.Chrome(driverLocation, chrome_options=options)


        driver.get("http://www.ip-adress.eu/")








c = ChromeTest()
c.test()