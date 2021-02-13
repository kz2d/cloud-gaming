import sys
sys.path.insert(0,'C:/Users/37525/vs_project/python_project-master/cloud gaming/serverside/screenLoader')
import newGrabScreen
import ImageGrab
import cv2
import time


class ScreenRecorderInterface:

    def __init__(self,reg=None):
        self.grabscreen=ImageGrab.screen(reg)
        self.height=self.grabscreen.height
        self.width=self.grabscreen.width

    def takeScreen(self):
        screen=self.grabscreen.grab_screen()

        return screen

    def close(self):
        self.grabscreen.close()





# class ScreenRecorderInterface:

#     def __init__(self,reg=None):
#         self.grabscreen=newGrabScreen.screen(reg)
#         self.height=self.grabscreen.height
#         self.width=self.grabscreen.width

#     def takeScreen(self):
#         screen=self.grabscreen.grab_screen()

#         return screen

#     def close(self):
#         self.grabscreen.close()

