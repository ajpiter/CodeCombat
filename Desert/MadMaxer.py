# Attack the enemy that's farthest away first.

while True:
    farthest = None
    maxDistance = 0
    enemyIndex = 0
    enemies = hero.findEnemies()

    # Look at all the enemies to figure out which one is farthest away.
    while enemyIndex < len(enemies):
        target = enemies[enemyIndex]
        enemyIndex += 1

        # Is this enemy farther than the farthest we've seen so far?
        distance = hero.distanceTo(target)
        if distance > maxDistance:
            maxDistance = distance
            farthest = target

    if farthest:
        # Take out the farthest enemy!
        # Keep attacking the enemy while its health is greater than 0.
        while target.health > 0:
            hero.attack(target)
        pass
