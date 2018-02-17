import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select




class FindThisShit():

    def test(self):
        url = "https://shop-usa.palaceskateboards.com/collections/jackets"
        driver = webdriver.Firefox()
        driver.get(url)





        # #container > article:nth-child(2) > div:nth-child(1) > p:nth-child(3) > a:nth-child(1)
        jacket = driver.find_element_by_xpath("/html/body/div/div/article/div/a")
        driver.implicitly_wait(10)

        jacket.click()

        wait = WebDriverWait(driver, 10)

        # size = wait.until(EC.element_to_be_clickable((By.ID , "s")))
        # sel = Select(size)


        # sel.select_by_visible_text("Large")

        add = wait.until(EC.element_to_be_clickable((By.XPATH , "/html/body/div/div/div[2]/div/form/fieldset[2]/input")))
        add.click()

        cart = wait.until(EC.element_to_be_clickable((By.XPATH , "/html/body/div/div/div[1]/div/a[2]")))
        cart.click()

        name = wait.until(EC.element_to_be_clickable((By.ID , "order_billing_name")))
        nameText = "Ned Flanders"
        i = 0
        while i<len(nameText):
            name.send_keys(nameText[i])
            i +=1

        email =  wait.until(EC.element_to_be_clickable((By.ID , "order_email")))
        emaiText = "NF@gmail.com"
        i = 0
        while i < len(emaiText):
            email.send_keys(emaiText[i])
            i += 1

        tel = wait.until(EC.element_to_be_clickable((By.ID , "order_tel")))
        telText = "555-555-5555"
        i = 0
        while i < len(telText):
            tel.send_keys(telText[i])
            i += 1



        add = wait.until(EC.element_to_be_clickable((By.NAME , "order[billing_address]")))
        addText = "99 fake st"
        i = 0
        while i < len(addText):
            add.send_keys(addText[i])
            i += 1







        city = wait.until(EC.element_to_be_clickable((By.ID , "order_billing_city")))
        city.send_keys("Albuquerque")

        zCode = wait.until(EC.element_to_be_clickable((By.ID, "order_billing_zip")))
        zCode.send_keys("87108")




        card = wait.until(EC.element_to_be_clickable((By.NAME , "credit_card[nlb]")))
        card.send_keys("1111111111111111")


        cvv = wait.until(EC.element_to_be_clickable((By.NAME , "credit_card[rvv]")))
        cvv.send_keys('111')


        button = wait.until(EC.element_to_be_clickable((By.XPATH , "/html/body/div[1]/div/form/div[2]/div[2]/fieldset/p[2]/label/div/ins")))
        button.click()



        pay = button = wait.until(EC.element_to_be_clickable((By.XPATH , "/html/body/div[1]/div/form/div[3]/div/input")))
        pay.click()













ff = FindThisShit()
ff.test()



