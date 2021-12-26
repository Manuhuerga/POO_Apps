import numpy as np
from PIL import Image

class Canvas:
    def __init__(self,w,h,color):
        self.w = w
        self.h = h
        self.color = color

        self.data = np.zeros((self.h, self.w, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make (self,filename):
        img = Image.fromarray(self.data, 'RGB')
        img.save(filename)