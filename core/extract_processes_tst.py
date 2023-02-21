import os.path
import sys
import time
from datetime import timedelta
from pathlib import Path

import pendulum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from services.services_browser import ServicesBrowser
from settings import (COURT_ID, END_DATE_ID, INITIAL_DATE_ID,
                      SEARCH_BUTTON_XPATH, TABLE_DIARIES_ID, URL)


class ExtractProcessesTST:

    def __init__(self):
        self.browser = self.start_browser_by_url()
        self.services_browser = ServicesBrowser(self.browser)

    @staticmethod
    def start_browser_by_url() -> WebDriver:
        if getattr(sys, 'frozen', False):
            chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            browser = webdriver.Chrome(chromedriver_path)
        else:
            browser = webdriver.Chrome()

        browser.get(URL)
        return browser

    def search_last_week_tst_diaries(self) -> dict:
        start_date, end_date = self.get_start_end_dates_week()
        self.services_browser.fill_input_field(INITIAL_DATE_ID, start_date)
        self.services_browser.fill_input_field(END_DATE_ID, end_date)
        self.services_browser.fill_select_field_by_index(COURT_ID, 1)
        self.services_browser.click_button(SEARCH_BUTTON_XPATH)

        return self._download_last_week_tst_diaries()

    def _download_last_week_tst_diaries(self) -> dict:
        table_with_diaries = self.browser.find_element(By.ID, TABLE_DIARIES_ID)
        rows = table_with_diaries.find_elements(By.TAG_NAME, "tr")[1:]
        first_line_table = 2

        diaries_separated_by_date = {}
        for index, row in enumerate(rows, start=first_line_table):
            availability_date = self.browser.find_element(
                By.XPATH, f'//*[@id="diarioCon"]/fieldset/table/tbody/tr[{index}]/td[1]/span').text
            title = self.browser.find_element(
                By.XPATH, f'//*[@id="diarioCon"]/fieldset/table/tbody/tr[{index}]/td[2]/span').text
            self.services_browser.click_button(f'//*[@id="diarioCon"]/fieldset/table/tbody/tr[{index}]/td[3]/button')
            self.is_download_finished()
            self.group_diaries_by_date(diaries_separated_by_date, availability_date, title)

        return diaries_separated_by_date

    @staticmethod
    def get_start_end_dates_week() -> tuple[str, str]:
        pendulum.week_starts_at(pendulum.SUNDAY)
        pendulum.week_ends_at(pendulum.SATURDAY)

        today = pendulum.now()
        start_date = (today.start_of('week') - timedelta(7)).strftime('%d/%m/%Y')
        end_date = (today.end_of('week') - timedelta(7)).strftime('%d/%m/%Y')

        return start_date, end_date

    @staticmethod
    def is_download_finished() -> None:
        path_download = str(Path.home() / 'Downloads')
        while True:
            if not sorted(Path(path_download).glob('*.crdownload')):
                break
            time.sleep(1)

    @staticmethod
    def group_diaries_by_date(diaries_separated_by_date: dict, availability_date: str, title: str) -> None:
        if availability_date not in diaries_separated_by_date:
            diaries_separated_by_date[availability_date] = [title]
        else:
            diaries_separated_by_date[availability_date].append(title)
