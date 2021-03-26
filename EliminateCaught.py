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
        
        sh = gc.open_by_key(spreadsheet_key)
        Y9Sheet = sh.worksheet("YEAR9")
        Y9 = np.array(Y9Sheet.get_all_values())

        Y9RSheet = sh.worksheet("YEAR9_REMOVED")
        Y9R = np.array(Y9RSheet.get_all_values())

        Y10Sheet = sh.worksheet("YEAR10")
        Y10 = np.array(Y10Sheet.get_all_values())

        Y10R = sh.worksheet("YEAR10_REMOVED")
        Y10 = np.array(Y10R.get_all_values())

        Y11Sheet = sh.worksheet("YEAR11")
        Y11 = np.array(Y11Sheet.get_all_values())

        Y11RSheet = sh.worksheet("YEAR11_REMOVED")
        Y11R = np.array(Y11RSheet.get_all_values())

        Y12Sheet = sh.worksheet("YEAR12")
        Y12 = np.array(Y12Sheet.get_all_values())

        Y12RSheet = sh.worksheet("YEAR12_REMOVED")
        Y12R = np.array(Y12RSheet.get_all_values())

        FCSheet = sh.worksheet("FORM_CAUGHT")
        FC = np.array(FCSheet.get_all_values())

        FCRSheet = sh.worksheet("FORM_CAUGHT_REMOVED")
        FCR = np.array(FCRSheet.get_all_values())

        # Creating lists of Player:Target pairs to validate against
        # PTL = Player Target List

        Y9PTL = [[player, target] for player, target in zip(list(Y9[:,0]), list(Y9[:,6]))]
        Y10PTL = [[player, target] for player, target in zip(list(Y10[:,0]), list(Y10[:,6]))]
        Y11PTL = [[player, target] for player, target in zip(list(Y11[:,0]), list(Y11[:,6]))]
        Y12PTL = [[player, target] for player, target in zip(list(Y12[:,0]), list(Y12[:,6]))]

        # Creating list of IDs for each year group
        Y9ID, Y10ID, Y11ID, Y12ID = Y9[:,0], Y10[:,0], Y11[:,0], Y12[:,0]

        # Removing headings 
        del Y9PTL[0], Y10PTL[0], Y11PTL[0], Y12PTL[0]

        # Creating main PTL list
        PTL = Y9PTL + Y10PTL + Y11PTL + Y12PTL
        
        # print(PTL)
        # print(len(PTL))
        
        CF_PTL = [[chaser, runner] for chaser, runner in zip(list(FC[:,2]), list(FC[:,3]))]
        del CF_PTL[0]
        

        # Iterating through entries in the CF Sheet
        for pair_num in range(1,len(PTL) + 1):
            print(pair_num, "hello")
            if CF_PTL[pair_num] in PTL:
                # Finding index of the runner in the main sh eet

                if CF_PTL[pair_num] in Y9PTL:
                    
            
if __name__ == "__main__":
    Eliminate()
