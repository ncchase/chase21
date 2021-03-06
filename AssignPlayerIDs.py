import gspread
from credentials import *

def AssignPlayerIDs():
    gc = gspread.service_account(filename=service_account_filepath)
    sh = gc.open_by_key(spreadsheetkey)
    worksheet = sh.worksheet("MASTER USER TABLE")


confirmation = input("Are you sure you want to assign Player IDs? This will overwrite the existing IDs.\nTHIS IS IRREVERSIBLE\nYES or NO\n")

if confirmation == "YES":
    AssignPlayerIDs()
else:
    print("Cancelled")
