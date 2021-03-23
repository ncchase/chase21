from random import shuffle
import gspread
from credentials import *

def AssignPlayerIDs():

    # Accessing spreadsheet
    gc = gspread.service_account(filename=service_account_9_filepath)
    sh = gc.open_by_key(spreadsheet_key)
    
    # Assigning sheets to arrays dependent on year group
    YEAR9 = sh.worksheet("YEAR9")
    YEAR10 = sh.worksheet("YEAR10")
    YEAR11 = sh.worksheet("YEAR11")
    YEAR12 = sh.worksheet("YEAR12")
    # YEAR13 = sh.worksheet("YEAR13") # YEAR 13 REMOVED

    # Getting Number of players in each year by getting length of list, of column of peoples first names. Minus once to exclude the header row.    
    NOY9 = len(YEAR9.col_values(2)) - 1
    NOY10 = len(YEAR10.col_values(2)) - 1
    NOY11 = len(YEAR11.col_values(2)) - 1
    NOY12 = len(YEAR12.col_values(2)) - 1
    # NOY13 = len(YEAR13.col_values(2)) - 1 # YEAR 13 REMOVED

    pre = 0
    list_of_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "K", "M", "R", "T", "X"]
    all_id_list = []

    for letter in list_of_letters:
        new_letter_list = [[letter + "{}".format(i)] for i in range(101, 500)]
        all_id_list += new_letter_list

    shuffle(all_id_list)
    
    YEAR9.update("A2:A{}".format(NOY9 + 1), all_id_list[:NOY9])
    pre += NOY9
    YEAR10.update("A2:A{}".format(NOY10 + 1), all_id_list[pre:NOY10 + pre])
    pre += NOY10
    YEAR11.update("A2:A{}".format(NOY11 + 1), all_id_list[pre:NOY11 + pre])
    pre += NOY11
    YEAR12.update("A2:A{}".format(NOY12 + 1), all_id_list[pre:NOY12 + pre])
    # pre += NOY12
    # YEAR13.update("A2:A{}".format(NOY13 + 1), all_id_list[pre:NOY13 + pre]) # YEAR 13 REMOVED

    
confirmation = input("Are you sure you want to assign Player IDs? This will overwrite the existing IDs.\nTHIS IS IRREVERSIBLE\nYES or NO\n\n")

if confirmation == "YES":
    AssignPlayerIDs()
    print("Player ID Assign Complete")
else:
    print("Cancelled...")
    

