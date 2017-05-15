# Cast your "drain-life" spell at short range.
# Attack with your staff at long range.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < 15:
            # Cast "drain-life" on the enemy.
            hero.cast("drain-life", enemy)
        else:
            # Attack the enemy with your staff.
            hero.attack(enemy)
