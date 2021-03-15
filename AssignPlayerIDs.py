from random import shuffle
import gspread
<<<<<<< Updated upstream
from credentials import *
=======
from example_credentials import spreadSheetKey, service_account_filepath
>>>>>>> Stashed changes

numberOfy9 = 0
numberOfy10 = numberOfy9 + 0
numberOfy11 = numberOfy10 + 0
numberOfy12 = numberOfy11 + 0
numberOfy13 = numberOfy12 + 0

def AssignPlayerIDs():
    gc = gspread.service_account(filename=service_account_9_filepath)
    sh = gc.open_by_key(spreadsheet_key)
    YEAR9 = sh.worksheet("YEAR9")
    YEAR10 = sh.worksheet("YEAR10")
    YEAR11 = sh.worksheet("YEAR11")
    YEAR12 = sh.worksheet("YEAR12")
    YEAR13 = sh.worksheet("YEAR13")
    As = ["A{}".format(i) for i in range(101, 500)]
    Bs = ["B{}".format(i) for i in range(101, 500)]
    Cs = ["C{}".format(i) for i in range(101, 500)]
    Ds = ["D{}".format(i) for i in range(101, 500)]
    allID = As + Bs + Cs + Ds
    shuffle(allID)
    YEAR9.update("A2:A{}".format(numberOfy9 + 1), allID[:numberOfy9])
    YEAR10.update("A2:A{}".format(numberOfy10 + 1), allID[numberOfy9:numberOfy10])
    YEAR11.update("A2:A{}".format(numberOfy11 + 1), allID[numberOfy10:numberOfy11])
    YEAR12.update("A2:A{}".format(numberOfy12 + 1), allID[numberOfy11:numberOfy12])
    YEAR13.update("A2:A{}".format(numberOfy13 + 1), allID[numberOfy13:numberOfy9])

confirmation = input("Are you sure you want to assign Player IDs? This will overwrite the existing IDs.\nTHIS IS IRREVERSIBLE\nYES or NO\n")

if confirmation == "YES":
    AssignPlayerIDs()
else:
    print("Cancelled")
