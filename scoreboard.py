from turtle import Turtle, RawTurtle, Shape
from tkinter import *
from PIL import Image, ImageTk
import turtle
from ship import Ship

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.lives = []

        self.score_label = Turtle()
        self.score_label.color("white")
        self.score_label.penup()
        self.score_label.hideturtle()
        self.score_label.goto(-450, 300)
        self.score_label.write("SCORE", font=("Courier", 24, "normal"))

        self.current_score = Turtle()
        self.current_score.color("green")
        self.current_score.penup()
        self.current_score.hideturtle()
        self.current_score.goto(-300, 300)
        self.current_score.write(f"{self.score}", font=("Courier", 24, "normal"))

        self.lives_label = Turtle()
        self.lives_label.color("white")
        self.lives_label.penup()
        self.lives_label.hideturtle()
        self.lives_label.goto(150, 300)
        self.lives_label.write("LIVES", font=("Courier", 24, "normal"))

        initial_live_x = 300
        for live in range(3):
            self.lives.append(Ship(initial_live_x,320))
            initial_live_x += 35

    def add_score(self):
        self.score += 10
        self.current_score.clear()
        self.current_score.write(f"{self.score}", font=("Courier", 24, "normal"))

    def remove_live(self):
        self.lives.pop().hideturtle()



