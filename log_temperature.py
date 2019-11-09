#!/usr/bin/python3

import os
import time
import sys
from serial import Serial
from datetime import datetime

working_dir = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(working_dir + '/data'):
    os.makedirs(working_dir + '/data')

ser = Serial(sys.argv[1], 9600, timeout=5)
temperature = ser.readline().decode('utf-8').strip(' \t\n\r')
date = datetime.now().strftime('%d-%m-%Y')
time = datetime.now().strftime('%H:%M')

csv_file = open(working_dir + '/data/' + date + '.csv', 'a+')
csv_file.write(time + ',' + temperature + '\n')
csv_file.close()