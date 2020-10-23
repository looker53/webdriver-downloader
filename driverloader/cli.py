import click
from driverloader.chrome_driver import ChromeDriver, DEFAULT_CHROME_VERSION
from driverloader.firefox_driver import FirefoxDriver, DEFAULT_FIREFOX_VERSION


def download_driver(name: str, dst=None, version=None, force=False):
    if name.lower() == 'chrome':
        version = version or DEFAULT_CHROME_VERSION
        return ChromeDriver(version=version).get(dst, force=force)
    elif name.lower() == 'firefox':
        version = version or DEFAULT_FIREFOX_VERSION
        return FirefoxDriver(version=version).get(dst, force=force)
    raise ValueError("name must be chrome or firefox")


@click.command()
@click.argument('driver_name', type=click.Choice(['chrome', 'firefox']))
@click.argument('path', type=click.Path(exists=True))
@click.option('-v', '--version')
@click.option('-f', '--force')
def cli(driver_name, path, version, force):
    """Webdriver downloader  of chrome and firefox.

    - driver_name: Which driver, [chrome, firefox] supported.\n
    - path: Path to save the driver.
    """
    driver = download_driver(driver_name, dst=path, version=version, force=force)
    click.echo(driver)


if __name__ == '__main__':
    cli()
