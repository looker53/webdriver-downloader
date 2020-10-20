from selenium.webdriver import Chrome
import driver

driver_path = driver.get_chrome_driver(target='.')
driver = Chrome(executable_path=driver_path)
driver.quit()

