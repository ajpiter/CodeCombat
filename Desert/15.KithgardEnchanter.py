"""You do not need to change your boots to beat this level. Define moveUp, and moveDown and then the popup warning will go away."""

# Define your own simple movement functions.
# Define moveRight
# Note: each function should move the hero 12 meters!
def moveRight():
    x = hero.pos.x + 12
    y = hero.pos.y
    hero.moveXY(x, y)

# Define moveUp
def moveUp():
    x = hero.pos.x
    y = hero.pos.y+12 
    hero.moveXY(x, y)
# Define moveDown
def moveDown():
    x = hero.pos.x 
    y = hero.pos.y-12
    hero.moveXY(x, y)
# Now, use those functions!
moveRight()
moveDown()
moveUp()
moveUp()
moveRight()
