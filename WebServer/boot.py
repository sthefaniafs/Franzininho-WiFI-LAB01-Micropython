# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

try:
  import usocket as socket
except:
  import socket

import network
from machine import Pin
import dht

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Cabo12'
password = '96851598'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# might already be connected somehow.
if wlan.isconnected() == False:
    wlan.connect(ssid, password)

# Wait for connection.
while wlan.isconnected() == False:
    pass

print('connected!')

sensor= dht.DHT11(Pin(15))