# Matthew Godwin 20904377 (MG)
# Vincent Forte-Perri 21006478 (VFP)
# Jason Zouein 21037143 (JZ)

from random import choice
from turtle import *
from freegames import floor, vector
import winsound

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, 160)
# Increased the amount of ghosts from 4 to 7
# Altered the starting locations and movements of the ghosts to fit into the new game board
ghosts = [
    [vector(-180, 160), vector(10, 0)],
    [vector(-180, -145), vector(0, -10)],
    [vector(100, 140), vector(0, 10)],
    [vector(100, -120), vector(-10, 0)],
    [vector(-120, -180), vector(10, 0)],
    [vector(-120, -360), vector(10, 0)],
    [vector(-120, -360), vector(0, 10)]
]

# fmt: off
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0,
    0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0,
    0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0,
    0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]


# Created a new game board by altering the placement of the ones and zeros,
# Added additional rows to increase the playable area
# Added a two at the end of the grid to represent the final winning tile

def square(x, y):
    """Draw square using path at (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """Draw world using path."""
    # Changed the colour of the path and of the background
    bgcolor('black')
    path.color('teal')
    for index in range(len(tiles)):
        tile = tiles[index]
        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)
            # Set a parameter which created a red dot on the two tile in our grid which is the exit of the maze

            if tile == 2:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(20, 'red')


# We removed the function that added to pac-mans score as it isn't necessary for our iteration of the game
def move():
    """Move pacman and all ghosts."""
    writer.undo()
    writer.write(state['score'])
    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)
    # Added winning text and a winning sound to the two tile when it is touched by Pac-man
    if tiles[index] == 2:
        tiles[index] = 3
        winner = Turtle()
        winner.penup()
        winner.color('yellow')
        style = ('Bauhaus 93', 45, 'italic')
        winner.write('You Won!', font=style, align='center')
        winsound.PlaySound('olg-winner-gagnant.wav', winsound.SND_ASYNC)
        return

    # changed the colour of pac-man from yellow to purple
    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'purple')
    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        # changed the move speed of the ghosts from 5 to 10
        else:
            options = [
                vector(10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, -10), ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y
        up()
        goto(point.x + 10, point.y + 10)
        # changed the colour of the ghosts from red to yellow
        dot(20, 'yellow')
    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            # When pac-man comes into contact with a ghost, a message displaying "You lost!" will pop up and pacman
            # death sound will play this will also end the code.
            loser = Turtle()
            loser.penup()
            loser.color('red')
            style = ('Bauhaus 93', 45, 'italic')
            loser.write('You Lost!', font=style, align='center')
            winsound.PlaySound('pacman_death.wav', winsound.SND_ASYNC)
            return

    ontimer(move, 100)


def change(x, y):
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


screensize(1920, 1080)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('black')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
# this function adds a sound when the game starts up.
winsound.PlaySound('pacman_beginning.wav', winsound.SND_ASYNC)
world()
move()
done()
