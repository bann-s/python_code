"""A simple test to open a web page and check its title.
webdriver: Allows you to control the browser.
Keys: Lets you simulate keyboard key presses.

"""


from selenium import webdriver

#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service


#create a new Chrome session
#driver = webdriver.Chrome('./chromedriver')
#service = Service('C:/Users/scari/Downloads/My_py_codes/projects/AutomatingWithSelenium/msedgedriver.exe')
#service = Service('./msedgedriver.exe')
driver = webdriver.Edge()

driver.get("https://www.python.org")
print(driver.title)




"""
The error ModuleNotFoundError: No module named 'selenium' means the Selenium package is not installed in your Python environment.

To fix this, open your terminal and run: 'pip install selenium'

After installation, try running your script again.
If you have multiple Python versions, you may need to use pip3: 'pip3 install selenium'

This will install the Selenium package and resolve the error.

driver = webdriver.Edge('./msedgedriver') -> for this to work you need to have the msedgedriver executable in the same path as your script or provide the full path to the executable or.
driver = webdriver.Edge() -> this will work if the msedgedriver is in your system PATH. 
"""