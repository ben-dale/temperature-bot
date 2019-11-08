# Generates an image based on today's temperature log data.
# Posts image to imgur and then posts to slack.
# Required args: 1 = imgur client ID (https://apidocs.imgur.com)
# Required args: 2 = slack incoming webhook url (https://api.slack.com/apps/APYNP95A6/incoming-webhooks)

import requests
import matplotlib
import matplotlib.pyplot as plt
import csv
import os
import base64
import sys
import numpy as np
from datetime import datetime

date = datetime.now().strftime('%d-%m-%Y')
times = []
temps = []
with open(date + '.csv') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    for row in csv_data:
        if len(row) == 2:
            times.append(row[0])
            temps.append(round(float(row[1])))

plt.plot(times, temps)
plt.axhspan(16, 24, facecolor='#2ca02c', alpha=0.1)
plt.title(date)
plt.ylabel('Temperature (°C)')
plt.xlabel('Time')
plt.grid(axis='y', linestyle='--')
plt.yticks([6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])
image_filename = date + '.png'
plt.savefig(image_filename, dpi=200)
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