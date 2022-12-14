from PageObj.Google import GooglePage


def test_lucky_button(browser):
    page = GooglePage(browser)
    page.click_lucky_button()
    assert browser.current_url == "https://www.google.com/doodles"

def test_create_page(browser):
    page = GooglePage(browser)
    page.click_lucky_button()
    browser.back()
    assert browser.current_url == "https://www.google.ru/", 'Not correct url'
