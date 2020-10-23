
import sys
from driverloader.base_driver import BaseDriver

DEFAULT_CHROME_VERSION = '71.0.3578.80'


class ChromeDriver(BaseDriver):
    def __init__(self, version=DEFAULT_CHROME_VERSION, host=None):
        super().__init__('chrome', version, host)

    @property
    def _get_file(self):
        """parse filename using platform"""
        platform = sys.platform
        platforms = {
            "win32": "win32",
            "win64": "win64",
            "linux": "linux64",
            "darwin": "mac64",
        }
        return 'chromedriver_{}.zip'.format(platforms.get(platform, ''))

if __name__ == '__main__':
    chrome = ChromeDriver()
    chrome.get_driver()