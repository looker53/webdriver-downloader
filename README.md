## Quick start:

Download chrome driver:
```python
import webdrivers
print(webdrivers.chrome)
```

Download firefox driver:
```python
import webdrivers
print(webdrivers.firefox)
```

The drivers would be downloaded in **executor/** dir of the webdrivers package.
You can find chromedriver.exe or geckodriver.exe in the dir.


Using with selenium:
```python
from selenium.webdriver import Chrome
import webdrivers

driver = Chrome(webdrivers.chrome)
driver.quit()
```

Downloading to customized path:
```python
import webdrivers
driver_path = webdrivers.get_chrome_driver(target='.')
```

or absolute path:
```python
import pathlib
import webdrivers

current_dir = pathlib.Path(__file__).parent.parent
print(webdrivers.get_chrome_driver(current_dir))
```