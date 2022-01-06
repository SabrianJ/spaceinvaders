from turtle import Turtle, Screen
from alien import Alien
from ship import Ship
from scoreboard import Scoreboard
import time
import random
from island import Island

screen = Screen()
screen.setup(width=920, height=700)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

aliens = []
enemy_lasers = []
ship_lasers = []
islands = []

row = 5
column = 11

starting_y = 100
for i in range(row):
    current_y = starting_y + (i * 35)
    starting_x = -420
    for j in range(column):
        current_x = starting_x + (j * 40)
        alien = Alien("enemy1_1",current_x,current_y)
        aliens.append(alien)

ship = Ship(-425,-300)
scoreboard = Scoreboard()

island_starting_x = -340
for i in range(4):
    island = Island(island_starting_x,-150)
    island_starting_x += 200
    islands.append(island)



screen.listen()
screen.onkeypress(ship.move_left, "Left")
screen.onkeypress(ship.move_right, "Right")
screen.onkeyrelease(lambda ship_lasers=ship_lasers: ship.shoot(ship_lasers), "space")


alien_movement = 10
count = 0
game_over = False

while not game_over:
    try:
        screen.update()
        ship.restate()
        count += 1

        reverse = False

        for alien in aliens:
            current_x, current_y = alien.pos()
            alien.goto(current_x + alien_movement, current_y)

            new_x = current_x + alien_movement

            if new_x == 420 or new_x == -420:
                reverse = True

        for enemy_laser in enemy_lasers:
            current_x, current_y = enemy_laser.pos()
            enemy_laser.goto(current_x, current_y - 10)

            if enemy_laser.distance(ship) < 30:
                if len(scoreboard.lives) != 0:
                    scoreboard.remove_live()
                    ship.explode()
                    enemy_lasers.remove(enemy_laser)
                    enemy_laser.hideturtle()
                else:
                    game_over = True

            for island in islands:
                for rock in island.rocks:
                    if enemy_laser.distance(rock) < 20:
                        enemy_lasers.remove(enemy_laser)
                        island.rocks.remove(rock)
                        enemy_laser.hideturtle()
                        rock.hideturtle()


        for ship_laser in ship_lasers:
            current_x, current_y = ship_laser.pos()
            ship_laser.goto(current_x, current_y + 10)

            for alien in aliens:
                if ship_laser.distance(alien) < 30:
                    aliens.remove(alien)
                    ship_lasers.remove(ship_laser)
                    ship_laser.hideturtle()
                    alien.hideturtle()
                    scoreboard.add_score()

            if current_y > 500:
                ship_lasers.remove(ship_laser)



        for ship_laser in ship_lasers:
            for enemy_laser in enemy_lasers:
                if ship_laser.distance(enemy_laser) < 20:
                    enemy_lasers.remove(enemy_laser)
                    ship_lasers.remove(ship_laser)
                    enemy_laser.hideturtle()
                    ship_laser.hideturtle()

            for island in islands:
                for rock in island.rocks:
                    if ship_laser.distance(rock) < 20:
                        ship_lasers.remove(ship_laser)
                        island.rocks.remove(rock)
                        ship_laser.hideturtle()
                        rock.hideturtle()

        if reverse:
            alien_movement *= -1
            for alien in aliens:
                current_x, current_y = alien.pos()
                alien.goto(current_x, current_y -5)

                if current_y < -300:
                    game_over = True
                    break

        if count % 10 == 0:
            enemy_lasers.append(random.choice(aliens).shoot())

        time.sleep(0.09)
    except ValueError:
        continue

gameover = Turtle()
gameover.color("white")
gameover.penup()
gameover.hideturtle()
gameover.goto(-350, 0)
gameover.write("GAME OVER", font=("Courier", 100, "normal"))

screen.exitonclick()

