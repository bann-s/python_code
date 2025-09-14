import time
from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.bing.com")
print(driver.title)

time.sleep(5)  # Keeps the browser open for 5 seconds
driver.quit()