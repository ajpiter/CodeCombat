# Gather 4 lightstones to defeat the Brawler.
# If you find a lightstone, hide.

def checkTakeHide(item):
    if item:
        # The item is here, so take it.
        hero.moveXY(item.pos.x, item.pos.y)
        # Then move to the center of the camp (40, 34)
        hero.moveXY(40, 34)

while True:
    # Move to the top right X mark.
    hero.moveXY(68, 56)
    # Search for a stone there.
    stone = hero.findNearestItem()
    # Call checkTakeHide() with the argument: stone
    checkTakeHide(stone)
    hero.moveXY(12, 56)
    # Move to the top left mark.
    stone = hero.findNearestItem()
    # Search for a stone.
    checkTakeHide(stone)
    # Call the checkTakeHide() function.
    # Pass in the result of your search as an argument.
    pass
