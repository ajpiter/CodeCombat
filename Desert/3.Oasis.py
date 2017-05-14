"""Do not play with softened leather boots. Your boots need to have a speed of 2 in order for the code to work."""

# Move right to reach the oasis,
# Move left to avoid nearby yaks.
while True:
    x = hero.pos.x
    y = hero.pos.y
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        # Subtract 10 from x to move left.
        x = hero.pos.x - 10
        y = hero.pos.y
        # Use moveXY to move to the new x, y position.
        hero.moveXY(x,y)
        pass
    else:
        # Add 10 to x to move right.
        x = hero.pos.x + 10 
        y = hero.pos.y
        # Use moveXY to move to the new x, y position.
        hero.moveXY(x,y)
        pass
