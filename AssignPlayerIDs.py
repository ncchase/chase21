from random import shuffle
import gspread
from credentials import *

def AssignPlayerIDs():
    gc = gspread.service_account(filename = service_account_9_filepath, scopes = gspread.auth.DEFAULT_SCOPES)
    sh = gc.open_by_key(spreadsheet_key)
    YEAR9 = sh.worksheet("YEAR9")
    YEAR10 = sh.worksheet("YEAR10")
    YEAR11 = sh.worksheet("YEAR11")
    YEAR12 = sh.worksheet("YEAR12")
    YEAR13 = sh.worksheet("YEAR13")

    # Getting Number of players in each year by getting length of list, of column of peoples first names. Minus once to exclude the header row.    
    NOY9 = len(YEAR9.col_values(2)) - 1
    NOY10 = len(YEAR10.col_values(2)) - 1
    NOY11 = len(YEAR11.col_values(2)) - 1
    NOY12 = len(YEAR12.col_values(2)) - 1
    NOY13 = len(YEAR13.col_values(2)) - 1
    
    # # Uncomment for Testing.
    # NOY9 = 80
    # NOY10 = 80
    # NOY11 = 80
    # NOY12 = 80
    # NOY13 = 80

    pre = 0
    As = [["A{}".format(i)] for i in range(101, 500)]
    Bs = [["B{}".format(i)] for i in range(101, 500)]
    Cs = [["C{}".format(i)] for i in range(101, 500)]
    Ds = [["D{}".format(i)] for i in range(101, 500)]
    allID = As + Bs + Cs + Ds
    shuffle(allID)
    YEAR9.update("A2:A{}".format(NOY9 + 1), allID[:NOY9])
    pre += NOY9
    YEAR10.update("A2:A{}".format(NOY10 + 1), allID[pre:NOY10 + pre])
    pre += NOY10
    YEAR11.update("A2:A{}".format(NOY11 + 1), allID[pre:NOY11 + pre])
    pre += NOY11
    YEAR12.update("A2:A{}".format(NOY12 + 1), allID[pre:NOY12 + pre])
    pre += NOY12
    YEAR13.update("A2:A{}".format(NOY13 + 1), allID[pre:NOY13 + pre])

    
# AssignPlayerIDs()
confirmation = input("Are you sure you want to assign Player IDs? This will overwrite the existing IDs.\nTHIS IS IRREVERSIBLE\nYES or NO\n")

if confirmation == "YES":
    AssignPlayerIDs()
else:
    print("Cancelled")
