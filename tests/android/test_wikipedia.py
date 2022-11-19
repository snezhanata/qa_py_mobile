from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from allure import step


def test_search_on_wikipedia():
    with step('Search and verify content "BrowserStack" found'):
        browser.element('Search Wikipedia').click()
        browser.element('#search_src_text').type('BrowserStack')
        browser.all('#page_list_item_title').should(have.size_greater_than(0))

    with step('Search and verify content "God of War: Ragnarok" found'):
        browser.element('#search_src_text').clear()
        browser.element('#search_src_text').type('God of War: Ragnarök')
        browser.all('#page_list_item_title').should(have.size_greater_than(0))