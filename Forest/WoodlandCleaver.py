# Use your new "cleave" skill as often as you can.

hero.moveXY(23, 23)
while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        # Cleave the enemy!
        hero.cleave(enemy)
        pass
    else:
        # Else (if cleave isn't ready), do your normal attack.
        hero.attack(enemy)
        pass
