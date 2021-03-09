import gspread
import random
from collections import deque
from operator import itemgetter
from credentials import *

gc = gspread.service_account(filename=service_account_filepath)
masterSheet = gc.open_by_key(year9_spreadsheet_key)

workSheetName = ""
numberOfPlayers = 0

# Example for getting worksheet by name:
# worksheet = masterSheet.worksheet("INSERT_WORKSHEET_NAME")
userList = masterSheet.worksheet(workSheetName)

playerInfo = list(userList.get("F2:F{}".format(numberOfPlayers + 1)))
kowhai13 = []
matai13 = []
rimu13 = []
totara13 = []
kowhai12, matai12, rimu12, totara12 = [], [], [], []
kowhai11, matai11, rimu11, totara11 = [], [], [], []
kowhai10, matai10, rimu10, totara10 = [], [], [], []
kowhai9, matai9, rimu9, totara9 = [], [], [], []


def houseDivision():
    "Put players into their house group"
    for player in playerInfo:
        if player[]


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