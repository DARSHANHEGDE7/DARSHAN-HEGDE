from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service

#chrome driver service selenium 160->160  chrome driver
#service_object=Service("D:\chromedriver-win64.exe")
#driver=webdriver.Chrome(service=service_object)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.get("http://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print((driver.current_url))





# Wait for 2 seconds
time.sleep(2)

# Optionally, you can close the browser after the sleep
driver.quit()
