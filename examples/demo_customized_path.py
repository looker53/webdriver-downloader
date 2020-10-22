from selenium.webdriver import Chrome
import driverloader

driver_path = driverloader.get_chrome_driver(target='.')
driver = Chrome(executable_path=driver_path)
driver.quit()

