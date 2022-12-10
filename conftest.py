import pytest
import os
import itertools as it

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver import Remote, DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        nargs=1,
        type=str.lower,
        choices=["chrome", "firefox", "safari", "opera"],
        default=["chrome"],
        help="browsers to tests_files with (choose from 'chrome', 'firefox', 'safari', 'opera')"
    )


def is_headless():
    return os.getenv('HEADLESS_MODE', '1').lower() in ('yes', 'y', 'true', 't', '1')


def grouper(item):
    return item.nodeid[:item.nodeid.rfind('[')]


def pytest_collection_modifyitems(config, items):
    """
    This function differentiate tests_files results between different browsers in the Bamboo
    :param config:
    :param items:
    """
    browser = config.getoption('browser')[0]
    for _, group in it.groupby(items, grouper):
        for i, item in enumerate(group):
            item._nodeid = item._nodeid.replace("::", "::" + browser + "_", 1)


@pytest.fixture
def base_url():
    return os.getenv('BASE_URL', 'https://mikewencel.github.io/thesis_web/')


def base_url_animals():
    return 'https://mikewencel.github.io/thesis_web/'


@pytest.fixture
def driver(base_url, request):
    browser = request.config.getoption("browser")[0]
    selenoid_url = os.getenv('SELENOID_URL', '').lower().strip()

    if selenoid_url:
        caps = {
            'chrome':DesiredCapabilities.CHROME.copy(),
            'firefox': DesiredCapabilities.FIREFOX.copy()
        }
    else:
        if browser == 'chrome':
            driver = _chrome_driver()
        elif browser == 'firefox':
            driver = _firefox_driver()
        else:
            raise Exception("Sorry, in local mode only firefox and chrome are supported at this time")

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        request.cls.driver = driver

        yield driver
        driver.quit()


def _chrome_driver():
    opts = ChromeOptions()
    if is_headless():
        opts.add_argument('--headless')
        opts.add_argument("--window-size=1920,1080")
    return Chrome(ChromeDriverManager().install(), options=opts)


def _firefox_driver():
    opts = FirefoxOptions()
    return Firefox(executable_path=GeckoDriverManager().install(), options=opts)
