import pytest
from selene.support.shared import browser
from selene import browser
from selene import be, have


@pytest.fixture()
def browser_conf():
    browser.config.hold_browser_open = True
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    browser.open('https://google.com')
    return browser


def test_valid_text_input(browser_conf):
    browser.element('input[name=q]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_text_input(browser_conf):
    browser.element('input[name=q]').should(be.blank).type('qwewqefgrhhrfhhfhfhdhdhfshdfhsdf').press_enter()
    browser.element('div[class="card-section"]').should(have.text('ничего не найдено'))
