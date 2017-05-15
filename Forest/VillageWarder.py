# This function attacks the nearest enemy.
def findAndAttackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

# Define a function to cleave enemies (but only when the ability is ready).
def findAndCleaveEnemy():
    # Find the nearest enemy:
    enemy = hero.findNearestEnemy()
    # If an enemy exists:
    if enemy:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
        # And if "cleave" is ready:
            # It's time to cleave!
    pass

# In your main loop, patrol, cleave, and attack.
while True:
    # Move to the patrol point, cleave, and attack.
    hero.moveXY(35, 34)
    findAndCleaveEnemy()
    findAndAttackEnemy()
    # Move to the other point:
    hero.moveXY(60, 31)
    # Use findAndCleaveEnemy function:
    findAndCleaveEnemy()
    # Use findAndAttackEnemy function:
    findAndAttackEnemy()
