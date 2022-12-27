from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from .models import Robot, Part, Controls, Button, Slider, ValueDisplay
import pygame



# to capture video class
class Get_FS_Data(object):
    def __init__(self):
        pygame.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()
        self.buttons = {'axis1': 0., 'axis2': 0., 'axis3': 0., 'axis4': 0., 'axis5': 0., }

        self.axiss = [1000, 1000, 1000, 1000, 1000, 1000]

        self.Robot = Robot.objects.get(id=1)
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        pass

    def update(self):
        while True:
            # retrieve any events ...
            for event in pygame.event.get():  # Analog Sticks
                if event.type == pygame.JOYAXISMOTION:
                    self.axiss[event.axis] = round(500 * (event.value - 0.16) + 1500, 0)

            # to remove element 2 since axis numbers are 0 1 3 4
            self.buttons['axis1'], self.buttons['axis2'], self.buttons['axis3'], self.buttons['axis4'], self.buttons['axis5'], self.buttons[
                'axis6'] = [
                self.axiss[0], self.axiss[1], self.axiss[2], self.axiss[3], self.axiss[4], self.axiss[5]]

