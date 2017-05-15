# Patrol the village entrances.
# If you find an enemy, attack it.
while True:
    hero.moveXY(35, 34)
    left = hero.findNearestEnemy()
    if left:
        hero.attack(left)
        hero.attack(left)
    # Now move to the right entrance.
    hero.moveXY(60, 31)
    # Find the right enemy.
    # Use "if" to attack if there is a right enemy.
    right = hero.findNearestEnemy() 
    if right:
        hero.attack(right)
        hero.attack(right)
