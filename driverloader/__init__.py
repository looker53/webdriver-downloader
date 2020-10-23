from .chrome_driver import ChromeDriver
from .firefox_driver import FirefoxDriver


# class Drivers:
#     chrome = ChromeDriver()
#     firefox = FirefoxDriver()
#
#
# drivers = Drivers()

chrome_driver = ChromeDriver().get()
firefox_driver = FirefoxDriver().get()

