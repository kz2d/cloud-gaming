import cv2
import numpy as np


class ShowWindow:
    def __init__(self,h,w):
        self.width=int(w)
        self.height=int(h)

    def show(self,bitArray):
        img=np.array(bitArray)
        print(img.shape) 
        # img = np.frombuffer(bitArray, dtype='uint8')
        # img.shape = (self.height,self.width,4)
        cv2.imshow('55',img)
        cv2.waitKey(1)

    def close(self):
        cv2.destroyAllWindows()