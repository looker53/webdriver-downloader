from selenium.webdriver import Chrome
import webdrivers

driver = Chrome(webdrivers.chrome_driver)
driver.quit()
