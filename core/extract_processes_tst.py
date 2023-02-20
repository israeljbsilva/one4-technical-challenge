from datetime import timedelta

import pendulum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from services.services_browser import ServicesBrowser
from settings import (COURT_ID, END_DATE_ID, INITIAL_DATE_ID,
                      SEARCH_BUTTON_XPATH, URL, TABLE_DIARIES_ID)


class ExtractProcessesTST:

    def __init__(self):
        self.browser = self.start_browser_by_url()
        self.services_browser = ServicesBrowser(self.browser)

    @staticmethod
    def start_browser_by_url() -> WebDriver:
        browser = webdriver.Chrome()
        browser.get(URL)
        return browser

    def search_last_week_tst_diaries(self) -> None:
        start_date, end_date = self.get_start_end_dates_week()
        self.services_browser.fill_input_field(INITIAL_DATE_ID, start_date)
        self.services_browser.fill_input_field(END_DATE_ID, end_date)
        self.services_browser.fill_select_field_by_index(COURT_ID, 1)
        self.services_browser.click_button(SEARCH_BUTTON_XPATH)

    def _download_last_week_tst_diaries(self) -> None:
        table_with_diaries = self.browser.find_element(By.ID, TABLE_DIARIES_ID)
        rows = table_with_diaries.find_elements(By.TAG_NAME, "tr")[1:]
        first_line_table = 2

        for index, row in enumerate(rows, start=first_line_table):
            self.services_browser.click_button(f'//*[@id="diarioCon"]/fieldset/table/tbody/tr[{index}]/td[3]/button')

    @staticmethod
    def get_start_end_dates_week() -> tuple[str, str]:
        pendulum.week_starts_at(pendulum.SUNDAY)
        pendulum.week_ends_at(pendulum.SATURDAY)

        today = pendulum.now()
        start_date = (today.start_of('week') - timedelta(7)).strftime('%d/%m/%Y')
        end_date = (today.end_of('week') - timedelta(7)).strftime('%d/%m/%Y')

        return start_date, end_date
