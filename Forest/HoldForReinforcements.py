# Ogres are climbing the cliffs!
# Protect the peasants long enough for the militia to assemble.
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag:
        # Pick up the flag.
        hero.pickUpFlag(flag)
        pass
    
    elif enemy:
        # Else, attack!
        # Use flags to move into position, and cleave if ready.
        if hero.isReady("cleave"): 
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
