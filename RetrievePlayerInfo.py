import gspread
from credentials import *
import random
import numpy as np

def Retrieveinfo():

    # Retrieve information from user
    print("Please enter valid ID's and then press enter, type 'f' when complete.")
    players_to_retrieve = []
    id = "D"

    # Taking input
    while id.lower() != "f":
        id = input("")
        players_to_retrieve.append(id)

    players_to_retrieve.remove("f")

    # Signing into service account & allowing access
    gc = gspread.service_account(filename=service_account_10_filepath)
    sh = gc.open_by_key(spreadsheet_key)
    
    # Creating (numpy) array of all players (includes all removed players)
    players = np.array([])
    for year in range(9,14):
        year_sheet = sh.worksheet("YEAR" + str(year))
        year_removed_sheet = sh.worksheet("YEAR" + str(year) + "_REMOVED")
        year_sheet_data = np.array(year_sheet.get_all_values())
        year_sheet_removed_data = np.array(year_removed_sheet.get_all_values())
        
        if year == 9:
            players = year_sheet_data
        else:
            players = np.vstack((players, year_sheet_data))
        
        # print(year_sheet_removed_data, "year removed")          
        if len(year_sheet_removed_data) > 1:
            player = np.vstack((player, year_sheet_removed_data))
        
        # Following lines if you want to print when no players in a year have yet been removed
        # else:
        #     print("No players removed in year " + str(year))

    playerID_list = list(players[:,0])

    # Iterating through ID's given, finding matching index within sheet and appending that index's data to the return_list

    return_list = []

    for ID in players_to_retrieve:
        if ID in playerID_list:
            player_index = playerID_list.index(ID)
            # print("\n")
            return_list.append(list(players[player_index,:]))
            # print(list(players[player_index,:]))     
        else:
            print("\n" + ID + " is not a valid ID")

    return return_list


if __name__ =="__main__":
    info = Retrieveinfo()
    print((info[0])[0])
