import logging
import sys
import platform
import tempfile
import zipfile
import tarfile
import pathlib
from urllib import request
from webdrivers import constant


DEFAULT_VERSION = 'v0.27.0'
DEFAULT_DOWNLOAD_URL = 'https://npm.taobao.org/mirrors/geckodriver'

logging.basicConfig(level=logging.INFO)


def get_firefox():
    if constant.firefox_driver.exists():
        return str(constant.firefox_driver)
    else:
        return str(get_firefox_driver())


def get_firefox_filename(version=DEFAULT_VERSION):
    """parse filename using platform"""
    system = sys.platform
    if system.startswith('win'):
        system = system[:3]
    file_map = {
        "linux32": f"geckodriver-{version}-linux32.tar.gz",
        "linux64": f"geckodriver-{version}-linux64.tar.gz",
        "darwin32": f"geckodriver-{version}-macos.tar.gz",
        "darwin64": f"geckodriver-{version}-macos.tar.gz",
        "win32": f"geckodriver-{version}-win32.zip",
        "win64": f"geckodriver-{version}-win64.zip",
    }
    bit = platform.architecture()[0][:2]
    file = file_map.get(system + bit, '')
    return file


def download_firefox_driver(version=None, mirror_url=None):
    """Download web webdrivers from URL"""
    version = version if version else DEFAULT_VERSION
    host = mirror_url if mirror_url else DEFAULT_DOWNLOAD_URL
    url = '/'.join([host, str(version), get_firefox_filename(version)])
    logging.info("Downloading webdriver. Please wait...")
    r = request.urlopen(url)
    logging.info("Downloading webdriver finished")
    return r


def save_firefox_driver(response, target=None):
    with tempfile.TemporaryFile() as f:
        f.write(response.read())
        if zipfile.is_zipfile(f):
            comp_file = zipfile.ZipFile(f)
        elif tarfile.is_tarfile(f):
            comp_file = tarfile.TarFile(f)
        else:
            raise ValueError("Not zip or tar format file")

        for file in comp_file.filelist:
            target = target if target else constant.DRIVER_PATH
            abs_target = pathlib.Path(target).resolve()
            driver = pathlib.Path(abs_target) / file.filename
            if not driver.exists():
                comp_file.extract(file, abs_target)
            return str(driver)


def get_firefox_driver(target=None, version=None, mirror_url=None):
    """
    Get firefox webdrivers from mirror_url, save to target.
    :param target: the path dir to save the webdrivers
    :param version: webdrivers version
    :param mirror_url: resource url to get the webdrivers
    :return:
    """
    driver_data = download_firefox_driver(version, mirror_url)
    return save_firefox_driver(driver_data, target)
