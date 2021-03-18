import gspread
from example_credentials import *

def EXAMPLE(year):
    if year == 9:
        gc = gspread.service_account(filename=service_account_9_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        worksheet = sh.worksheet("YEAR9")

    elif year == 10:
        gc = gspread.service_account(filename=service_account_10_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        worksheet = sh.worksheet("YEAR10")

    elif year == 11:
        gc = gspread.service_account(filename=service_account_11_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        worksheet = sh.worksheet("YEAR11")

    elif year == 12:
        gc = gspread.service_account(filename=service_account_12_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        worksheet = sh.worksheet("YEAR12")

    elif year == 13:
        gc = gspread.service_account(filename=service_account_13_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        worksheet = sh.worksheet("YEAR13")  

