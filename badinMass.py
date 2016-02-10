#!/usr/bin
# because too lazy to remember to check the schedule and email everyone by hand

import re
import sys
import os
import subprocess
import datetime
import time

# dictionary of Name(no spaces) : netId
dict ={'KellyKoerwer':'kkoerwer','MeghanGrojean':'mgrojean','LizzieCannon':'ecannon1','MollyClark':'mclark24','JuliaLe':'jle1','KellyHeiniger':'kheinige', 'NicoleHanda':'nhanda','ZosiaZdanowicz':'zzdanowi','MaggieFitzGerald':'mfitzg13','LaneNicolay':'lnicolay','AudreyMeier':'ameier2', 'JessicaDeutsch':'jdeutsch'}

# find todays date
today = datetime.datetime.today()

month = today.month
day = today.day
year = today.year

date = []
date.append(str(month))
date.append(str(day))
date.append(str(year))

s = "-"
print s.join(date)
todaysDate = s.join(date)

# get the line with this date if there is one
tempStr1 = "/"
tempStr2 = "/p"
sedInput = []
sedInput.append(tempStr1)
sedInput.append(todaysDate)
sedInput.append(tempStr2)
sedIn = ''.join(sedInput)

f = 'sp16.txt'
output = subprocess.check_output(["sed", "-n", sedIn, f])

lineAsList = re.sub("[^\w]", " ", output).split()
del lineAsList[0:3] # ignore date, don't need that anymore

si = iter(lineAsList)
namesList = [c+next(si, '') for c in si]

# make list of emails
listOfEmails = ['mnelso12@nd.edu']
listOfEmails.append('kkoerwer@nd.edu')
for name in namesList[0:6:]: 
    listOfEmails.append(dict[name]+"@nd.edu")

emailsWithCommas = ",".join(listOfEmails)
print emailsWithCommas

#echo "dont forget about mass" | mail -s "Badin Mass Reminder" mnelso12@nd.edu,rbusk@nd.edu
massScheduleStr = 'Sacristan: '+lineAsList[0]+' '+lineAsList[1]+'\nReader 1: '+lineAsList[2]+' '+lineAsList[3]+'\nReader 2: '+lineAsList[4]+' '+lineAsList[5]+'\nEM: '+lineAsList[6]+' '+lineAsList[7]+', '+lineAsList[8]+' '+lineAsList[9]+', '+lineAsList[10]+' '+lineAsList[11]

echoStr = 'echo "Hello Badin Ladies! \n\nYou are on this week\'s mass schedule!\n\n'+massScheduleStr+'\n\nHere\'s the schedule:\nhttps://docs.google.com/spreadsheets/d/1Sy7IAzSSB1uKPIT_dH9taEBlc-srTfO-XG7kQFQg3i8/edit#gid=0\n\nSee you there! \n<3 Liturgical Commission" |'

callStr = echoStr+' mail -s "Badin Mass Reminder" '+emailsWithCommas
subprocess.call(callStr, shell = True)
