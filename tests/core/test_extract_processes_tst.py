from unittest import mock

from freezegun import freeze_time

from core.extract_processes_tst import ExtractProcessesTST


@mock.patch("core.extract_processes_tst.ExtractProcessesTST.get_start_end_dates_week")
def test_must_extract_processes_tst(mock_get_start_end_dates_week):
    mock_get_start_end_dates_week.return_value = ('16/02/2023', '17/02/2023', )

    extract_processes_tst = ExtractProcessesTST()
    diaries_separated_by_date = extract_processes_tst.search_last_week_tst_diaries()

    assert diaries_separated_by_date == {
        '17/02/2023': [
            'Edição 3666/2023 - Caderno do Tribunal Superior do Trabalho - Judiciário',
            'Edição 3666/2023 - Caderno do Tribunal Superior do Trabalho - Administrativo'
        ],
        '16/02/2023': [
            'Edição 3665/2023 - Caderno do Tribunal Superior do Trabalho - Judiciário',
            'Edição 3665/2023 - Caderno do Tribunal Superior do Trabalho - Administrativo'
        ]
    }


@freeze_time("2023-02-20")
def test_must_get_start_end_dates_week():
    start_date, end_date = ExtractProcessesTST().get_start_end_dates_week()

    assert start_date == '12/02/2023'
    assert end_date == '18/02/2023'
