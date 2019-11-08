from serial import Serial
from datetime import datetime

temperature = Serial('/dev/ttyACM1', 9600, timeout=5).readline().decode("utf-8").strip(' \t\n\r')
date = datetime.now().strftime('%d-%m-%Y')
time = datetime.now().strftime('%H:%M')
csv_file = open(date + ".csv", "a+")
csv_file.write(time + "," + temperature + "\n")
csv_file.close()