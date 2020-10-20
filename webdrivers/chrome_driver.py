import logging
import sys
import tempfile
import zipfile
import pathlib
from urllib import request
from . import constant

DEFAULT_VERSION = '71.0.3578.80'
DEFAULT_DOWNLOAD_URL = 'https://npm.taobao.org/mirrors/chromedriver'

logging.basicConfig(level=logging.INFO)


def get_chrome():
    if constant.chrome_driver.exists():
        return str(constant.chrome_driver)
    else:
        return str(get_chrome_driver())


def get_chrome_filename():
    """parse filename using platform"""
    platform = sys.platform
    platforms = {
        "win32": "win32",
        "win64": "win64",
        "linux": "linux64",
        "darwin": "mac64",
    }
    return 'chromedriver_{}.zip'.format(platforms.get(platform, ''))


def download_chrome_driver(version=None, mirror_url=None):
    """Download web webdrivers from URL"""
    version = version if version else DEFAULT_VERSION
    host = mirror_url if mirror_url else DEFAULT_DOWNLOAD_URL
    url = '/'.join([host, str(version), get_chrome_filename()])
    logging.info("Downloading webdriver. Please wait...")
    r = request.urlopen(url)
    logging.info("Downloading webdriver finished")
    return r


def save_chrome_driver(response, target=None):
    """Save the data of download_chrome_driver."""
    with tempfile.TemporaryFile() as f:
        f.write(response.read())
        zip_file = zipfile.ZipFile(f)
        if not zip_file:
            raise ValueError("Not a zip file format")
        for file in zip_file.filelist:
            target = target if target else constant.DRIVER_PATH
            abs_target = pathlib.Path(target).resolve()
            chrome_driver = pathlib.Path(abs_target) / file.filename
            if not chrome_driver.exists():
                zip_file.extract(file, abs_target)
            return str(chrome_driver)


def get_chrome_driver(target=None, version=None, mirror_url=None):
    """
    Get chrome webdrivers from mirror_url, save to target.
    :param target: the path dir to save the webdrivers
    :param version: webdrivers version
    :param mirror_url: resource url to get the webdrivers
    :return:
    """
    driver_data = download_chrome_driver(version, mirror_url)
    return save_chrome_driver(driver_data, target)
