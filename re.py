import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Firefox()
search=driver.get("http://uat.reachsafe.co.in/SheShuttle/logout.html")
search1=driver.find_element_by_id("userInput").send_keys("nikhil.tumiki@votarytech.com")
search2=driver.find_element_by_id("passwordInput").send_keys("nikhil")
serach3=driver.find_element_by_id("login-button").click()

vehicle=driver.find_element_by_link_text("Registration").click()
vehicle1=driver.find_element_by_link_text("Vehicle").click()


