import time
import turtle
from turtle import Turtle, RawTurtle, Shape
from tkinter import *
from PIL import Image, ImageTk
import threading


def register_PIL(name, image):
    photo_image = ImageTk.PhotoImage(image)
    turtle.register_shape(f"{name}", Shape("image", photo_image))


class Ship(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        image = Image.open("images/ship.gif")
        image = image.resize((30, 30))
        register_PIL("ship", image)
        self.shape("ship")
        self.penup()
        self.goto(x_pos, y_pos)
        self.cooldown = False

    def move_left(self):
        current_x, current_y = self.pos()

        if current_x - 25 >= -425:
            self.goto(current_x - 25, current_y)

    def move_right(self):
        current_x, current_y = self.pos()

        if current_x + 25 <= 425:
            self.goto(current_x + 25, current_y)

    def shoot(self, ship_lasers):
        if not self.cooldown:
            laser = Turtle()
            image = Image.open(f"images/laser.gif")
            image = image.resize((10, 15))
            register_PIL(f"laser", image)
            laser.shape("laser")
            laser.penup()

            current_x, current_y = self.pos()

            laser.goto(current_x, current_y)

            ship_lasers.append(laser)

            self.cooldown = True

            threading.Thread(target=self.deactivate_cooldown).start()


    def explode(self):
        image = Image.open("images/explosiongreen.gif")
        image = image.resize((30, 30))
        register_PIL("explode", image)
        self.shape("explode")
        self.penup()

    def restate(self):
        image = Image.open("images/ship.gif")
        image = image.resize((30, 30))
        register_PIL("ship", image)
        self.shape("ship")
        self.penup()

    def deactivate_cooldown(self):
        time.sleep(3)
        self.cooldown = False
