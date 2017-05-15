# Don't worry about small and medium-sized ogres.
# Your targets are type "brawler".
# When a "brawler" is closer than 50m, fire artillery.

while True:
    # Find the nearest enemy and the distance to it.
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    # If the enemy's type is "brawler"
    # AND the distance to it is less than 50 meters,
    # Then say "Fire!" to signal the artillery.
    if enemy.type == "brawler" and distance <50:
        hero.say("Fire!")
    pass
