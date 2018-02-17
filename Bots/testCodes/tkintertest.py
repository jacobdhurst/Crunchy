from tkinter import *
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

def Drive():
    driver = webdriver.Firefox()
    driver.get('https://shop-usa.palaceskateboards.com/collections/tops')

root = Tk()
# Label(root,text='URL').grid(row=0)
# e1= Entry(root)
# e1.grid(row=0,column=1)
# url = str(e1.get())
but1 = Button(root,text="Launch",command=Drive).grid(row=1)


root.mainloop()






