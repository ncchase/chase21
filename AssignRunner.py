import gspread
import random
from collections import deque
from operator import itemgetter
from example_credentials import *

gc = gspread.service_account(filename = service_account_filepath)
masterSheet = gc.open_by_key(spreadSheetKey)

workSheetName = "YEAR9"
numberOfPlayers = 80

# Example for getting worksheet by name:
# worksheet = masterSheet.worksheet("INSERT_WORKSHEET_NAME")
userList = masterSheet.worksheet(workSheetName)

playerInfo = list(userList.get("A2:F{}".format(numberOfPlayers + 1)))
kowhai = []
matai = []
rimu = []
totara = []
allPlayer = []
houseOrder = []

def houseDivision():
    "Put players into their house group"
    # player = [ID, first, last, email, form, house, position, # of chasers]
    # use to track the position of the player in the sheet
    # so when update, they can be in the correct position
    position = 0
    # use to track how many other players are chasing the player
    # default value for everyone is 0 i.e. no one's chasing them
    chaser = 0
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
    print(houseOrder)
    return allPlayer, houseOrder


def assignRunner():
    'draw pkayers from the playerInfo of the house'
    allPlayer, houseOrder = houseDivision()
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
            player.append(playerInfo[pointer][0])
            # move the pointer left because the player 
            # the pointer was pointing to 
            # has been assigned as a runner
            pointer -= 1
    playerInfo.sort(key = itemgetter(6))
    result = [i[0:5] + [i[8]] for i in playerInfo]
    for i in result:
        print(i)
assignRunner()