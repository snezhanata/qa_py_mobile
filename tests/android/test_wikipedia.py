from selene import have, be
from selene.support.shared import browser
from allure import step

import config

from wikipedia.model import app


def test_search():
    app.given_opened()
    with step('Verify content "BrowserStack" found'):
        browser.element('Search Wikipedia').click()
        browser.element('#search_src_text').type('BrowserStack')
        browser.all('#page_list_item_title').should(have.size_greater_than(0))

    with step('Verify content "God of War: Ragnarok" found'):
        browser.element('#search_src_text').clear()
        browser.element('#search_src_text').type('God of War: Ragnarök')
        browser.all('#page_list_item_title').should(have.size_greater_than(0))


if not config.settings.run_on_browserstack:

    def test_getting_started():
        with step('Onboard screen verification'):
            browser.element('#primaryTextView').should(
                have.text('The Free Encyclopedia\n…in over 300 languages')
            )
            browser.element('#fragment_onboarding_forward_button').click()
            browser.element('#primaryTextView').should(have.text('New ways to explore'))
            browser.element('#fragment_onboarding_forward_button').click()
            browser.element('#secondaryTextView').should(
                have.text(
                    'You can make reading lists from articles you want to read later, even when you’re offline. '
                    '\nLogin to your Wikipedia account to sync your reading lists. Join Wikipedia'
                )
            )
            browser.element('#fragment_onboarding_forward_button').click()
            browser.element('#switchView').click()
            browser.element('#switchView').should(
                have.attribute('checked').value('false')
            )
            browser.element('#fragment_onboarding_done_button').click()
            browser.element('#main_toolbar_wordmark').should(be.present)
