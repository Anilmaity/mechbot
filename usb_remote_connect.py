# import usb.core
# import usb.backend.libusb1
#
#
# VENDOR_ID = "2341" # OnTrak Control Systems Inc. vendor ID
# PRODUCT_ID = "0043"  # ADU200 Device product name - change this to match your product
#
# #VID_046D&PID_C084
#
# device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
# print(device)
#
# ep = device[0].interfaces()[0].endpoints()[0]
# print(ep)
# i = device[0].interfaces()[0].bInterfaceNumber
# device.reset()
#
# if device.is_kernel_driver_active(i):
#     device.detach_kernel_driver(i)
#
# device.set_configuration()
# eaddr = ep.bEndpointAddress
# print(eaddr)
#
# r= device.read(eaddr, 1024)
#
# print(len(r))
#
# # if device is None:
# #     raise ValueError('ADU Device not found. Please ensure it is connected to the tablet.')
# #     sys.exit(1)
#
# # Claim interface 0 - this interface provides IN and OUT endpoints to write to and read from
# usb.util.claim_interface(device, 0)
#
#
# #
# # import pyvjoy
# #
# # #Pythonic API, item-at-a-time
# #
# # j = pyvjoy.VJoyDevice(1)
# #
# # #turn button number 15 on
# # j.set_button(15,1)
# #
# # #Notice the args are (buttonID,state) whereas vJoy's native API is the other way around.
# #
# #
# # #turn button 15 off again
# # j.set_button(15,0)
# #
# # #Set X axis to fully left
# # j.set_axis(pyvjoy.HID_USAGE_X, 0x1)
# #
# # #Set X axis to fully right
# # j.set_axis(pyvjoy.HID_USAGE_X, 0x8000)
# #
# # #Also implemented:
# #
# # j.reset()
# # j.reset_buttons()
# # j.reset_povs()

import serial
import time

ser = serial.Serial('COM3', 115200, timeout=1)
ser.flush()
# 8N1
# Data frame
# 32 bytes
# Structure
# Example set of 32 bytes
# 20 40 DB 5 DC 5 54 5 DC 5 E8 3 D0 7 D2 5 E8 3 DC 5 DC 5 DC 5 DC 5 DC 5 DC 5 DA F3
# Section
# Protocol length	Command code	CH1	CH2	CH3	...	CH14	Checksum
# 0x20	0x40	0xDB 0x05	0xDC 0x05	0x54 0x05	...	0xDC 0x05	0xDA 0xF3
# Little Endian
# ibus data	HEX	DEC
# CH1	0x05DB	1499
# CH2	0x05DC	1500
# CH3	0x0554	1364
# ...	...	...
# CH14	0x05DC	1500
# Checksum	0xF3DA
# Checksum calculation
# 0xFFFF - (sum of previous 30 bytes)
online = False
while True:
    if ser.in_waiting > 0:
        st = time.time()
        hex = ser.read_until(b'@').strip(b'@')
        #print(hex)
        dt = time.time() - st

        # print(start, cmd)
        hexchecksum = hex[len(hex) - 3:len(hex)]
        #print(hexchecksum)
        # print(checksum)
        checksum = int.from_bytes(hexchecksum, byteorder='little')

        data = []
        cal_checksum = 0
        for i in range(0, len(hex) -3, 2):
            val = int.from_bytes(hex[i:i + 2], byteorder='little')
            data.append(val)

        cal_checksum =  sum(data)



            # calculate checksum

        print( data, int(dt*1000), cal_checksum,)

#  Data convertion


# hex = b'\x20\x40\xDB\x05\xDC\x05\x54\x05\xDC\x05\xE8\x03\xD0\x07\xD2\x05\xE8\x03\xDC\x05\xDC\x05\xDC\x05\xDC\x05\xDC\x05\xDC\x05\xDA\xF3'
# # split
# start = int.from_bytes(hex[0:1], byteorder='little')
# cmd = int.from_bytes(hex[1:2], byteorder='little')
# # print(start, cmd)
# checksum = hex[-2:]
# # print(checksum)
# checksum = int.from_bytes(checksum, byteorder='little')
#
# data = []
# for i in range(2, len(hex)-3, 2):
#
#     val = int.from_bytes(hex[i:i+2], byteorder='little')
#     data.append(val)
#
# print(start, cmd, checksum, data)
