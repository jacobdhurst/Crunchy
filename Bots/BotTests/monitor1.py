import time
from selenium import webdriver
from bs4 import BeautifulSoup



driver = webdriver.Firefox()

driver.get("http://yeezysupply.com")

soup = BeautifulSoup(driver.page_source)


for link in soup.find_all('a'):
    print (link.get('href',None),link.get_text())

    print(link.get_text)
    print("----------------------------------------")

