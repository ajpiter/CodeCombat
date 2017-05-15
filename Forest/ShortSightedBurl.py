# Collect coins and run lest the burl will find you.

# Write the function "checkTakeRun" with one parameter.
# If the item exists, take it.
# Move to the start point (the green mark) whether the item or no.
def checkTakeRun(target): 
    if target: 
        hero.moveXY(target.pos.x, target.pos.y)
    hero.moveXY(40, 12)

# Don't change this code.
while True:
    hero.moveXY(16, 56)
    item = hero.findNearestItem()
    checkTakeRun(item)
    hero.moveXY(64, 56)
    item = hero.findNearestItem()
    checkTakeRun(item)
