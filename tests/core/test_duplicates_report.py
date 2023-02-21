import os

from core.duplicates_report import (generate_duplicates_report,
                                    group_process_number_by_dates)


def test_must_group_process_number_by_dates():
    diaries_separated_by_date = {
        '17/02/2023': [
            'Edição 3666/2023 - Caderno do Tribunal Superior do Trabalho - Judiciário',
            'Edição 3666/2023 - Caderno do Tribunal Superior do Trabalho - Administrativo'
        ],
        '16/02/2023': [
            'Edição 3666/2023 - Caderno do Tribunal Superior do Trabalho - Judiciário',
            'Edição 3665/2023 - Caderno do Tribunal Superior do Trabalho - Administrativo'
        ]
    }

    process_number_by_dates = group_process_number_by_dates(diaries_separated_by_date)

    assert process_number_by_dates == {
        'Edição 3666/2023 - Caderno do Tribunal Superior do Trabalho - Judiciário': ['17/02/2023', '16/02/2023']
    }


def test_must_generate_duplicates_report():
    diaries_separated_by_date = {
        '17/02/2023': [
            'Edição 3666/2023 - Caderno do Tribunal Superior do Trabalho - Judiciário',
            'Edição 3666/2023 - Caderno do Tribunal Superior do Trabalho - Administrativo'
        ],
        '16/02/2023': [
            'Edição 3666/2023 - Caderno do Tribunal Superior do Trabalho - Judiciário',
            'Edição 3665/2023 - Caderno do Tribunal Superior do Trabalho - Administrativo'
        ],
        '15/02/2023': [
            'Edição 3663/2023 - Caderno do Tribunal Superior do Trabalho - Administrativo',
            'Edição 3664/2023 - Caderno do Tribunal Superior do Trabalho - Administrativo'
        ],
        '14/02/2023': [
            'Edição 3664/2023 - Caderno do Tribunal Superior do Trabalho - Administrativo',
        ],
    }

    generate_duplicates_report(diaries_separated_by_date)

    path_spreadsheets = os.path.abspath(os.getcwd())
    assert os.path.isfile(os.path.join(path_spreadsheets, 'Relatorio de Duplicatas.xlsx')) is True
