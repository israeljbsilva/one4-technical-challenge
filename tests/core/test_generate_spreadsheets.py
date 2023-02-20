import os

from core.generate_spreadsheets import generate_spreadsheets_per_day


def test_must_generate_spreadsheets_per_day():
    diaries_separated_by_date = {
        '17/02/2023': [
            'Edição 3666/2023 - Caderno do Tribunal Superior do Trabalho - Judiciário',
            'Edição 3666/2023 - Caderno do Tribunal Superior do Trabalho - Administrativo'
        ],
        '16/02/2023': [
            'Edição 3665/2023 - Caderno do Tribunal Superior do Trabalho - Judiciário',
            'Edição 3665/2023 - Caderno do Tribunal Superior do Trabalho - Administrativo'
        ]
    }

    generate_spreadsheets_per_day(diaries_separated_by_date)

    path_spreadsheets = os.path.abspath(os.getcwd())
    assert os.path.isfile(os.path.join(path_spreadsheets, 'TST-16-02-2023.xlsx')) is True
    assert os.path.isfile(os.path.join(path_spreadsheets, 'TST-17-02-2023.xlsx')) is True
