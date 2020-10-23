## Quick start:

Download chrome driver:
```python
from driverloader import chrome_driver
print(chrome_driver)
```

Download firefox driver:
```python
from driverloader import firefox_driver
print(firefox_driver)
```

The drivers would be downloaded in **executor/** dir of the webdrivers package.
You can find chromedriver.exe or geckodriver.exe in the dir.


Using with selenium:
```python
from selenium.webdriver import Chrome
from driverloader import chrome_driver

browser = Chrome(chrome_driver)
browser.quit()
```

Downloading to customized path:
```python
from driverloader import ChromeDriver
driver_path = ChromeDriver().get('.')
```

or absolute path:
```python
import pathlib
from driverloader import ChromeDriver

current_dir = pathlib.Path(__file__).parent.parent
print(ChromeDriver().get(current_dir))
```

customized version:
```python
from driverloader import ChromeDriver
driver_path = ChromeDriver(version=70).get('.')
```


## command line
Using driverloader by command line like this:
```bash
driverloader chrome .
driverloader firefox .
```
Two arguments:
- driver_name, chrome and firefox supported.
- path,  the path you want to save the driver.

Options:
- `-v` or `--version`,  the version would be downloaded.
- `-f` or `--force`, force downloading if the similar driver exists


## Mirror URL
webdriver-downloader get the drivers from https://npm.taobao.org/mirrors/
- chrome driver: https://npm.taobao.org/mirrors/chromedriver/
- firefox driver: https://npm.taobao.org/mirrors/geckodriver/