from selenium.webdriver import Chrome
from driverloader import drivers

driver = Chrome(drivers.chrome_driver)
driver.quit()
