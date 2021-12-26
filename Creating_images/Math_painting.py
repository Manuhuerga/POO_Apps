from canvas import Canvas
from shape import Square,Rectangle
from colors import colors


game = True

while (game):
    print('Hello, welcome to math painting')
    op = True
    while(op):
        try:
            back= str(input('Select background color (white or black): '))
            back = back.upper()
            if back == 'WHITE':
                color_can = (255,255,255)
                op = False
                break
            elif back == 'BLACK':
                color_can = (0,0,0)
                op = False
                break
            else:
                print('Option no list')

        except:
            print('Please, select a correct option')
    

    dimentions = [int(input('Width: ')), int(input('High: '))]
    
    can = Canvas(dimentions[0],dimentions[1],color_can)

    op2 = True

    while(op2):

        shape= str(input('Please select a shape(Rectangle or Square): '))
        shape = shape.upper()

        if(shape == 'SQUARE'):
            coord = [int(input('X position: ')), int(input('Y position: '))]
            side = int(input('Side: '))
            c = str(input('Color (blue,red,green): '))
            c = c.lower()
            sq1 = Square(coord[0], coord[1],side, colors[c])
            sq1.draw(can)
            can.make('Testing.png')

        elif(shape == 'RECTANGLE'):
            coord2 = [int(input('X position: ')), int(input('Y position: '))]
            dimentions2 = [int(input('Width: ')), int(input('High: '))]
            c = str(input('Color (blue,red,green): '))
            c = c.lower()
            rect1 = Rectangle(coord2[0],coord2[1],dimentions2[0],dimentions2[1],colors[c])
            rect1.draw(can)
            can.make('Testing.png')

        cont= str(input('Do you continue this game? : '))
        cont = cont.upper()
        if cont=='NO':
            op2= False
            op= False
            game =False
            print('Chiao')
        else:
            pass