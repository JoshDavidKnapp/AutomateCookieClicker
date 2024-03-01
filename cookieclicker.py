from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



product_price_prefix = "productPrice"
product_prefix = "product"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service)

driver.get("https://orteil.dashnet.org/cookieclicker/")



#Language Selection
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="langSelect-EN"]')))
language = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language.click()

#Find Cookie to Click
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="bigCookie"]' )))
cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="bigCookie"]' )))
cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

cookies_id = "cookies"


while True:
    #Click Cookie
    cookie.click()

    #Count Points
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",",""))
    

    for i in range(4):
        #Find Upgrade Product
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, product_price_prefix + str(i) )))
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",","")

        #Skip Products that can't convert to int
        if not product_price.isdigit():
            continue

        product_price = int(product_price)
        

        #Buy Upgrades when possible
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break
