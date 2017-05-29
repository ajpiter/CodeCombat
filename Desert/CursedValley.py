# The hot sun is draining the hero's health!

while True:
    enemy = hero.findNearestEnemy()
    # Attack if enemy exists AND enemy.team is "ogres"
    # AND enemy.type is "skeleton"
    if enemy and enemy.team == "ogres" and enemy.type == "skeleton":
        hero.attack(enemy)
    item = hero.findNearestItem()
    # Collect if item exists AND item.type is "potion"
    # AND hero.health is less than hero.maxHealth / 4
    if item and item.type == "potion" and hero.health < hero.maxHealth/4:
        hero.moveXY(item.pos.x, item.pos.y)
