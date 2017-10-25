import xlrd
import selenium
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://192.168.4.19:8886/Nichehire/")
workbook=xlrd.open_workbook('/home/keertmak/login.xlsx')
worksheet=workbook.sheet_by_name('Sheet1') #Read for XCL Sheet names#add login
for current_row in range(worksheet.nrows):
	fname = worksheet.row(current_row)[0]
	lname = worksheet.row(current_row)[1]
	dri=driver.find_element_by_id("email_id").send_keys(fname)
	drii=driver.find_element_by_id("pwd").send_keys(lname)
	drr=driver.find_element_by_id("signinBtn").click()

