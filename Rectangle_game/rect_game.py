import random
import turtle

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def falls_in_rectangle (self, rect):
        if rect.point1.x < self.x < rect.point2.x and rect.point1.y < self.y < rect.point2.y:
            return True
        else:
            return False
    
    def distance(self,point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**1/2
        
class Rectangle:

    def __init__(self, point1,point2 ):
        self.point1 = point1
        self.point2 = point2
    
    def area (self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)

class GuiRectangle(Rectangle):
    
    def draw_rect(self):
        myturtle= turtle.Turtle()
        myturtle.penup()
        myturtle.goto(self.point1.x , self.point1.y)
        myturtle.pendown()
        myturtle.goto(self.point2.x ,self.point1.y)
        myturtle.goto(self.point2.x ,self.point2.y)
        myturtle.goto(self.point1.x ,self.point2.y)
        myturtle.goto(self.point1.x ,self.point1.y)
        

class GuiPoint(Point):

    def draw_point(self):
        myturtle= turtle.Turtle()
        myturtle.penup()
        myturtle.goto(self.x ,self.y)
        myturtle.pendown()
        myturtle.dot(9,'blue')
        


#Generate a random values for this points
point1 = Point(random.randint(0,100),random.randint(0,100))
point2 = Point(random.randint(100,200),random.randint(100,200))

print(f'The coordinates of rectangle is: {point1.x,point1.y}{point2.x,point2.y}')

#Create a rectangle object
rect = Rectangle(point1, point2)

#Get point and area from user
user_area = int(input('Input your area: '))
print(f'Rectangle area is {rect.area()}')
print('Your suposition is: ', rect.area() == user_area)
point = Point(int(input('Input x coordinate: ')), int(input('Input y coordinates: ')))
print(point.falls_in_rectangle(rect))

#Get distance from the point3
point3 = Point(100,100)
print(point.distance(point3))

#Draw Rectangle
draw = GuiRectangle(point1, point2)
draw.draw_rect()

#Draw Point
draw_2 = GuiPoint(point.x,point.y)
draw_2.draw_point()

turtle.done()