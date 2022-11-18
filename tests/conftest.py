import os
import pytest
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from appium import webdriver

from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options

from wikipedia.util import attachments


@pytest.fixture(scope='session', autouse=True)
def driver_management():
    load_dotenv()
    USER_NAME = os.getenv('USER_NAME')
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    APPIUM_BROWSERSTACK = os.getenv('APPIUM_BROWSERSTACK')
    options = UiAutomator2Options()

    options.load_capabilities({
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        "deviceName": "Google Pixel 3",
        "platformVersion": "9.0",
        "platformName": "android",
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
    browser.config.timeout = 4
    yield driver_management
    attachments.add_video(browser)
    browser.quit()



