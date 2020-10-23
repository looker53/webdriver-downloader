from driverloader import chrome_driver
from selenium import webdriver

driver = chrome_driver(version='71')
browser = webdriver.Chrome(driver)
browser.quit()

