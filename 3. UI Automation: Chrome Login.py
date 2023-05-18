from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'http://google.com'
driver.get(url)


# Chrome Login

elm = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[2]/a/span')
elm.click()

email_input = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
email_input.send_keys('testautomation13579')

next_button = driver.find_element(By.ID, 'identifierNext')
next_button.click()

# Wait for 5 seconds 
time.sleep(5)

password_input = None
password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
password_input.send_keys('Test97531')

next_button = driver.find_element(By.ID, "passwordNext")
next_button.click()

# Wait for 3 seconds 
time.sleep(3)

driver.quit()
