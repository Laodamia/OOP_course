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

        img = Image.fromarray(data, 'RGB')
        img.save('canvas.png')
class Rectangle(Canvas):

    def __init__(self, x, y, width, height, color = (0,0,0)):
        super().__init__(width, height)
        self.x = x
        self.y = y
        self.color = color

# class Square(Rectangle):
#
#     def __init__(self,x,y width, height, color):
#         super().__init__(x,y,width,color)
#         self.height = height




c = Canvas(100,100, color = "black")
print(c.draw())
# b = Rectangle(x = 10, y =50, width=200, height=100, color="red")
# print(b)