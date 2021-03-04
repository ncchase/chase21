import gspread
from credentials import *

gc = gspread.service_account(filename=service_account_filepath)
sh = gc.open_by_key(spreadsheetkey)
worksheet = sh.worksheet("INSERT_WORKSHEET_NAME")

