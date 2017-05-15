# Munchkins are attacking!
# The swarms will come at regular intervals.
# Whenever you can, cleave to clear the mass of enemies.

while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)
        hero.attack(enemy)
