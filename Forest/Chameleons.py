# Ogres are disguised as coins or gems!

while True:
    enemy = hero.findNearestEnemy()
    # If you see an enemy - attack it:
    if enemy:
        hero.attack(enemy)
    item = hero.findNearestItem()
    # If you see a coin or a gem - move to it's X and Y position:
    if item:
        pos = item.pos
        x = pos.x
        y = pos.y
        hero.moveXY(x, y)
