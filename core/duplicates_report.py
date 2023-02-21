import os
from typing import Optional

import xlsxwriter


def generate_duplicates_report(diaries_separated_by_date: dict) -> None:
    process_number_by_dates = group_process_number_by_dates(diaries_separated_by_date)
    if process_number_by_dates:
        row = 0
        column = 0
        name_file = 'Relatorio de Duplicatas.xlsx'

        workbook = xlsxwriter.Workbook(os.path.join(os.path.abspath(os.getcwd()), name_file))
        worksheet = workbook.add_worksheet()
        worksheet.write(row, column, 'Números de Processos')
        worksheet.write(row, column+1, 'Data')

        for process_number in process_number_by_dates:
            for availability_date in process_number_by_dates[process_number]:
                row += 1
                worksheet.write(row, column, process_number)
                worksheet.write(row, column+1, availability_date)

            row += 1

        workbook.close()


def group_process_number_by_dates(diaries_separated_by_date: dict) -> Optional[dict]:
    process_number_by_dates = {}
    for availability_date in diaries_separated_by_date:
        for process_number in diaries_separated_by_date[availability_date]:
            if process_number not in process_number_by_dates:
                process_number_by_dates[process_number] = [availability_date]
            else:
                process_number_by_dates[process_number].append(availability_date)

    _remove_non_repeating_items(process_number_by_dates)
    return process_number_by_dates


def _remove_non_repeating_items(process_number_by_dates: dict) -> None:
    for process_number in list(process_number_by_dates):
        if len(process_number_by_dates[process_number]) == 1:
            process_number_by_dates.pop(process_number)
