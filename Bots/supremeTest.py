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


class ChromeTest():
    def test(self):
        driverLocation = "/Users/danielguzman/Documents/workspace/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        # options.add_argument("user-data-dir=/Users/danielguzman/Library/Application Support/Google/Chrome")
        options.set_headless(True)

        driver = webdriver.Chrome(driverLocation, chrome_options= options)
        wait = WebDriverWait(driver, 1000)


        driver.get("http://www.supremenewyork.com/shop/all/accessories")

        product = '//*[@id="container"]/article[8]/div/a/img'
        print('Looking for product')


        cproduct = wait.until(EC.element_to_be_clickable((By.XPATH, product)))
        cproduct.click()
        start = time.time()
        print('Product found')

        size = wait.until(EC.element_to_be_clickable((By.ID, "s")))
        sel = Select(size)
        sel.select_by_visible_text("Medium")
        print('Size found')

        add = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"add-remove-buttons\"]/input")))
        add.click()
        print('Adding to cart....')

        add2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"cart\"]/a[2]")))
        add2.click()
        print('Added to cart....')

        pfName = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"order_billing_name\"]")))
        print('Billing Info')
        # pfName.click()
        driver.execute_script("document.getElementById(\"order_billing_name\").value=\"ned flanders\"")
        driver.execute_script("document.getElementById(\"order_email\").value=\"ned@ned.com\"")
        driver.execute_script("document.getElementById(\"order_tel\").value=\"55555555555\"")
        driver.execute_script("document.getElementById(\"bo\").value=\"321 MAin St\"")
        driver.execute_script("document.getElementById(\"bo\").value=\"321 MAin St\"")
        driver.execute_script("document.getElementById(\"order_billing_zip\").value=\"87110\"")
        driver.execute_script("document.getElementById(\"order_billing_city\").value=\"Albuquerque\"")
        driver.execute_script("document.getElementById('order_billing_state').getElementsByTagName('option')[35].selected = 'selected'")
        driver.execute_script("document.getElementById(\"nnaerb\").value=\"4122329904837289\"")
        driver.execute_script("document.getElementById(\"orcer\").value=\"324\"")
        driver.execute_script("document.getElementById('credit_card_month').getElementsByTagName('option')[6].selected = 'selected'")
        driver.execute_script("document.getElementById('credit_card_year').getElementsByTagName('option')[4].selected = 'selected'")

        end = time.time()
        print('Done')
        print("Checkout time" +str(time.time()-start) + " seconds")



c = ChromeTest()
c.test()

