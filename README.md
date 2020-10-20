## Usage:

Quick start:

```python
import webdrivers
print(webdrivers.chrome_driver)
```

Using with selenium
```python
from selenium.webdriver import Chrome
import webdrivers

driver = Chrome(webdrivers.chrome_driver)
driver.quit()
```

Dowloading to customized path:
```python
from selenium.webdriver import Chrome
import webdrivers

driver_path = webdrivers.get_chrome_driver(target='.')
driver = Chrome(executable_path=driver_path)
driver.quit()
```