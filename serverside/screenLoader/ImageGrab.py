import cv2
import numpy as numpy
import d3dshot
import win32gui, win32ui, win32con, win32api
import sys
import time
import pickle


class screen:
    def __init__(self,region=None):
        self.d = d3dshot.create(capture_output="pil",frame_buffer_size=1)
        self.d.capture()
        time.sleep(0.1)

        if region:
                self.left,self.top,x2,y2 = region
                self.width = x2 - self.left + 1
                self.height = y2 - self.top + 1
        else:
            self.width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
            self.height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
            self.left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
            self.top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)



    def grab_screen(self):
        return self.d.frame_buffer[0]

    def close(self):
        self.d.stop()


if __name__ == "__main__":
    clas=screen()
    t=time.time()
    data=clas.grab_screen()
    print(sys.getsizeof(data),data)
    tt=time.time()
    print(tt-t)
    print((tt-t)/120)
    data=pickle.loads(pickle.dumps(data))
    cv2.imshow('55',data)
    cv2.waitKey(0)
    clas.close()
    cv2.destroyAllWindows()