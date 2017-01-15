import subprocess as sub
import sys

def testPrint():
    try:
        wires = sub.check_output(["ls", "/sys/bus/w1/devices"])
        wires = wires.split('\n')
    except:
        wires = "An error was encountered - do you have OneWire probes attached?  error: %s" % sys.exc_info()[0]    
    return wires