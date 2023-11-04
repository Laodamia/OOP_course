import numpy as np
from PIL import Image
class Canvas():

     def __init__(self, width, height, color ="white"):
         self.width = width
         self.height = height
         self.color = color
         self.data = np.zeros((self.width, self.height,3), dtype=np.uint8)

         if self.color == "black":
             self.data[:] = [0,0,0]
         else:
             self.data[:] = [255,255,255]
     def make(self, imagepath):
         # create image
         img = Image.fromarray(self.data, 'RGB')
         # save image
         img.save(imagepath)


class Rectangle:

    def __init__(self, x, y, width, height, color = (0,0,0)):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

    def draw(self, canvas):
        # cover for the case when the shape goes off canvas bounds
        canvas.data[self.y:self.y + self.height, self.x:self.x + self.width] = self.color

class Square:

    def __init__(self, x, y, height, color=(0,0,0)):
        self.x = x
        self.y = y
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y:self.y + self.height, self.x:self.x + self.height] = self.color

# get the user to give input to create a canvas
canvas_width = int(input("Enter canvas width in px: "))
canvas_height = int(input("Enter canvas height in px: "))
canvas_color = input("Enter canvas color (white or black): ")
#instantiate a canvas
canvas = Canvas(width=canvas_width,height=canvas_height, color = canvas_color)

while True:
    # get choice of what to draw
    # it has to go on until the user quits so this is not the right way to go
    shape = input("What would you like to draw (rectangle or a square)? ")
    if shape == "rectangle":
        width = int(input(f"Enter the width of the {shape}: "))
        height = int(input(f"Enter the height of the {shape}: "))
        x_point = int(input(f"Enter x of the {shape}: "))
        y_point = int(input(f"Enter y of the {shape}: "))

        # colours
        red = int(input(f"How much red should the {shape} have? (0-255) "))
        green = int(input(f"How much green should the {shape} have? (0-255) "))
        blue = int(input(f"How much blue should the {shape} have? (0-255) "))
        to_draw = Rectangle(x=x_point, y=y_point, width=width, height=height, color=(red,green, blue))
        to_draw.draw(canvas)

    elif shape == "square":
        height = int(input(f"Enter the side of the {shape}: "))
        x_point = int(input(f"Enter x of the {shape}: "))
        y_point = int(input(f"Enter y of the {shape}: "))
        red = int(input(f"How much red should the {shape} have? (0-255) "))
        green = int(input(f"How much green should the {shape} have? (0-255) "))
        blue = int(input(f"How much blue should the {shape} have? (0-255) "))
        to_draw = Square(x=x_point, y=y_point, height=height, color=(red,green, blue))
        to_draw.draw(canvas)

    else:
        print("This is not a shape I like! Remember you can only enter 'rectangle' or 'square'.")

    quit = input("If you're finished press 'q', if you want to continue, press anything else. ")
    if quit == 'q':
        break

canvas.make('canvas.png')

