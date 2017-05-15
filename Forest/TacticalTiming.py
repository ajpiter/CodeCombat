# Help out on the front line.
# Move back to a flag if any try to sneak by.
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag:
        hero.pickUpFlag(flag)
    else:
        if enemy:
            hero.attack(enemy)
