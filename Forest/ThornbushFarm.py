# Patrol the village entrances.
# Build a "fire-trap" when you see an ogre.
# Don't blow up any peasants!

while True:
    hero.moveXY(43, 50)
    top = hero.findNearestEnemy()
    if top:
        hero.buildXY("fire-trap", 43, 50)
    hero.moveXY(25, 34)
    left = hero.findNearestEnemy()
    # Check if left exists.
    if left:
        # Build a trap at 25, 34 if the enemy exists.
        hero.buildXY("fire-trap", 25, 34)
    hero.moveXY(43, 20)
    # Set a variable for the bottom enemy.
    bottom = hero.findNearestEnemy()
    # Check if the bottom enemy exists.
    if bottom:
        # Build a trap if an enemy exists.
        hero.buildXY("fire-trap", 43, 20)
