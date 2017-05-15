while True:
    # Check the distance to the nearest enemy.
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    # If it comes closer than 10 meters, cleave it!
    if distance < 10:
        hero.cleave(enemy)
    # Else, attack the "Chest" by name.
    else:
        hero.attack("Chest")
    pass
