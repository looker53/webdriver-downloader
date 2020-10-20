from pathlib import Path

DRIVER_DIR = 'executer'
DRIVER_PATH = Path(__file__).parent.resolve() / DRIVER_DIR
if not DRIVER_PATH.exists():
    DRIVER_PATH.mkdir()

chrome_driver = DRIVER_PATH / 'chromedriver.exe'
firefox_driver = DRIVER_PATH / 'geckodriver'
