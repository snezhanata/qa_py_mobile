import os

import allure
import pytest
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from appium import webdriver

from selene.support.shared import browser
# from selenium.webdriver.chrome.options import Options

from wikipedia.util import attachments

load_dotenv()
USER_NAME = os.getenv('USER_NAME')
ACCESS_KEY = os.getenv('ACCESS_KEY')
PLATFORM_NAME = os.getenv('PLATFORM_NAME')
options = UiAutomator2Options()


@pytest.fixture(scope='session', autouse=True)
def driver_management():

    options.load_capabilities({
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        "deviceName": "Google Pixel 3",
        "platformVersion": "9.0",
        "platformName": f"{PLATFORM_NAME}",
        "project": "Python project",
        "build": "wikipedia-build-qa_guru",
        'bstack:options': {
            "projectName": "Wikipedia project",
            "buildName": "wikipedia-build-01",
            "sessionName": "BStack first_test",
            "userName": f"{USER_NAME}",
            "accessKey": f"{ACCESS_KEY}",
        }
    })
    browser.config.driver = webdriver.Remote(
        command_executor="http://hub.browserstack.com/wd/hub",
        options=options,
    )
    browser.config.timeout = 2
    yield driver_management
    allure.step('Close app session')(browser.quit)()  # завернем в аллюр степ
    # attachments.add_video(browser)
    browser.quit()



@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import wikipedia.extension.selene.patch_selector  # noqa


