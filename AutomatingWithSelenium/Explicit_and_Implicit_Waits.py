"""
[TBD] Explicit and Implicit Waits
Question: Explain the difference between implicit and explicit waits with examples.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait_examples(driver):
    # Implicit Wait - applies to all elements
    driver.implicitly_wait(10)
    
    # Explicit Wait - for specific conditions
    wait = WebDriverWait(driver, 10)
    
    # Wait for element to be clickable
    element = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
    
    # Wait for element to be present
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
    
    # Wait for element to be visible
    element = wait.until(EC.visibility_of_element_located((By.ID, "loading")))
