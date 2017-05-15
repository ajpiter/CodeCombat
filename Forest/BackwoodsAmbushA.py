# In this level you will use functions with two parameters.
# Look at the structure below, notice how there are two arguments.
# These are both accessible within the function. 

def checkAndAttack(x, y):
    # First move to the coordinates provided by the parameters.
    hero.moveXY(x, y)
    # Then check for an enemy.
    enemy = hero.findNearestEnemy()
    if enemy:
        # If there is one, attack it!
        hero.attack(enemy)
    pass

checkAndAttack(24, 42)
checkAndAttack(27, 60)
# Navigate to the last 3 x-marks and defeat any remaining munchkins.
checkAndAttack(42, 50)
checkAndAttack(39, 24)
checkAndAttack(55, 29)
