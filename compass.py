
import webbrowser
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.select import Select

url= "https://upassbc.translink.ca/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://upassbc.translink.ca/')


s1= Select(driver.find_element_by_id('PsiId'))
s1.select_by_value('sfu')

#GO bottom
driver.find_element_by_id('goButton').click()

#print("SFU")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")


username.send_keys("nbagheri")
password.send_keys("xxxxxxx")

driver.find_element_by_name("submit").click()


