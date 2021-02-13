import cv2
import numpy as np
from PIL import Image
from io import BytesIO


class ShowWindow:
    def __init__(self,h,w):
        self.width=int(w)
        self.height=int(h)

    def show(self,bitArray):
        bites=BytesIO(bitArray)
        array=Image.open(bites)
        img=np.array(array)
        print(img.shape) 
        # img = np.frombuffer(bitArray, dtype='uint8')
        # img.shape = (self.height,self.width,4)
        cv2.imshow('55',img)
        cv2.waitKey(1)

    def close(self):
        cv2.destroyAllWindows()