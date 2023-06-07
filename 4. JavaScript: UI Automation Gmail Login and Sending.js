/*
This is a Gmail UI Automation JavaScript to Run and Debug. 
The script utilizes the Selenium WebDriver and Visual Studio Code integration to automate the Gmail login and email sending process.
The Results shows 'Message sent successfully' PASS.

This JavaScript was written in June 2023.
If the script is not working, you can try increasing the time sleep to give more time for the elements to load.
However, if there are any changes in the elements' IDs, XPATHs, or classes due to Chrome updates or other reasons, you may need to modify those parts accordingly.
*/

const { Builder, By, Key, until } = require('selenium-webdriver');

async function test_send_gmail() {
    let driver = await new Builder().forBrowser('chrome').build();
    try {
        let url = 'http://google.com';
        await driver.get(url);

        // Chrome Login
        let gmail_link = await driver.findElement(By.xpath('//*[@id="gb"]/div/div[2]/a/span'));
        await gmail_link.click();

        let gmail_input = await driver.findElement(By.css('input[type="email"]'));
        await gmail_input.sendKeys('testautomation13579');

        let next_button = await driver.findElement(By.id('identifierNext'));
        await next_button.click();

        
        await driver.sleep(5000);

        let password_input = await driver.findElement(By.css('input[type="password"]'));
        await password_input.sendKeys('Test97531');

        next_button = await driver.findElement(By.id('passwordNext'));
        await next_button.click();

        
        let gmail_button = await driver.wait(until.elementLocated(By.linkText('Gmail')), 10000);
        await gmail_button.click();

        await driver.sleep(3000);

        // Send email 
        let compose_button = await driver.findElement(By.xpath('//div[@role="button" and text()="Compose"]'));
        await compose_button.click();

        await driver.sleep(2000);

 
        let to_input = await driver.findElement(By.css('input[peoplekit-id="BbVjBd"]'));
        await to_input.sendKeys('testautomation13579@gmail.com');

       
        let subject_box = await driver.findElement(By.name('subjectbox'));
        await subject_box.sendKeys('Web UI Test Automation With Selenium and Visual Studio Code');

        await driver.sleep(1000);

      
        let message_box = await driver.findElement(By.css('div[role="textbox"]'));
        await message_box.sendKeys('Successful ~!! ');

        await driver.sleep(3000);

        // Find and Click 'Send' button
        let send_button = await driver.findElement(By.css('div[role="button"][aria-label^="Send"]'));
        await send_button.click();
        await driver.sleep(4000);

        // Wait for the "Message sent" element to be visible
        let message_sent_element = await driver.wait(until.elementLocated(By.className('bAq')), 10000);

        // Assertion
        if (message_sent_element !== null) {
            console.log('Message sent successfully');
        } else {
            console.log('Failed to send message');
        }
    } finally {
        await driver.quit();
    }
}

test_send_gmail().catch(console.error);



