# A desert storm is coming!
# Yaks can detect when a storm is coming.

# This variable will be used as a condition.
yak = hero.findNearestEnemy()

# While there is at least one sand yak:
while yak:
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
    # Update the value of the variable yak
    # with findNearestEnemy()
    yak = hero.findNearestEnemy()
    pass
# The yaks have hidden.
# Move to the red X at the hideout.
hero.moveXY(38, 58)
