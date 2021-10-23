from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer
driver = webdriver.Chrome()
driver.get('https://www.google.com')
print('Título: ', driver.title)
print('URL:', driver.current_url)