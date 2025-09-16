"""
2. Element Locators
Question: What are the different ways to locate elements in Selenium? Provide examples.
"""

from selenium.webdriver.common.by import By

def find_elements_examples(driver):
    # By ID
    element = driver.find_element(By.ID, "username")
    
    # By Class Name
    element = driver.find_element(By.CLASS_NAME, "form-control")
    
    # By XPath
    element = driver.find_element(By.XPATH, "//input[@name='password']")
    
    # By CSS Selector
    element = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    
    # By Name
    element = driver.find_element(By.NAME, "email")
    
    # By Tag Name
    elements = driver.find_elements(By.TAG_NAME, "a")
