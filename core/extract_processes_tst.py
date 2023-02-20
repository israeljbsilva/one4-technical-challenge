from datetime import timedelta

import pendulum
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from services.services_browser import ServicesBrowser
from settings import (COURT_ID, END_DATE_ID, INITIAL_DATE_ID,
                      SEARCH_BUTTON_XPATH, URL)


class ExtractProcessesTST:

    def __init__(self):
        self.browser = self.start_browser_by_url()
        self.services_browser = ServicesBrowser(self.browser)

    @staticmethod
    def start_browser_by_url() -> WebDriver:
        browser = webdriver.Chrome()
        browser.get(URL)
        return browser

    def search_last_week_tst_diaries(self) -> dict:
        start_date, end_date = self.get_start_end_dates_week()
        self.services_browser.fill_input_field(INITIAL_DATE_ID, start_date)
        self.services_browser.fill_input_field(END_DATE_ID, end_date)
        self.services_browser.fill_select_field_by_index(COURT_ID, 1)
        self.services_browser.click_button(SEARCH_BUTTON_XPATH)

    @staticmethod
    def get_start_end_dates_week() -> tuple[str, str]:
        pendulum.week_starts_at(pendulum.SUNDAY)
        pendulum.week_ends_at(pendulum.SATURDAY)

        today = pendulum.now()
        start_date = (today.start_of('week') - timedelta(7)).strftime('%d/%m/%Y')
        end_date = (today.end_of('week') - timedelta(7)).strftime('%d/%m/%Y')

        return start_date, end_date
