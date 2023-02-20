from core.extract_processes_tst import ExtractProcessesTST
from core.generate_spreadsheets import generate_spreadsheets_per_day

if __name__ == "__main__":
    extract_processes_tst = ExtractProcessesTST()
    diaries_separated_by_date = extract_processes_tst.search_last_week_tst_diaries()

    generate_spreadsheets_per_day(diaries_separated_by_date)
