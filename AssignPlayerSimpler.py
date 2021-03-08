import gspread
import random
from collections import deque
from operator import itemgetter

gc = gspread.oauth()
masterSheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1-6fTPzP3Em48V1LU2sSgz23jEyG2TrKtTM1BW96nYUo/edit#gid=1234076362')
userList = masterSheet.get_worksheet(0)
playerTarget = masterSheet.get_worksheet(1)
#playerInfo = [house, status]
playerInfo = list(userList.get("F2:F206"))
kowhais = []
matais = []
rimus = []
totaras = []
notAlive = []

def assignId():
    "Assign Id to players and put alive players into their house, record dead's position"
    #shuffle the array and so the chaser id will be random in the next step
    random.shuffle(playerInfo)
    selfId = 101
    #playerInfo = [house, status, self ID, # of chasers]
    for player in playerInfo:
        player.append(selfId)
        selfId += 1
        player.append(0)
        # put players into respect house group for assigning runner later
        if player[0] == "Kowhai":
            kowhais.append(player)
        elif player[0] == "Matai":
            matais.append(player)
        elif player[0] == "Rimu":
            rimus.append(player)
        else:
            totaras.append(player)

def result():
    #create a deque for fast changing player pool values
    assignTarget(kowhais, "Kowhai")
    assignTarget(matais, "Matai")
    assignTarget(rimus, "Rimu")
    assignTarget(totaras, "Totara")
    re = kowhais + matais + rimus + totaras
    re.sort(key = itemgetter(1))
    for player in notAlive:
        player.append("N/A")
        re.insert(player[1] - 101, player)
    re.sort(key = itemgetter(0))
    return re

def assignTarget(house, houseName):
    'draw pkayers from the playerInfo of the house'
    #shuffles the rivalry list then sort by # of chaser descending order
    random.shuffle(playerInfo)
    playerInfo.sort(key = itemgetter(2), reverse = True)
    for i in playerInfo:
        print(i)
    print("\n")
    pointer = -1
    for player in house:
        while playerInfo[pointer][0] == houseName:
            pointer -= 1
        playerInfo[pointer][2] += 1
        player.append(playerInfo[pointer][1])
        pointer -= 1

def testClient():
    assignId()
    re = result()
    for i in re:
        print(i)
    userList.update("F2:I201")
testClient()