
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()

# Wait for up to 10 seconds for elements to appear
driver.implicitly_wait(10)  

url = 'http://google.com'
driver.get(url)


elm = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[2]/a/span')
elm.click()

time.sleep(1)

email_input = driver.find_element(By.CLASS_NAME, "whsOnd.zHQkBf")
email_input.send_keys('testautomation13579')
elm = driver.find_element(By.ID, "identifierNext").click()

time.sleep(1)

password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_input.send_keys('Test97531')
elm = driver.find_element(By.ID, "passwordNext").click()


# wait for 5 seconds
time.sleep(5)

# close the browser window
driver.quit()  


