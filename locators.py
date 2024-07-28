from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print((driver.current_url))


#Id, Xpath, CSSSelectors, Classname,name,linktest
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

#Xpth= //tagname[@attribute='value']->// input[@type='submit']
#css = tagname[@attribute='value'] -> //input[type='submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("darshan")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message





# Wait for 2 seconds


time.sleep(200)

# Optionally, you can close the browser after the sleep
driver.quit()