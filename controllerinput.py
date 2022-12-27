import pygame
from time import sleep

pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()
buttons = {'axis1': 0., 'axis2': 0., 'axis3': 0., 'axis4': 0., 'axis5': 0.,}

axiss = [1000, 1000, 1000, 1000, 1000, 1000]


def getJS(name=''):
    global buttons
    # retrieve any events ...
    for event in pygame.event.get():  # Analog Sticks
        if event.type == pygame.JOYAXISMOTION:
            axiss[event.axis] = round(500*(event.value-0.16)+1500, 0)

    # to remove element 2 since axis numbers are 0 1 3 4
    buttons['axis1'], buttons['axis2'], buttons['axis3'], buttons['axis4'], buttons['axis5'], buttons['axis6'] = [
        axiss[0], axiss[1], axiss[2], axiss[3], axiss[4], axiss[5]]
    if name == '':
        return buttons
    else:
        return buttons[name]


def main():
    print(getJS())  # To get all values


#     print(getJS('share')) # To get a single value
#     sleep(0.05)


if __name__ == '__main__':
    while True:
        main()

