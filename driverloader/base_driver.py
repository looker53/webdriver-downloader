import logging
import re
import tempfile
import zipfile
import pathlib
from urllib import request
from driverloader import config

DEFAULT_HOST = 'https://npm.taobao.org'

logging.basicConfig(level=logging.INFO)


class BaseDriver:
    host = DEFAULT_HOST
    pattern = r'<a href="(/mirrors/(chromedriver|geckodriver)/v?([0-9.]+)\/)">'

    def __init__(self, name, version, host=None):
        self.name = name
        if self.name == 'firefox':
            self.name = 'gecko'
        self.version = str(version)
        self.host = host or DEFAULT_HOST
        self.full_version = ''
        self.url = ''
        self.index_url = self.host + '/mirrors/' + self.name + 'driver'


    def __get__(self, instance, owner):
        return self.get_driver(config.DRIVER_PATH)

    @property
    def versions(self):
        r = request.urlopen(self.index_url)
        html = r.read().decode('utf8')
        regex = re.compile(self.pattern)
        for e in regex.finditer(html):
            url, version = e.group(1), e.group(3)
            yield url, version

    @property
    def _get_file(self):
        """parse filename using platform"""
        raise NotImplementedError("use child class")

    @property
    def full_version_and_url(self):
        for url, v in self.versions:
            if v.startswith(self.version):
                self.full_version = v
                self.url = self.host + url + self._get_file
                return self.full_version, self.url
        raise ValueError("no this version {}".format(self.version))

    def get(self, path=None, force=False):
        save_dir_str = path if path else config.DRIVER_PATH
        save_dir = pathlib.Path(save_dir_str).resolve()
        version = self.version

        if not force:
            gen = save_dir.iterdir()
            for f in gen:
                if version in f.name:
                    # logging.info(""" you get a driver:{}
                    # if you want to download any way, use force=True
                    # """.format(f))
                    return str(f)
        self.full_version_and_url
        driver_data = self.download()
        return self.save(driver_data, save_dir)

    def download(self):
        """Download web driver from URL"""
        logging.info("Downloading chrome webdriver. Please wait...")
        r = request.urlopen(self.url)
        logging.info("Downloading chrome webdriver finished")
        return r

    def save(self, response, path):
        """Save the data of download."""
        with tempfile.TemporaryFile() as f:
            f.write(response.read())
            zip_file = zipfile.ZipFile(f)
            if not zip_file:
                raise ValueError("Not a zip file format")
            for file in zip_file.filelist:
                download_file = zip_file.extract(file, path)
                download_file = pathlib.Path(download_file)
                new_name = download_file.stem + self.full_version + download_file.suffix
                new_target = path / new_name
                try:
                    download_file.rename(new_target)
                    return str(new_target)
                except FileExistsError:
                    download_file.unlink()
                    return str(new_target)
