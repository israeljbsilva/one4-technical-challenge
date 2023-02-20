from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select


class ServicesBrowser:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def fill_input_field(self, element_id: str, value: str) -> None:
        field = self.browser.find_element(By.ID, element_id)
        field.clear()
        field.send_keys(value)

    def fill_select_field_by_index(self, element_id: str, index_option: int) -> None:
        field = Select(self.browser.find_element(By.ID, element_id))
        field.select_by_index(index_option)

    def click_button(self, element_xpath: str) -> None:
        self.browser.find_element(By.XPATH, element_xpath).click()
