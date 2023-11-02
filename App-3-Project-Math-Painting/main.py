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
        # cover for the case when the shape goes off canvas bounds
        if self.y+self.height >= Canvas.height:
            y_slice = Canvas.height - self.y
        if self.x+self.width >= Canvas.width:
            x_slice = Canvas.width - self.x
        else:
            y_slice = self.y + self.height
            x_slice = self.x + self.width
        data[self.y:y_slice, self.x:x_slice] = self.color
        return data


class Square(Rectangle):

    def __init__(self,x,y, side_length, color=(0,0,0)):
        super().__init__(x,y,side_length,side_length, color)

# get the user to give input to create a canvas
canvas_width = int(input("Enter canvas width in px: "))
canvas_height = int(input("Enter canvas height in px: "))
canvas_color = input("Enter canvas color (white or black): ")

#instantiate a canvas
c = Canvas(width=canvas_width,height=canvas_height, color = canvas_color)

#draw a canvas
canvas_background = c.draw()

# get choice of what to draw
# it has to go on until the user quits so this is not the right way to go
shape = input("what would you like to draw (rectangle or a square)? ")
x_point = input(f"Enter x of the {shape}: ")
y_point = input(f"Enter y of the {shape}: ")

if shape == "rectangle":
    width = input(f"Enter the width of the {shape}: ")
    height = input(f"Enter the height of the {shape}: ")
    b = Rectangle(x=x_point, y=y_point, width=width, height=height, color=(200,160,40))
    data = b.draw(canvas_background)
elif shape == "square":
    side_length = input(f"Enter the height of the {shape}: ")
    s = Square(x=x_point, y=y_point, side_length=side_length, color=(160,170,3))
    data = s.draw(canvas_background)

# create image
img = Image.fromarray(data, 'RGB')

#save image
img.save('canvas.png')