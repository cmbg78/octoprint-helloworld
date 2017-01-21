import subprocess as sub
import sys
import os

def getDeviceList():
    try:
        devices = os.listdir("/sys/bus/w1/devices")
    except:
        devices = "An error was encountered - do you have OneWire probes attached?  error: %s" % sys.exc_info()[0]    
    return devices