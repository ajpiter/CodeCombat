"""<ust have The Precious and Emperor's Gloves enabled for code to work"""

# An ogre army approaches. Use flags to win the battle!
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag:
        hero.pickUpFlag(flag)
        if enemy and hero.canCast("chain-lightning"):
            hero.cast("chain-lightning", enemy)
        elif hero.canCast("invisibility"):
            hero.cast("invisibility", hero)
    else:
        if enemy:
            hero.attack(enemy)
