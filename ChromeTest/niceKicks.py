import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import selenium.webdriver
import os


class ChromeTest():

    def test(self):

        driverLocation = "/Users/Jacob/Documents/chromedriver.exe" #"/Users/danielguzman/Documents/workspace/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)




        driver = webdriver.Chrome(driverLocation, chrome_options= options)
        wait = WebDriverWait(driver, 1000)


        driver.get("https://shopnicekicks.com/cart/7062420750385:1")

        checkEmail = email = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"checkout_email\"]")))
        checkEmail.send_keys("testme234@gmail.com")

        fn = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"checkout_shipping_address_first_name\"]")))
        fn.send_keys('ned')

        ln = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"checkout_shipping_address_last_name\"]")))
        ln.send_keys("flanders")

        add1=  wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"checkout_shipping_address_address1\"]")))
        add1.send_keys("321 Main st")

        city =  wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"checkout_shipping_address_city\"]")))
        city.send_keys("Albuquerque")

        zip = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"checkout_shipping_address_zip\"]")))
        zip.send_keys("87108")

        phone = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"checkout_shipping_address_phone\"]")))
        phone.send_keys('5555555555')

        cont = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div/form/div[2]/button")))
        cont.click()

        cont2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div/form/div[2]/button")))
        cont2.click()

        time.sleep(10)



        driver.switch_to.active_element.send_keys('1111')
        # driver.switch_to.frame(wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"card-fields-number-gowwdwi5n4a00000\"]"))))






        # ccNum = driver.find_element(By.XPATH, "//*[@id=\"number\"]")
        # ccNum.send_keys('1111111111111111')
        # ccName = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"name\"]")))
        # ccName.send_keys("Ned Flanderson")
        #
        # ccExp = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"number\"]")))
        # ccExp.send_keys('08/20')
        #
        # cvv = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"verification_value\"]")))
        # cvv.send_keys('234')
        #
        # finish = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div/div/form/div[3]/button/span")))
        # finish.click()