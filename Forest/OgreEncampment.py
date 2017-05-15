# If there is an enemy, attack it.
# Otherwise, attack the chest!

while True:
    # Use if/else.
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    else:
        hero.attack("Chest")
