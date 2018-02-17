import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select




class FindThisShit():

    def item1(self):
        url = "https://shop-usa.palaceskateboards.com/collections/tops"
        driver = webdriver.Firefox()
        driver.get(url)
        wait = WebDriverWait(driver, 1000)
        itemName = "'WAFFLE ON POLO YELLOW'"
        item = driver.find_element_by_xpath("//div[@class='product-info']//a[@href='/products/waffle-on-polo-yellow']")

        item.click()




        size = wait.until(EC.element_to_be_clickable((By.ID  , "product-select")))
        sel = Select(size)
        sel.select_by_visible_text("Large")

        add = wait.until(EC.element_to_be_clickable((By.XPATH  , "/html/body/div[2]/div[2]/div/div[5]/form/input")))
        add.click()

        add2 = wait.until(EC.element_to_be_clickable((By.XPATH  , "/html/body/section/div[1]/a")))
        add2.click()

        checkOut = wait.until(EC.element_to_be_clickable((By.ID  , "checkout")))
        checkOut.click()
        #
        email = wait.until(EC.element_to_be_clickable((By.ID, "checkout_email")))
        emaiText = "NF@gmail.com"
        email.send_keys(emaiText)

        first = wait.until(EC.element_to_be_clickable((By.ID , "checkout_shipping_address_first_name")))
        first.send_keys("ned")

        last = wait.until(EC.element_to_be_clickable((By.ID, "checkout_shipping_address_last_name")))
        last.send_keys("flanders")

        home = wait.until(EC.element_to_be_clickable((By.ID, "checkout_shipping_address_address1")))
        home.send_keys("111 fake st")
        home2 = wait.until(EC.element_to_be_clickable((By.ID, "checkout_shipping_address_address2")))
        home2.send_keys("B")

        city = wait.until(EC.element_to_be_clickable((By.ID, "checkout_shipping_address_city")))
        city.send_keys("flavortown")

        zipCode = wait.until(EC.element_to_be_clickable((By.ID, "checkout_shipping_address_zip")))
        zipCode.send_keys("11111")

        tel = wait.until(EC.element_to_be_clickable((By.ID, "checkout_shipping_address_phone")))
        tel.send_keys("6966969696")

        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id="'recaptcha-anchor'"]")))


        cont = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div[1]/div/div/span/div[5]")))
        cont.click()







ff = FindThisShit()
ff.item1()



