import gspread
from credentials import *


def EmailCaught():
    # Signing into service account & allowing access
        gc = gspread.service_account(filename=service_account_11_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        worksheet = sh.worksheet("YEAR9")



        