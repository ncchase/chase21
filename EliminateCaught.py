# This script iterates through the caught form, and eliminates players who have been caught. It also validates etcetc.

# 2020 version of this script at https://github.com/ncchase/NC-Chase/blob/master/RemovePlayersV3.py
    
import gspread
from credentials import *
import random
import numpy as np
import logging

def Eliminate():

    gc = gspread.service_account(filename=service_account_13_filepath)

    # Importing data of ALL year groups + removed players sheets + caught form sheets + caught form removed sheets
    
    np.set_printoptions(threshold=np.inf)

    sh = gc.open_by_key(spreadsheet_key)
    Y9Sheet = sh.worksheet("YEAR9")
    Y9 = np.array((Y9Sheet.get_all_values()[1:]))

    Y9RSheet = sh.worksheet("YEAR9_REMOVED")
    Y9R = np.array(Y9RSheet.get_all_values()[1:])

    Y10Sheet = sh.worksheet("YEAR10")
    Y10 = np.array(Y10Sheet.get_all_values()[1:])

    Y10RSheet = sh.worksheet("YEAR10_REMOVED")
    Y10R = np.array(Y10RSheet.get_all_values()[1:])

    Y11Sheet = sh.worksheet("YEAR11")
    Y11 = np.array(Y11Sheet.get_all_values()[1:])

    Y11RSheet = sh.worksheet("YEAR11_REMOVED")
    Y11R = np.array(Y11RSheet.get_all_values()[1:])

    Y12Sheet = sh.worksheet("YEAR12")
    Y12 = np.array(Y12Sheet.get_all_values()[1:])

    Y12RSheet = sh.worksheet("YEAR12_REMOVED")
    Y12R = np.array(Y12RSheet.get_all_values()[1:])

    FCSheet = sh.worksheet("FORM_CAUGHT")
    FC = np.array(FCSheet.get_all_values()[1:])

    FCRSheet = sh.worksheet("FORM_CAUGHT_REMOVED")
    FCR = np.array(FCRSheet.get_all_values()[1:])

    # Creating lists of Player:Target pairs to validate against
    # PTL = Player Target List

    Y9PTL = [[player, target] for player, target in zip(list(Y9[:,0]), list(Y9[:,6]))]
    Y10PTL = [[player, target] for player, target in zip(list(Y10[:,0]), list(Y10[:,6]))]
    Y11PTL = [[player, target] for player, target in zip(list(Y11[:,0]), list(Y11[:,6]))]
    Y12PTL = [[player, target] for player, target in zip(list(Y12[:,0]), list(Y12[:,6]))]

    # Creating list of IDs for each year group
    Y9ID, Y10ID, Y11ID, Y12ID = list(Y9[:,0]), list(Y10[:,0]), list(Y11[:,0]), list(Y12[:,0])




    # Removing headings 
    # del Y9PTL[0], Y10PTL[0], Y11PTL[0], Y12PTL[0]

    # Creating main PTL list
    PTL = Y9PTL + Y10PTL + Y11PTL + Y12PTL
    # print(PTL, "PTL")
    # print(len(PTL), "PTL Len")
    
    # print(PTL)
    # print(len(PTL))
    
    # Creating PTL list from the caught form
    CF_PTL = [[chaser, runner] for chaser, runner in zip(list(FC[:,2]), list(FC[:,3]))]
    print(CF_PTL, "Caught form player:runner list")
    
    # Creating "remove" and "add point" lists
    Y9R, Y10R, Y11R, Y12R = [], [], [], []
    Y9AP, Y10AP, Y11AP, Y12AP = [], [], [], []

    # Iterating through entries in the CF Sheet
    for pair_num in range(0,(len(CF_PTL))):

        pair = CF_PTL[pair_num]
        chaser, runner = pair[0], pair[1]


        # Creating players-to-be-removed dictionary. Data is stored in "*player index*:*player data*" format
            # Y9R,Y10R,Y11R,Y12R = {}
            
        # Checking if player:target list exists at all (inefficient but too much effort to change rn)
        if CF_PTL[pair_num] in PTL:
            # Finding index of the runner in the main sh eet

            # Checks if the player:target pair exists in each sheet and if so, will add the runner to the "remove" list and the chaser to the "add one point list"
            if CF_PTL[pair_num] in Y9PTL:

                Y9R.append(Y9ID.index(runner))
                Y9AP.append(Y9ID.index(chaser))
            elif CF_PTL[pair_num] in Y10PTL:
                Y10R.append(Y10ID.index(runner))
                Y10AP.append(Y10ID.index(chaser))
            elif CF_PTL[pair_num] in Y11PTL:
                Y11R.append(Y11ID.index(runner))
                Y11AP.append(Y11ID.index(chaser))
            elif CF_PTL[pair_num] in Y12PTL:
                Y12R.append(Y12ID.index(runner))
                Y12AP.append(Y12ID.index(chaser))
        else:
            # Code for invalid ID to be added here --> logging smth smth?
            # Save invalid entries to variable --> notify
            print("Invalid ID", pair)

    # Printing removal and add point lists
    print(Y9R, Y9AP, "Y9 R AP")
    print(Y10R, Y10AP, "Y10 R AP")
    print(Y11R, Y11AP, "Y11 R AP")
    print(Y12R, Y12AP, "Y12 R AP")

    # Adding points to players who have caught their runners
    # AP = Add points 
    # CI = Chaser Index
    for Y9CI  in Y9AP:
        catches = int(Y9[int(Y9CI), 11])
        Y9[int(Y9CI), 11] = str(int(catches + 1))

    for Y10CI in Y10AP:
        catches = int(Y10[int(Y10CI), 11])
        Y10[int(Y10CI), 11] = str(int(catches + 1))

    for Y11CI in Y11AP:
        catches = int(Y11[int(Y11CI), 11])
        Y11[int(Y11CI), 11] = str(int(catches + 1))

    for Y12CI in Y12AP:
        catches = int(Y12[int(Y12CI), 11])
        Y12[int(Y12CI), 11] = str(int(catches + 1))
    
    # Ordering deletion indexes so that deletion of one entry does not change the index of all other entries
    Y9R.sort(reverse=True), Y10R.sort(reverse=True), Y11R.sort(reverse=True), Y12R.sort(reverse=True)

    # print(Y9, Y10, Y11, Y12)
    print(Y9R, Y10R, Y11R, Y12R, "Player indexes to be removed from each year sheet")
    
    # Adding caught players into respective caught removed sheets
    Y9RSheet.append_rows(Y9R, value_input_option="USER_ENTERED")
    Y10RSheet.append_rows(Y10R, value_input_option="USER_ENTERED")
    Y11RSheet.append_rows(Y11R, value_input_option="USER_ENTERED")
    Y12RSheet.append_rows(Y12R, value_input_option="USER_ENTERED")

    # Deleting caught players from local version of sheet(s)
    for player in Y9R:
        print(Y9[player])
        Y9 = np.delete(Y9, player, 0)
    for player in Y10R:
        Y10 = np.delete(Y10, player, 0)
    for player in Y11R:
        Y11 = np.delete(Y11, player, 0)
    for player in Y12R:
        Y12 = np.delete(Y12, player, 0)

    # print(Y9)
    print(len(Y9))
    
    # Deleting Sheet for updating
    # print(len(Y9), "Y9LEN")
    Y9Sheet.delete_rows(2, len(Y9)+ 1)
    Y10Sheet.delete_rows(2, len(Y10)+ 1)
    Y11Sheet.delete_rows(2, len(Y11)+ 1)
    Y12Sheet.delete_rows(2, len(Y12)+ 1)
    
    # Update all player sheets to new version with removed players
    Y9Sheet.update("A2:M" + str(len(Y9) + 1), Y9.tolist(), value_input_option="USER_ENTERED")
    Y10Sheet.update("A2:M" + str(len(Y10) + 1), Y10.tolist(), value_input_option="USER_ENTERED")
    Y11Sheet.update("A2:M" + str(len(Y11) + 1), Y11.tolist(), value_input_option="USER_ENTERED")
    Y12Sheet.update("A2:M" + str(len(Y12) + 1), Y12.tolist(), value_input_option="USER_ENTERED")


    
if __name__ == "__main__":
    
    Eliminate()
