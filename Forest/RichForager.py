"""Unequiped the ring of speed"""

# Use "if" and "else if" to handle any situation.
# Put it all together to defeat enemies and pick up coins!
# Make sure you bought great armor from the item shop! 400 health recommended.

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if flag:
        # What happens when I find a flag?
        hero.pickUpFlag(flag)
    elif enemy:
        # What happens when I find an enemy?
        hero.attack(enemy)
    elif item:
        # What happens when I find an item?
        hero.moveXY(item.pos.x, item.pos.y)
