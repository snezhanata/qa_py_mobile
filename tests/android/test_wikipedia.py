from selene import have
from selene.support.shared import browser
from allure import step

from wikipedia.model import app


def test_search():
    app.given_opened()
    with step('Verify content "BrowserStack" found'):
        browser.element('Search Wikipedia').click()
        browser.element('#search_src_text').type('BrowserStack')
        browser.all('#page_list_item_title').should(have.size_greater_than(0))

    # with step('Verify content "God of War: Ragnarok" found'):
    #     browser.element('#search_src_text').clear()
    #     browser.element('#search_src_text').type('God of War: Ragnarök')
    #     browser.all('#page_list_item_title').should(have.size_greater_than(0))