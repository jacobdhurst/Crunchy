import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class Crunchy():

    def cop(self):
        # User Data
        user = (
            "Ned Flanders",           # Name
            "Ned@BussDown.edu",       # Email
            "1234567890",             # Phone
            "742 Evergreen Terrace",  # Billing
            "742 Evergreen Terrace",  # Shipping
            "12345",                  # Zip
            "Buss Down",              # City
            "35",                     # State Index
            "1234567887654321",       # CC
            "123",                    # CCV
            "0",                      # CC Month Index
            "0"                       # CC Year Index
        )

        # Initializing webdriver
        driverLocation = "C:/Users/Jacob/Documents/chromedriver.exe"#"/Users/danielguzman/Documents/workspace/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.set_headless(False)
        driver = webdriver.Chrome(driverLocation, chrome_options= options)
        wait = WebDriverWait(driver, 100)

        # Start timer
        start = time.time()

        # Find and cart item(s)
        driver.get("http://www.supremenewyork.com/shop/all/accessories")
        productID = '//*[@id="container"]/article[8]/div/a/img'
        product = wait.until(EC.element_to_be_clickable((By.XPATH, productID)))
        product.click()
        size = wait.until(EC.element_to_be_clickable((By.ID, "s")))
        select = Select(size)
        select.select_by_visible_text("Medium")
        add = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"add-remove-buttons\"]/input")))
        add.click()
        cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"cart\"]/a[2]")))
        cart.click()

        # Inject billing via JavaScript
        driver.execute_script("document.getElementById(\"order_billing_name\").value=\""+user[0]+"\"")
        driver.execute_script("document.getElementById(\"order_email\").value=\""+user[1]+"\"")
        driver.execute_script("document.getElementById(\"order_tel\").value=\""+user[2]+"\"")
        driver.execute_script("document.getElementById(\"bo\").value=\""+user[3]+"\"")
        driver.execute_script("document.getElementById(\"bo\").value=\""+user[4]+"\"")
        driver.execute_script("document.getElementById(\"order_billing_zip\").value=\""+user[5]+"\"")
        driver.execute_script("document.getElementById(\"order_billing_city\").value=\""+user[6]+"\"")
        driver.execute_script("document.getElementById('order_billing_state').getElementsByTagName('option')["+user[7]+"].selected = 'selected'")
        driver.execute_script("document.getElementById(\"nnaerb\").value=\""+user[8]+"\"")
        driver.execute_script("document.getElementById(\"orcer\").value=\""+user[9]+"\"")
        driver.execute_script("document.getElementById('credit_card_month').getElementsByTagName('option')["+user[10]+"].selected = 'selected'")
        driver.execute_script("document.getElementById('credit_card_year').getElementsByTagName('option')["+user[11]+"].selected = 'selected'")

        print("Elapsed: " + str(time.time() - start) + "s")


bot = Crunchy()
bot.cop()

