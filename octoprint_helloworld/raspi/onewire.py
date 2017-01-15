import subprocess as sub
import sys

def getDeviceList():
    try:
        devices = sub.check_output(["ls", "/sys/bus/w1/devices"])
        devices = wires.split('\n')
    except:
        devices = "An error was encountered - do you have OneWire probes attached?  error: %s" % sys.exc_info()[0]    
    return devices