import os
from datetime import datetime

import xlsxwriter


def generate_spreadsheets_per_day(diaries_separated_by_date: dict) -> None:
    for availability_date in diaries_separated_by_date:
        row = 0
        column = 0
        name_file = f'TST-{datetime.strptime(availability_date, "%d/%m/%Y").strftime("%d-%m-%Y")}.xlsx'

        workbook = xlsxwriter.Workbook(os.path.join(os.path.abspath(os.getcwd()), name_file))
        worksheet = workbook.add_worksheet()
        worksheet.write(row, column, 'Números de Processos')

        for process_number in diaries_separated_by_date[availability_date]:
            row += 1
            worksheet.write(row, column, process_number)

        workbook.close()
