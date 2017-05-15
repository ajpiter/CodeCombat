# Sneak through the forest and ambush the shaman.
# Listen to Commander Craig for warning of approaching enemy.

# Place flags after pressing Submit.
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag:
        # Pick the flag up.
        hero.pickUpFlag(flag)
        pass
    elif enemy:
        # Attack enemies on sight.
        hero.attack(enemy)
        pass
