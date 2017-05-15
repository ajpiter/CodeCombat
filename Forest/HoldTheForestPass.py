# Use flags to join the battle or retreat.
# If you fail, press Submit again for new random enemies and try again!
# You'll want at least 300 health, if not more.
while True:
    enemy = hero.findNearestEnemy()
    flag = hero.findFlag()
    if flag:
        # Pick up the flag.
        hero.pickUpFlag(flag)
        pass
    elif enemy:
        # Fight!
        hero.attack(enemy)
        pass
