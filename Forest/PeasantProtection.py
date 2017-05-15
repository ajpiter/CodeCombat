while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if distance < 10:
        # Attack if they get too close to the peasant.
        hero.attack(enemy)
        pass
    # Else, stay close to the peasant! Use else.
    else:
        hero.moveXY(40, 37)
