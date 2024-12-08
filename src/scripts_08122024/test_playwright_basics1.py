import pytest
import allure
from playwright.sync_api import expect , sync_playwright


def test_hola():
    #browser setup
    browser = sync_playwright().start().chromium.launch(headless=False)
    # context setup
    context = browser.new_context()
    # page setup
    page = context.new_page()
    page.goto('https://google.com/')

    expect(page).to_have_title('Google')

# testing multiple contexts
def test_multiple_context():
    browser= sync_playwright().start().chromium.launch(headless=False)
    context1 = browser.new_context()
    context2 = browser.new_context()
    page1= context1.new_page()
    page2 = context2.new_page()
    page1.goto('https://google.com/')
    page2.goto('https://www.bing.com/')




