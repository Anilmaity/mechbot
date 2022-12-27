import threading
import pygame

#to capture video class
class Get_FS_Data(object):
    def __init__(self):

        self.controller = pygame.joystick.Joystick(0)

        self.controller.init()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        pass

    def update(self):
        while True:
            self.ch1 = self.controller.get_axis(0)
            self.ch2 = self.controller.get_axis(1)
            self.ch3 = self.controller.get_axis(2)
            self.ch4 = self.controller.get_axis(3)
            self.ch5 = self.controller.get_axis(4)
            self.ch6 = self.controller.get_axis(5)
            self.data = {"ch1": self.ch1, "ch2": self.ch2, "ch3": self.ch3, "ch4": self.ch4, "ch5": self.ch5,
                         "ch6": self.ch6}
            print(self.data)


FS = Get_FS_Data()
