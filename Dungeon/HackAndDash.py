# You can write code before a loop.
# Break open the "Chest" before using the loop to escape the maze!
hero.moveRight()
hero.moveUp()
hero.attack("Chest")
hero.moveDown()

while True:
    # Move 3 times.
    hero.moveRight(3)
    hero.moveDown(3)
