'''
This script was written in May 2023.
If the script is not working, you can try increasing the time sleep to give more time for the elements to load.
However, if there are any changes in the elements' IDs, XPATHs, or classes due to Chrome updates or other reasons, you may need to modify those parts accordingly.
'''

# This script was written in May 2023 (Updated in June. 04).
# If the script is not working, you can try increasing the time sleep to give more time for the elements to load.
# However, if there are any changes in the elements' IDs, XPATHs, or classes due to Chrome updates or other reasons, you may need to modify those parts accordingly.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

url = 'http://google.com'
driver.get(url)


# Chrome Login

elm = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[2]/a/span')
elm.click()

gmail_input = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
gmail_input.send_keys('testautomation13579')

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

# Find and click the 'Gmail' button
gmail_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Gmail')))
gmail_button.click()

time.sleep(3)

# Send email 
compose_button = driver.find_element(By.XPATH, '//div[@role="button" and text()="Compose"]')
compose_button.click()

time.sleep(2)

# Find and Type 'To' input box
To_input = driver.find_element(By.CSS_SELECTOR, 'input[peoplekit-id="BbVjBd"]')
To_input.send_keys('testautomation13579@gmail.com')


# Find and Type 'Subject' input box
subject_box = driver.find_element(By.NAME, 'subjectbox')
subject_box.send_keys('Web UI Test Automation With Selenium and Visual Studio Code')

time.sleep(1)

# Find and Type 'Message Box' 
message_box = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
message_box.send_keys('Successful ~!! ')

time.sleep(3)

# Find and Click 'Send' button
send_button = driver.find_element(By.XPATH, '//div[@aria-label="Send ‪(Ctrl-Enter)‬"]')
send_button.click()


time.sleep(4)
driver.quit()

