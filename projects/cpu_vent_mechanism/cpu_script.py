import time

import clr #package pythonnet, not clr
import os
import sys

# setup serial communication with arduino
import serial
import serial.tools.list_ports
import time
import datetime

# all ports
ports = serial.tools.list_ports.comports()
arduinoport = ""

import clr #package pythonnet, not clr
import os
import sys
version = "1.0.0"
# setup serial communication with arduino
import serial
import serial.tools.list_ports
import time
import datetime


print("This software is designed by Mechual Pvt Ltd")
print("Software version: ", version)
time.sleep(2)



# all ports
ports = serial.tools.list_ports.comports()
arduinoport = ""
for port, desc, hwid in sorted(ports):
    if "Arduino" in desc or "Silicon Labs" in desc:
        # print("{}: {} [{}]".format(port, desc, hwid))
        arduinoport  = port

if arduinoport == "":
    print("No Arduino Device Found")
    time.sleep(5)
    sys.exit(0)

# arduino port
serial = serial.Serial(arduinoport, 115200, timeout=1)



currentdir = os.path.dirname(os.path.realpath(__file__))

file = os.path.join(currentdir, 'OpenHardwareMonitorLib.dll')
clr.AddReference(file)
def initialize_openhardwaremonitor():
    from OpenHardwareMonitor import Hardware

    handle = Hardware.Computer()
    handle.MainboardEnabled = True
    handle.CPUEnabled = True
    handle.RAMEnabled = True
    handle.GPUEnabled = True
    handle.HDDEnabled = True
    handle.Open()
    return handle

def fetch_stats(handle):
    data = {}
    for i in handle.Hardware:
        i.Update()
        for sensor in i.Sensors:
            if sensor.Value is not None:
                if(sensor.Name == 'CPU Total'):
                    hardwaredata = {
                        "CPU":
                            {
                                'usage': sensor.Value,
                            }
                    }
                    data.update(hardwaredata)
                if(sensor.Name == 'Used Memory'):
                    hardwaredata = {
                        "RAM":
                            {
                                'usage': sensor.Value,
                            }
                    }
                    data.update(hardwaredata)
                if sensor.Name == 'GPU Core' and str(sensor.SensorType) == 'Temperature':
                    # print(subsensor.Value, subsensor.SensorType)
                    hardwaredata = {
                        "GPU":
                            {
                                'temperature': sensor.Value,

                            }
                    }
                    data.update(hardwaredata)


    return data







if __name__ == "__main__":
    print("OpenHardwareMonitor:")
    HardwareHandle = initialize_openhardwaremonitor()
    # hardwaredata =fetch_stats(HardwareHandle)
    # print(hardwaredata)
    # print(hardwaredata["CPU"]["load"])
    # print(hardwaredata["GPU"]["temperature"])
    while True:
        hardwaredata = fetch_stats(HardwareHandle)
        # print(hardwaredata)
        hardware = "CPU"
        value = hardwaredata[hardware]["usage"]
        # map value 0-100 to 40-100
        value = (value - 0) * (100 - 40) / (100 - 0) + 40

        data = "@##"+str(value)+"$"+str(hardware) + "##@"
        # send data to arduino
        serial.write(data.encode())
        # read data from arduino
        recieveddata = serial.readline().decode('ascii')
        if recieveddata != "":
            print("recieved data " , recieveddata)
