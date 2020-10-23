import platform
import sys
from driverloader.base_driver import BaseDriver

DEFAULT_FIREFOX_VERSION = '0.27.0'


class FirefoxDriver(BaseDriver):
    def __init__(self, version=DEFAULT_FIREFOX_VERSION, host=None):
        super().__init__('firefox', version=version, host=host)

    @property
    def _get_file(self):
        """parse filename using platform"""
        system = sys.platform
        if system.startswith('win'):
            system = system[:3]
        file_map = {
            "linux32": f"geckodriver-v{self.full_version}-linux32.tar.gz",
            "linux64": f"geckodriver-v{self.full_version}-linux64.tar.gz",
            "darwin32": f"geckodriver-v{self.full_version}-macos.tar.gz",
            "darwin64": f"geckodriver-v{self.full_version}-macos.tar.gz",
            "win32": f"geckodriver-v{self.full_version}-win32.zip",
            "win64": f"geckodriver-v{self.full_version}-win64.zip",
        }
        bit = platform.architecture()[0][:2]
        file = file_map.get(system + bit, '')
        return file
