# Patrol and place traps ONLY if you see a coin.

# Write this function.
def maybeBuildTrap(x, y):
    # Move to the given x,y postion
    hero.moveXY(x, y)
    # Search a coin and  if you see it, build a "fire-trap"
    item = hero.findNearestItem()
    if item and item.type == "coin":
        hero.buildXY("fire-trap", x, y)
    pass

while True:
    # Call maybeBuildTrap for the top left passage.
    maybeBuildTrap(12, 56)
    # Now for the top right passage.
    maybeBuildTrap(68,56)
    # Now for the bottom right passage.
    maybeBuildTrap(68,12)
    # Now for the bottom left passage.
    maybeBuildTrap(12,12)
