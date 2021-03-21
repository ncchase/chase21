import gspread
import random
from operator import itemgetter
from example_credentials import *

# gc = gspread.service_account(filename = service_account_filepath)
# masterSheet = gc.open_by_key(spreadSheetKey)

def houseDivision(playerInfo):
    "Put players into their house group"
    # player = [ID, first, last, email, form, house, position, # of chasers]
    # use to track the position of the player in the sheet
    # so when update, they can be in the correct position
    position = 0
    # use to track how many other players are chasing the player
    # default value for everyone is 0 i.e. no one's chasing them
    chaser = 0
    kowhai = []
    matai = []
    rimu = []
    totara = []
    houseOrder = []
    for player in playerInfo:
        player.append(position)
        position += 1
        player.append(chaser)
        if player[5] == "Rimu":
            rimu.append(player)
        elif player[5] == "Matai":
            matai.append(player)
        elif player[5] == "Totara":
            totara.append(player)
        elif player[5] == "Kowhai":
            kowhai.append(player)
    #add the houses together, sort by the number of the players in the house
    allPlayer = [rimu, matai, kowhai, totara]
    allPlayer = sorted(allPlayer, key = len, reverse = True)
    # sort house name by the number of players in the house
    houseOrder = {
        "rimu": len(rimu),
        "matai": len(matai),
        "kowhai": len(kowhai),
        "totara": len(totara)
    }
    # sort the dictionary by the number of players, then return a list of house names
    houseOrder = [k for k, v in sorted(houseOrder.items(), key = itemgetter(1), reverse = True)]
    perfectGame = len(allPlayer[0]) < len(allPlayer[1] + allPlayer[2] + allPlayer[3])
    return allPlayer, houseOrder, perfectGame

def assignRunner(year):
    if year == 9:
        gc = gspread.service_account(filename=service_account_9_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        userList = sh.worksheet("YEAR9")
        numberOfPlayers = len(userList.col_values(2))

    elif year == 10:
        gc = gspread.service_account(filename=service_account_10_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        userList = sh.worksheet("YEAR10")
        numberOfPlayers = len(userList.col_values(2))

    elif year == 11:
        gc = gspread.service_account(filename=service_account_11_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        userList = sh.worksheet("YEAR11")
        numberOfPlayers = len(userList.col_values(2))

    elif year == 12:
        gc = gspread.service_account(filename=service_account_12_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        userList = sh.worksheet("YEAR12")
        numberOfPlayers = len(userList.col_values(2))

    elif year == 13:
        gc = gspread.service_account(filename=service_account_13_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        userList = sh.worksheet("YEAR13")  
        numberOfPlayers = len(userList.col_values(2))

    'assign runner to chaser'

    playerInfo = list(userList.get("A2:F{}".format(numberOfPlayers + 1)))
    allPlayer, houseOrder, perfectGame = houseDivision(playerInfo)
    houseNum = 0
    for house in allPlayer:
        # the name of the house is corresponding to the current house list
        houseName = houseOrder[houseNum]
        houseNum += 1
        # shuffle the players so the runner is randomized
        # player = [ID, first, last, email, form, house, position, # of chasers]
        random.shuffle(playerInfo)
        # sort by the descending order of number of people chasing them
        # so the last item of the array i.e. the player at the end
        # always have the least number of people chasing them
        playerInfo.sort(key = itemgetter(7), reverse = True)
        # the pointer for looking for targets always start from the end
        pointer = -1
        for player in house:
            # look for players not in their house
            while playerInfo[pointer][5] == houseName or playerInfo[pointer][-1] == player[0] :
                # move pointer to the left
                pointer -= 1
            # when we locate the pointer, we add 1 to the
            # number of chasers of the target, as there is 
            # a player chasing after them
            playerInfo[pointer][7] += 1
            # add the ID of the runner to the chasers list
            player.insert(8, playerInfo[pointer][0])
            playerInfo[pointer].append(player[6])
            # move the pointer left because the player 
            # the pointer was pointing to 
            # has been assigned as a runner
            pointer -= 1
    playerInfo.sort(key = itemgetter(6))
    for i in playerInfo:
        if i[7] != 1:
            perfectGame = False
            break
    userList.update("G2:G1000", [[i[8]] for i in playerInfo])
    return perfectGame

assignRunner(9)