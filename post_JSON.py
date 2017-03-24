# !/usr/bin/python
# get data and put it to api gateway
# use curl command
# Created by Chris Hsu
# Modified by Dan Lwo

import json
import sys
import time
import datetime
from datetime import datetime, timedelta
import Adafruit_DHT
import socket
import subprocess

# Type of sensor, could be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT22

# Example of sensor connected to Raspberry Pi pin 23
DHT_PIN  = 22

# Attempt to get sensor reading.
humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
# Skip to the next reading if failed to get a valid measurement.
# This might happen if the CPU were under a lot of loading and the sensor
# can't be reliably read (timing is critical to read the sensor).
if humidity is None or temp is None:
        time.sleep(2)
        humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)

print "Temperature:",temp,"C"
print "Humidity:",humidity,"%"

# Get datetime.
DATE = datetime.strftime(datetime.now(), '%Y%b%d-%H:%M:%S')
print(DATE, temp, humidity)

# Get IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
Ip = (s.getsockname()[0])
print "ip address is :",Ip
s.close()

# Change flot to dem.
TempIn ="%.4f" %temp
HumiIn ="%.4f" %humidity
#covert to json
json_map = {}
json_map["DeviceName"] = "YourDeviceName"
json_map["TempIn"] = TempIn
json_map["HumiIn"] = HumiIn
json_map["Moment"] = DATE
json_map["Ip"] = Ip

#print json_map
result = json.dumps(json_map)
print "JSON here"
print result

print "\nstart use curl\n"
subprocess.call(["curl", "-H", "Content-Type:application/json", "-X", "POST", "-d", result, "http://InvokeURLofYourAPIgatewayDeployStage"], stdout=True)
print "upload DONE"
