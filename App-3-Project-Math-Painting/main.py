import numpy as np
from PIL import Image
class Canvas():

     def __init__(self, width, height, color ="white"):
         self.width = width
         self.height = height
         self.color = color

     def draw(self):
        data = np.zeros((self.width, self.height,3), dtype=np.uint8)
        if self.color == "black":
            data[:] = [0,0,0]
        else:
            data[:] = [255,255,255]

        return data


class Rectangle(Canvas):

    def __init__(self, x, y, width, height, color = (0,0,0)):
        super().__init__(width, height)
        self.x = x
        self.y = y
        self.color = color

    def draw(self, data):
        data[self.y:self.y+self.height, self.x:self.x+self.width] = self.color
        return data


class Square(Rectangle):

    def __init__(self,x,y, side_length, color=(0,0,0)):
        super().__init__(x,y,side_length,side_length, color)

c = Canvas(400,400, color = "black")
canvas_background = c.draw()

b = Rectangle(x = 10, y =50, width=200, height=100, color=(200,160,40))
data = b.draw(canvas_background)

s = Square(x=4, y=60, side_length=20, color=(160,170,3))
data = s.draw(data)

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')