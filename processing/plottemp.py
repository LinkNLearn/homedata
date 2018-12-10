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
print('the room key is: ')
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

# plot on Matlab
fig, ax = plt.subplots()
ax.plot(timestamp, temperature)
plt.show()
