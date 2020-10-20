from selenium.webdriver import Chrome
import webdrivers

driver_path = webdrivers.get_chrome_driver(target='.')
driver = Chrome(executable_path=driver_path)
driver.quit()

