import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api
import sys
import time


class screen:
    def __init__(self,region=None):
        self.hwin = win32gui.GetDesktopWindow()

        if region:
                self.left,self.top,x2,y2 = region
                self.width = x2 - self.left + 1
                self.height = y2 - self.top + 1
        else:
            self.width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
            self.height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
            self.left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
            self.top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

        self.hwindc = win32gui.GetWindowDC(self.hwin)
        self.srcdc = win32ui.CreateDCFromHandle(self.hwindc)
        self.memdc = self.srcdc.CreateCompatibleDC()


    def grab_screen(self):

        
        self.bmp = win32ui.CreateBitmap()
        self.bmp.CreateCompatibleBitmap(self.srcdc, self.width, self.height)
        self.memdc.SelectObject(self.bmp)
        self.memdc.BitBlt((0, 0), (self.width, self.height), self.srcdc, (self.left, self.top), win32con.SRCCOPY)
        
        signedIntsArray = self.bmp.GetBitmapBits(True)
        # img = np.fromstring(signedIntsArray, dtype='uint8')
        # img.shape = (self.height,self.width,4)
        #signedIntsArray=cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        

        return signedIntsArray

    def close(self):
        self.srcdc.DeleteDC()
        self.memdc.DeleteDC()
        win32gui.ReleaseDC(self.hwin, self.hwindc)
        win32gui.DeleteObject(self.bmp.GetHandle())


if __name__ == "__main__":
    clas=screen()
    t=time.time()
    for i in range(120):
        data=clas.grab_screen()
        img = np.frombuffer(data, dtype='uint8')
        img.shape = (clas.height,clas.width,4)
    print(sys.getsizeof(data))
    tt=time.time()
    print(tt-t)
    print((tt-t)/120)
    cv2.imshow('55',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()