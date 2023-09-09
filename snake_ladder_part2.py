import random
import turtle

# Setting up the screen
screen = turtle.Screen()
screen.title("Snake and Ladder Game")

# Creating the dice
dice = turtle.Turtle()
dice.speed(0)
dice.penup()
dice.goto(-200, 250)
dice.pendown()

# Creating the board
board = turtle.Turtle()
board.speed(0)
board.penup()
board.goto(0, 0)

# Define the number of squares on the board
num_squares = 100
square_size = 20

# Define the snakes and ladders
snakes = {99: 10, 70: 29, 55: 7, 28: 1, 83: 19}
ladders = {6: 25, 11: 40, 17: 69, 46: 90, 64: 86}

# Draw the board
for i in range(num_squares):
    board.pendown()
    for j in range(4):
        board.forward(square_size)
        board.right(90)
    board.penup()
    board.forward(square_size)

# Write the numbers on the board
board.goto(-10, 210)
for i in range(10, 100, 10):
    board.write(i, align="center", font=("Arial", 12, "normal"))
    board.forward(square_size * 10)

# Place the player on the starting square
player_position = 0
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("circle")
player.color("red")
player.goto(-180 + player_position * square_size, 180)

# Function to move the player
def move_player():
    global player_position
    dice_roll = random.randint(1, 6)
    player_position += dice_roll
    dice.clear()
    dice.write("You rolled a " + str(dice_roll), align="center", font=("Arial", 16, "normal"))
    if player_position in snakes:
        player_position = snakes[player_position]
    elif player_position in ladders:
        player_position = ladders[player_position]
    player.goto(-180 + player_position * square_size, 180)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_player, "space")

# Main loop
while True:
    screen.update()

screen.mainloop()
