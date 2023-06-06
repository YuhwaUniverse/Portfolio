'''
Pytest UI Automation Script with Visual Studio Code and Selenium for Gmail Login and Send
Status of Html Report is '1 passed in 37.76s'
Link to view the Html Report in a webpage format : 

This pytest script was written in May and Upodated in June 2023.
If the script is not working, you can try increasing the time sleep to give more time for the elements to load.
However, if there are any changes in the elements' IDs, XPATHs, or classes due to Chrome updates or other reasons, you may need to modify those parts accordingly.

If the downloaded file is not available to run the test, try changing the file name to something simple and start the test again. ex) 'test'
'''


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# pytest: Gmail Login and Send

@pytest.fixture(scope='session')

def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_send_email(driver):
    url = 'http://google.com'
    driver.get(url)


    # Chrome Login
    gmail_link = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[2]/a/span')
    gmail_link.click()

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
    send_button = driver.find_element(By.CSS_SELECTOR, 'div[role="button"][aria-label^="Send"]')
    send_button.click()
    time.sleep(4)

    # Wait for the "Message sent" element to be visible
    message_sent_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'bAq')))

    # Assertion
    assert message_sent_element is not None
    
    
    

