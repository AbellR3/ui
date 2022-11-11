from BaseClass import BasePage
from selenium.webdriver.common.by import By
import allure


class GoogleLocator:
    lucky_button = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]')


class GooglePage(BasePage):
    def click_lucky_button(self):
        button = self.find_element(GoogleLocator.lucky_button)
        with allure.step(f'Нажимаю на кнопку {GoogleLocator.lucky_button}'):
            try:
                button.click()
            except Exception as e:
                allure.attach(
                        self.driver.get_screenshot_as_png(),
                        name='screenshot',
                        attachment_type=allure.attachment_type.PNG
            )
                raise AssertionError(f'Exeption {e}')