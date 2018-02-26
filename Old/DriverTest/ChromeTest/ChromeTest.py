from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

class ChromeTest():

    def test(self):

        driverLocation = "/Users/danielguzman/Documents/workspace/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        options = webdriver.ChromeOptions()
        options.add_argument('')

        driver = webdriver.Chrome(driverLocation, chrome_options=options)

        driver.get("http://google.com")

        log = driver.find_element_by_xpath('//*[@id="gb_70"]')
        log.click()
        emailField = driver.find_element_by_xpath('//*[@id="identifierId"]')
        emailField.send_keys('danielguzman45@gmail.com')
        next = driver.find_element_by_xpath('//*[@id="identifierNext"]')
        next.click()
        pw = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')

c = ChromeTest()
c.test()