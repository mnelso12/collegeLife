#!/usr/bin
# because too lazy to remember to check the schedule and email everyone by hand

import re
import csv
import sys
import os
import subprocess
import datetime
import time

# dictionary of Name(no spaces) : netId
dict = {
		'Alex Viegut':'aviegut',
		'Nicole Schneider':'nschnei1',
		'Kathy Casillas':'kcasilla',
		'Jackie O\'Brien':'jobrie21',
		'Caterina Brewer':'cbrewer',
		'Alyssa Carroll':'acarrol3',
		'Amanda Addiego':'aaddiego',
		'Helen Streff':'hstreff',
		'Jane Bonfiglio':'jbonfigl',
		'Katie O\'Sullivan':'kosulli6',
		'Emily Labbe':'elabbe',
		'Madelyn Nelson':'mnelso12',
		'Kelly Koerwer':'kkoerwer',
		'Jessica Linton':'jlinton',
		'Lily Crawford':'lcrawfo3',
		'Kathleen Ryan':'kryan16',
		'Nhu-y Nguyen':'nnguyen7',
		'Maggie Dever':'mdever',
		'Casey Gelchion':'cgelchio',
		'Madeline Lewis':'mlewis13',
		'Luisa Andrade':'landrade',
		'Alicia Cristoforo':'acristof',
		'Michaela Evanich':'mevanich',
		'Paige Smith':'psmith27',
		'Louise Gregory':'lgregor2',
		'Alice Felker':'afelker',
		'Ale Orellana Muniz':'morellan',
		'Kathryn O\'Callaghan':'Kathryn.O\'Callaghan.12',
		'Mary Elizabeth Coleman':'mcolema9',
		'Lauren Lemaignen':'llemaign',
		'Jane Kassabian':'jkassabi',
		'Abbey Epplen':'aepplen'
		}

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

# TODO uncomment this
#todaysDate = "12-11-16"

# get the line with this date if there is one
#tempStr1 = "/"
#tempStr2 = "/p"
#sedInput = []
#sedInput.append(tempStr1)
#sedInput.append(todaysDate)
#sedInput.append(tempStr2)
#sedIn = ''.join(sedInput)

#print 'sedIn', sedIn

f = 'fall2016.csv'
#output = subprocess.check_output(["sed", "-n", sedIn, f])

output = [] 

with open('fall2016.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		if row[0] == todaysDate:
			print 'THERE IS MASS TODAY!'
			output = row

print output

#lineAsList = re.sub("[^\w]", " ", output).split()
#del lineAsList[0:3] # ignore date, don't need that anymore

#si = iter(lineAsList)
#namesList = [c+next(si, '') for c in si]

namesList = output[1:]

# make list of emails
listOfEmails = ['mnelso12@nd.edu']
listOfEmails.append('kkoerwer@nd.edu')
listOfEmails.append('aviegut@nd.edu')
for name in namesList[0:6:]: 
    listOfEmails.append(dict[name]+"@nd.edu")

emailsWithCommas = ",".join(listOfEmails)
print emailsWithCommas


#echo "dont forget about mass" | mail -s "Badin Mass Reminder" mnelso12@nd.edu,rbusk@nd.edu
massScheduleStr = 'Sacristan: '+ namesList[0]+'\nReader 1: '+ namesList[1] +'\nReader 2: '+ namesList [2] + '\nEM: '+ namesList[3] +', '+namesList[4]+', '+namesList[5]

echoStr = 'echo "Hello Badin Ladies! \n\nYou are on this week\'s mass schedule!\n\n'+massScheduleStr+'\n\nHere\'s the schedule:\n https://docs.google.com/a/nd.edu/spreadsheets/d/1UdlKC68wV_oJ4MtF1GchrJgPnGd1JZO-_ovG8yCjALE/edit?usp=sharing\n\nSee you there! \n<3 Liturgical Commission" |'

callStr = echoStr+' mail -s "Badin Mass Reminder" '+emailsWithCommas
subprocess.call(callStr, shell = True)
