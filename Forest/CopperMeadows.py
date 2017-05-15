# Collect all the coins in each meadow.
# Use flags to move between meadows.
# Press Submit when you are ready to place flags.


while True:
    flag = hero.findFlag()
    if flag:
        pass  # pass is a placeholder, it has no effect.
        # Pick up the flag.
        hero.pickUpFlag(flag)
    else:
        # Automatically move to the nearest item you see.
        item = hero.findNearestItem()
        if item:
            position = item.pos
            x = position.x
            y = position.y
            hero.moveXY(x, y)
