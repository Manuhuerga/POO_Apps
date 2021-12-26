class Rectangle:
    def __init__(self,x,y,h,w,color):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color

    def draw(self,canvas):
        canvas.data[self.x: self.x + self.w , self.y : self.y + self.h] = self.color

class Square:
    def __init__(self,x,y,side,color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self,canvas):
        canvas.data[self.x: self.x + self.side, self.y : self.y + self.side] = self.color
