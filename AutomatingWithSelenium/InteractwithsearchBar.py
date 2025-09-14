from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge()
driver.get("https://www.bing.com/")
search_bar = driver.find_element("name", "q") # Locate the search bar using its name attribute
search_bar.clear()  # Clear any pre-filled text in the search bar
search_bar.send_keys("getting started with python Selenium")    # Type the search query into the search bar
search_bar.send_keys(Keys.RETURN)
print(driver.title)  # Print the title of the current page
