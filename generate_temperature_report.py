#!/usr/bin/python3
# Generates an image based on today's temperature log data.
# Posts image to imgur and then posts to slack.
# Required args: 1 = imgur client ID (https://apidocs.imgur.com)
# Required args: 2 = slack incoming webhook url (https://api.slack.com/apps/APYNP95A6/incoming-webhooks)
# Required args: 3 = graph title

import requests
import matplotlib
import matplotlib.pyplot as plt
import csv
import os
import base64
import sys
import itertools
import numpy as np
from datetime import datetime

dir = os.path.dirname(os.path.realpath(__file__))
date = datetime.now().strftime('%d-%m-%Y')
timesWithTemps = []
with open(dir + '/data/' + date + '.csv') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    for row in csv_data:
        if len(row) == 2 and row[0] and row[1]:
            timesWithTemps.append((row[0], float(row[1])))

tempsByHours = {timeWithTemp[0].split(':')[0]: [] for timeWithTemp in timesWithTemps}
for timeWithTemp in timesWithTemps:
    hour = timeWithTemp[0].split(':')[0]
    tempsByHours[hour].append(timeWithTemp[1])

averageTempsByHour = {tempByHour: 0 for tempByHour in tempsByHours}
for hour, temps in tempsByHours.items():
    average = sum(temps) / len(temps)
    averageTempsByHour[hour] = average

temps = []
times = []
for hour, avgTemp in averageTempsByHour.items():
    times.append(hour + ':00')
    temps.append(avgTemp)

plt.figure(figsize=(len(temps) if len(temps) > 6 else 6, 6))
plt.plot(times, temps)
plt.axhspan(16, 24, facecolor='#2ca02c', alpha=0.1)
plt.title(sys.argv[3], loc='left', fontsize=14)
plt.title(date, loc='right', fontsize=14)
plt.ylabel('Temperature (°C)')
plt.xlabel('Time')
plt.grid(axis='y', linestyle='--')
plt.yticks([6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])
image_filename = date + '.png'
plt.tight_layout()
plt.savefig(image_filename)
# plt.show()

# Read image data and base64 encode image data
with open(image_filename, 'rb') as image_file:
    image_data = base64.b64encode(image_file.read())

# Send image to imgur
imgur_response = requests.post('https://api.imgur.com/3/image', data={'image': image_data}, headers={'Authorization': 'Client-ID ' + sys.argv[1]})
imgur_link = imgur_response.json()['data']['link']

# Send message to slack
data = {'attachments': [{'title': date, 'title_link': imgur_link, 'image_url': imgur_link}]}
slack_response = requests.post(sys.argv[2], json=data)