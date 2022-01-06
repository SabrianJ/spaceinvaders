import turtle
from turtle import Turtle, RawTurtle, Shape
from tkinter import *
from PIL import Image, ImageTk

def register_PIL(name, image):
    photo_image = ImageTk.PhotoImage(image)
    turtle.register_shape(f"{name}", Shape("image", photo_image))

class Alien(Turtle):
    def __init__(self,name, x_pos, y_pos):
        super().__init__()
        image = Image.open(f"images/{name}.gif")
        image = image.resize((30,30))
        register_PIL(f"{name}", image)
        self.shape(f"{name}")
        self.penup()
        self.goto(x_pos, y_pos)

    def shoot(self):
        laser = Turtle()
        image = Image.open(f"images/enemylaser.gif")
        image = image.resize((10, 15))
        register_PIL(f"enemylaser", image)
        laser.shape("enemylaser")
        laser.penup()

        current_x, current_y = self.pos()

        laser.goto(current_x, current_y)

        return laser


