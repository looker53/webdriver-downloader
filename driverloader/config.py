from pathlib import Path

DRIVER_DIR = 'executor'
DRIVER_PATH = Path(__file__).parent.resolve() / DRIVER_DIR
if not DRIVER_PATH.exists():
    DRIVER_PATH.mkdir()

# CHROME_PATH = DRIVER_PATH / 'chrome'
# if not CHROME_PATH.exists():
#     CHROME_PATH.mkdir()
#
# FIREFOX_PATH = DRIVER_PATH / 'firefox'
# if not FIREFOX_PATH.exists():
#     FIREFOX_PATH.mkdir()