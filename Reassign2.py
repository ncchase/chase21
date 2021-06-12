from example_credentials import *
from operator import itemgetter
import gspread
from datetime import datetime
import random

# connect to spread sheet
gc = gspread.service_account(filename=service_account_9_filepath)
sh = gc.open_by_key(spreadsheet_key)

def getallrequests():
    "to get all reasign request from the FORM_REASSIGN sheet"
    allRequest = sh.worksheet('FORM_REASSIGN').get_all_records()
    y9, y10, y11, y12 = [], [], [], []
    for request in allRequest:
        # date validation
        request['Timestamp'] = datetime.strptime(request['Timestamp'], "%d/%m/%Y %H:%M:%S")
        if request['Timestamp'].day == datetime.now().day:
            # handle requests by year levels
            # only record their player IDs
            if request['Your Year Level'] == 'Year 9':
                y9.append(request['Your Player ID'])
            elif request['Your Year Level'] == 'Year 10':
                y10.append(request['Your Player ID'])
            elif request['Your Year Level'] == 'Year 11':
                y11.append(request['Your Player ID'])
            elif request['Your Year Level'] == 'Year 12':
                y12.append(request['Your Player ID'])
    # sort the player IDs
    y9.sort()
    y10.sort()
    y11.sort()
    y12.sort()
    return {'year9': y9, 'year10': y10, 'year11': y11, 'year12': y12}

def getinfo(yearlevel = 9):
    "get all of chaser-runner information of a year level"
    info = sh.worksheet('YEAR{}'.format(yearlevel)).get_all_records()
    # keep track of index
    # when update the spread sheet everything will be in original order
    for i in range(len(info)):
        info[i]["index"] = i
    info.sort(key=itemgetter("ID"))
    return info

def reassign():
    requests = getallrequests()
    # handle different year levels
    for year in range(9, 13):
        # if no request from a year level, skip
        if not(requests['year{}'.format(year)]):
            continue
        info = getinfo(year)
        copyOfInfo = info.copy()
        # new lists to keep track of the index of the people 
        # in the "info" list that need a new runner
        # keep track of people who are not here
        notHere = []
        rowsNeedReassign = []
        # just a pointer for looping through the lists
        j = 0
        for request in requests['year{}'.format(year)]:
            # if a person doesn't have a request, skip
            # else, add their respective runner to the "nothere" list
            # add their index to the "rowsneedreassign" list
            while info[j]["ID"] != request:
                j += 1
            notHere.append(info[j]["R's ID"])
            rowsNeedReassign.append(j)
            j += 1
        # randomized the list, then sort by number of chasers to ensure fair game
        random.shuffle(copyOfInfo)
        copyOfInfo.sort(key=itemgetter("Chaser Count"))
        # pointer reused
        j = 0
        for request in rowsNeedReassign:
            # if in the same house or the person not here, skip
            # else renew the information of the runner of the chaser
            while ((info[request]["House"] == copyOfInfo[j]["House"])
            or (copyOfInfo[j]['ID'] in notHere)):
                j += 1
            info[request]["R's ID"] = copyOfInfo[j]["ID"]
            info[request]["R's First Name"] = copyOfInfo[j]["First Name"]
            info[request]["R's Last Name"] = copyOfInfo[j]["Last Name"]
            info[request]["R's Form Class"] = copyOfInfo[j]["Form Class"]
            info[request]["R's House"] = copyOfInfo[j]["House"]
            j += 1
        # sort by index to go back to the original order
        info.sort(key = itemgetter("index"))
        info = [list(person.values())[:14] for person in info]
        sh.worksheet("YEAR{}".format(year)).update("A2:N1000", info)

reassign()