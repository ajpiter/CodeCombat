# Collect exactly 7 spinach potions.
# Then you'll be strong enough to defeat the ogres.
potionCount = 0
# Wrap the potion collection code inside a while loop.
# Use a condition to check the potionCount
while potionCount < 7:
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
        potionCount += 1

# When the while loop is finished,
# Go and fight!
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
