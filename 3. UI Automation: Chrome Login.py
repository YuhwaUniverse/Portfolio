'''
This script was written in May 2023.
If the script is not working, you can try increasing the time sleep to give more time for the elements to load.
However, if there are any changes in the elements' IDs, XPATHs, or classes due to Chrome updates or other reasons, you may need to modify those parts accordingly.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'http://google.com'
driver.get(url)


# Chrome Login with valid email address and password 

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


