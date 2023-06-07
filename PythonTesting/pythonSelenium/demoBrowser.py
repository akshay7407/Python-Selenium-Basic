from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("PythonTesting/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# To run the test cases in firefox or any other driver jus changes service of driver 
driver.maximize_window()
driver.get("https://overapi.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://overapi.com/jquery")
driver.back()
driver.refresh()
driver.forward()
print(driver.current_url)
driver.close()