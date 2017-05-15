# Incoming munchkins! Defend the town!

# Define your own function to fight the enemy!
def cleaveOrAttack():
    # In the function, find an enemy, then cleave or attack it.
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
    pass

# Move between patrol points and call the function.
while True:
    hero.moveXY(35, 34)
    # Use cleaveOrAttack function you defined above.
    cleaveOrAttack()
    hero.moveXY(47, 27)
    # Call the function again.
    cleaveOrAttack()
    hero.moveXY(60, 31)
    # Call the function again.
    cleaveOrAttack()
