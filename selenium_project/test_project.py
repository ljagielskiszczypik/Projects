import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
driver.get('http://seleniumdemo.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.quit()