import unittest
import time
from selenium import webdriver
import xlrd
from xlrd import open_workbook, cellname
class Loogin(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
	def test_Login(self):
		driver=self.driver
		driver.get("http://192.168.4.19:8886/Nichehire/")
		driver.set_window_size(1920, 1080)
		wb=xlrd.open_workbook('/home/keertmak/login.xlsx')
		sheetname = wb.sheet_names() #Read for XCL Sheet names
		sh1 = wb.sheet_by_index(0) #add login
		i=0
		while (i<2):
			rownum=(i)
			rows = sh1.row_values(rownum)
			driver.find_element_by_name("email_id").send_keys(rows[0])
			time.sleep(8)
			i=i+1
	def tearDown(self):
		self.driver.close()
if __name__ == "__main__":
	unittest.main()


