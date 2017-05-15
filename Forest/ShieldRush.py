# Survive both waves by shielding and cleaving.
# When "cleave" is not ready, use your shield skill.
# You'll need at least 142 health to survive.

while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.shield()
