import random

# initial position
position = 0

# function to play the game
def play_game():
  roll_dice = random.randint(1, 6)
  print("You rolled a", roll_dice)
  global position
  position += roll_dice
  print("You are now on square", position)

  # check for ladders
  if position == 3:
    position = 22
    print("You climbed up a ladder to", position)
  elif position == 5:
    position = 8
    print("You climbed up a ladder to", position)
  elif position == 18:
    position = 9
    print("You climbed down a snake to", position)
  elif position == 20:
    position = 14
    print("You climbed down a snake to", position)

# loop until the player reaches square 100
while position < 100:
  play_game()

print("You won!")
