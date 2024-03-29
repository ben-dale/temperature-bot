#!/usr/bin/python3
# Generates an image based on today's temperature log data.
# Posts image to imgur and then posts to slack.
# Required args: 1 = Path to arduino (usually /dev/ttyACM0 or /dev/ttyACM1)

import os
import time
import sys
from serial import Serial
from datetime import datetime

working_dir = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(working_dir + '/data'):
    os.makedirs(working_dir + '/data')

ser = Serial(sys.argv[1], 9600)
temperature = ser.readline().decode('utf-8').strip(' \t\n\r')
date = datetime.now().strftime('%d-%m-%Y')
time = datetime.now().strftime('%H:%M')

csv_file = open(working_dir + '/data/' + date + '.csv', 'a+')
csv_file.write(time + ',' + temperature + '\n')
csv_file.close()