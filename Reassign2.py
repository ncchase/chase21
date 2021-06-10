from example_credentials import *
from operator import itemgetter
import gspread
from datetime import datetime
import random

gc = gspread.service_account(filename=service_account_9_filepath)
sh = gc.open_by_key(spreadsheet_key)

def getallrequests():
    allRequest = sh.worksheet('FORM_REASSIGN').get_all_records()
    y9, y10, y11, y12 = [], [], [], []
    for request in allRequest:
        request['Timestamp'] = datetime.strptime(request['Timestamp'], "%d/%m/%Y %H:%M:%S")
        # if request['Timestamp'].day == datetime.now().day:
        if True:
            if request['Your Year Level'] == 'Year 9':
                y9.append(request['Your Player ID'])
            elif request['Your Year Level'] == 'Year 10':
                y10.append(request['Your Player ID'])
            elif request['Your Year Level'] == 'Year 11':
                y11.append(request['Your Player ID'])
            elif request['Your Year Level'] == 'Year 12':
                y12.append(request['Your Player ID'])
    y9.sort()
    y10.sort()
    y11.sort()
    y12.sort()
    return {'year9': y9, 'year10': y10, 'year11': y11, 'year12': y12}

def getinfo(yearlevel = 9):
    info = sh.worksheet('YEAR{}'.format(yearlevel)).get_all_records()
    for i in range(len(info)):
        info[i]["index"] = i
    info.sort(key=itemgetter("ID"))
    return info

def reassign():
    requests = getallrequests()
    for year in range(9, 13):
        if not(requests['year{}'.format(year)]):
            continue
        info = getinfo(year)
        copyOfInfo = info.copy()
        notHere = []
        rowsNeedReassign = []
        j = 0
        for request in requests['year{}'.format(year)]:
            while info[j]["ID"] != request:
                j += 1
            notHere.append(info[j]["R's ID"])
            rowsNeedReassign.append(j)
            j += 1
        random.shuffle(copyOfInfo)
        copyOfInfo.sort(key=itemgetter("Chaser Count"))
        j = 0
        for request in rowsNeedReassign:
            while ((info[request]["House"] == copyOfInfo[j]["House"])
            or (copyOfInfo[j]['ID'] in notHere)):
                j += 1
            info[request]["R's ID"] = copyOfInfo[j]["ID"]
            info[request]["R's First Name"] = copyOfInfo[j]["First Name"]
            info[request]["R's Last Name"] = copyOfInfo[j]["Last Name"]
            info[request]["R's Form Class"] = copyOfInfo[j]["Form Class"]
            info[request]["R's House"] = copyOfInfo[j]["House"]
            j += 1
        info.sort(key = itemgetter("index"))
        info = [list(person.values())[:14] for person in info]
        sh.worksheet("YEAR{}".format(year)).update("A2:N1000", info)

reassign()