
import sys
from driverloader.driver import BaseDriver

DEFAULT_CHROME_VERSION = '71.0.3578.80'


class ChromeDriver(BaseDriver):
    def __init__(self, host=None):
        super().__init__('chrome', host)

    def __call__(self, path=None, version=DEFAULT_CHROME_VERSION, force=False):
        return super().__call__(path=path, version=version, force=force)

    @property
    def default(self):
        return self.__call__(path=None, version=DEFAULT_CHROME_VERSION, force=False)

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