# Get to the oasis. Watch out for new enemies: ogre scouts!
# Go up and right by adding to the current X and Y position.

while True:
    # If there's an enemy, attack.
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    # Else, keep moving up and to the right. 
    else:
        x = hero.pos.x + 5
        y = hero.pos.y + 5
        hero.moveXY(x, y)
    pass
