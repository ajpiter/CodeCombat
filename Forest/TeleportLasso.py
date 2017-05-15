""" I had to unequip ring of speed and the precious for this level to work"""

# Our wizards teleport ogres from their camp here.
# They appear for a short period and they are stunned.
# Attack only weak and near ogres.

while True:
    # If enemy.type is "munchkin"
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if enemy and enemy.type == "munchkin" and distance < 20:
            hero.attack(enemy)
    # AND the distance to it is less than 20m
        # Then attack it.
