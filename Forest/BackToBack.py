# Stay in the middle and defend!

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Either attack the enemy...
        hero.attack(enemy)
        hero.attack(enemy)
        pass
    else:
        # ... or move back to your defensive position.
        hero.moveXY(40,33)
        pass
