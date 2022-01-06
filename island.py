from turtle import Turtle

class Island:
    def __init__(self, starting_x, starting_y):
        self.rocks = []

        row = 3
        column = 4

        for i in range(row):
            current_y = starting_y + (i * 20)

            if i == 0:
                first = Turtle()
                first.penup()
                first.color("red")
                first.shape("square")
                first.goto(starting_x, starting_y)
                self.rocks.append(first)

                second = Turtle()
                second.penup()
                second.color("red")
                second.shape("square")
                second.goto(starting_x + ((column-1) * 20), starting_y)
                self.rocks.append(second)
                continue
            for j in range(column):
                current_x = starting_x + (j * 20)
                rock = Turtle()
                rock.penup()
                rock.color("red")
                rock.shape("square")
                rock.goto(current_x, current_y)
                self.rocks.append(rock)
