import pytest
from selenium import webdriver

CHROME_URL = "http://0.0.0.0:4444/wd/hub"

@pytest.fixture(scope='session')
def browser(request):
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor= CHROME_URL,
        options=chrome_options
    )
    def tear_down():
        driver.quit()

    request.addfinalizer(tear_down)
    return driver
