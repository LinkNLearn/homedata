import numpy as np
import time
import matplotlib
import json as json
import datetime # https://docs.python.org/3.3/library/datetime.html
import matplotlib.pyplot as plt
import numpy as np


path = 'room_temp.json' # path to our document containing json
thing = open(path) # put the json document into thing
data = json.load(thing) # use json.load to parse json into a list

keys = data[0].keys()
tempkey = list(keys)[2]
roomkey = list(keys)[3]
timekey = list(keys)[4]
print('the time key is: ')
print(timekey)
print('the temp key is: ')
print(tempkey)
print('the room id key is: ')
print(roomkey)

# Using Regular List and For Loop, then Put That List Into Array
print('Loading timestamps...')
N=len(data)
timestamp = []
for i in range(N):
    # extract date time at i
    A = data[i]['date_time']
    # setup  date_time as a unix timestamp so that it works as a float
    timeI = time.mktime(datetime.datetime.strptime(A, "%Y-%m-%d %H:%M:%S").timetuple())
    # put unix timestamp into list to be appended
    timeIlist = [time.mktime(datetime.datetime.strptime(A, "%Y-%m-%d %H:%M:%S").timetuple())]
    # append this value into timestamp
    timestamp.append(timeIlist)
print('...timestamps loaded.')

print('Loading temperatures...')
temperature = []
for i in range(N):
    # extract temperature at i
    A = data[i]['temperature']
    # append this value into temperature
    temperature.append(A)
print('...temperatures loaded.')

# Locate timestamps for each room_id
room0 = []
room1 = []
for i in range(N):
    # extract id value
    A = data[i]['room_id']
    # if room_id = 0, then put marker number in room0 list
    if A == 0:
        room0.append(i)
    # if room_id = 1, then put marker number in room1 list
    else:
        room1.append(i)

# Extract temperatures and timestamps from room0
temperature0 = [temperature[i] for i in room0]
timestamp0 = [timestamp[i] for i in room0]
print('temperature and timestamp from room0 sorted')

# Extract temperatures and timestamps from room1
temperature1 = [temperature[i] for i in room1]
timestamp1 = [timestamp[i] for i in room1]
print('temperature and timestamp from room1 sorted')


# plot on Matlab
fig, ax = plt.subplots()
ax.plot(timestamp0, temperature0)
ax.plot(timestamp1, temperature1)
plt.show()


# Cleaning Rules - Creating Temperature Rails, Extracting Indicies
HighTemp = 100
LowTemp = 30
validtemproom0 = []
validtimeroom0 = []

# for range of temperature0 - our new matrix of room0 temps
for i in range(len(temperature0)):
    if temperature0[i] < HighTemp and temperature0[i] > LowTemp:
        validtemproom0.append(temperature0[i])
        validtimeroom0.append(timestamp0[i])

print('room0 temp data cleaned')
print('room0 time data cleaned')


validtemproom1 = []
validtimeroom1 = []
# for range of temperature0 - our new matrix of room0 temps
for i in range(len(temperature1)):
    if temperature1[i] < HighTemp and temperature1[i] > LowTemp:
        validtemproom1.append(temperature1[i])
        validtimeroom1.append(timestamp1[i])


fig, ax = plt.subplots()
ax.plot(validtimeroom0, validtemproom0)
ax.plot(validtimeroom1, validtemproom1)
plt.show()
