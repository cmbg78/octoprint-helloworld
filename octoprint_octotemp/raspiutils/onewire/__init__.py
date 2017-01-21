import subprocess as sub
import sys
import os

# global inits
devicePath = "/sys/bus/w1/devices/"
if sys.platform.startswith('linux'):
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

def getDeviceList():
    try:
        devices = os.listdir(devicePath)
    except:
        devices = "An error was encountered - do you have OneWire probes attached?  error: %s" % sys.exc_info()[0]
    return devices

def readProbeRaw(device):
    deviceFile = devicePath + device + "/w1_slave"
    f = open(deviceFile, "r")
    raw = f.readlines()
    f.close
    return raw

def readRawTemp(raw):
    return raw[1].strip()[raw[1].find("t=")+2:]

def deviceReadSuccess(raw):
    if raw[0].strip()[-3:] == "YES":
        if raw[1].find("t=") != -1:
            return True
        else:
            return False
    else:
        return False

def readTempC(device):
    raw = readProbeRaw(device)
    if deviceReadSuccess(raw):
        rawTemp = readRawTemp(raw)
        return float(rawTemp) / 1000.0

def readTempF(device):
    temp_c = readTempC(device)
    return temp_c * 9.0 / 5.0 + 32.0
