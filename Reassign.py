from operator import itemgetter
import gspread
from datetime import date, datetime
import copy
import random
import heapq
from example_credentials import *

gc = gspread.service_account(filename=service_account_9_filepath)
sh = gc.open_by_key(spreadsheet_key)

def get_requests_from_sheet():
    userlist = sh.worksheet('FORM_REASSIGN').get('A2:D1000')
    year9 = []
    year10 = []
    year11 = []
    year12 = []
    # put players into year levels to handle separately
    for player in userlist:
        # format string into datetime object
        player[0] = datetime.strptime(player[0], "%d/%m/%Y %H:%M:%S")
        # date validation
        if player[0].day == datetime.now().day:
            if player[3] == 'Year 9':
                print('Year 9')
                year9.append(player)
            elif player[3] == 'Year 10':
                year10.append(player)
            elif player[3] == 'Year 11':
                year11.append(player)
            else:
                year12.append(player)
                print(year12)
    return (year9.sort(key = itemgetter(2)), 
            year10.sort(key = itemgetter(2)), 
            year11.sort(key = itemgetter(2)),
            year12.sort(key = itemgetter(2)))

def get_year_level(year_level=9):
    info = sh.worksheet('YEAR{}'.format(year_level))
    info = list(info.get('A2:L{}'.format(len(info.col_values(2)) + 1)))
    return info.sort(key = itemgetter(0))

def reassign():
    all = get_requests_from_sheet()
    print(all)
    # different year levels
    for year in range(9, len(all) + 9):
        year_level = get_year_level(year)
        year_level_copy = copy.deepcopy(year_level)
        info = sh.worksheet('YEAR9')
        not_here = []
        rows_need_reassign = []
        # j is the index of the chasers who need a new runner
        j = 0
        # loop through requests
        # record players who is not here
        for request in all[year - 9]:
            while year_level[j][0] != request[2]:
                j += 1
            not_here.append(year_level[j][6])
            rows_need_reassign.append(j)
            j += 1
        random.shuffle(year_level_copy)
        # sort by number of chasers to ensure fair games
        year_level_copy.sort(key = itemgetter(13), reverse = True)
        heapq.heapify(year_level_copy)
        # assign 
        for i in rows_need_reassign:
            j = -1
            while (year_level[i][5] == year_level_copy[j][5] # in the same house
            or year_level_copy[j][0] in not_here): # or not not here
                j -= 1
            year_level[i][6] = year_level_copy.pop(j)
            year_level[i][12] += 1
            j -= 1
        info.update('G2:H1000', [i[6] for i in year_level], value_input_option="USER_ENTERED")

reassign()