while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Replace this with your own code.
        # Find the distance to the enemy with distanceTo.
        if hero.distanceTo(enemy) < 5:
            if hero.isReady("cleave"):
                hero.cleave(enemy)
            else:
                hero.attack(enemy)
