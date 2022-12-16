import usb.core
import usb.backend.libusb1


VENDOR_ID = "046D" # OnTrak Control Systems Inc. vendor ID
PRODUCT_ID = "C084" # ADU200 Device product name - change this to match your product

#VID_046D&PID_C084

device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
print(device)

ep = device[0].interfaces()[0].endpoints()[0]
print(ep)
i = device[0].interfaces()[0].bInterfaceNumber
device.reset()

if device.is_kernel_driver_active(i):
    device.detach_kernel_driver(i)

device.set_configuration()
eaddr = ep.bEndpointAddress
print(eaddr)

r= device.read(eaddr, 1024)

print(len(r))

# if device is None:
#     raise ValueError('ADU Device not found. Please ensure it is connected to the tablet.')
#     sys.exit(1)

# Claim interface 0 - this interface provides IN and OUT endpoints to write to and read from
usb.util.claim_interface(device, 0)