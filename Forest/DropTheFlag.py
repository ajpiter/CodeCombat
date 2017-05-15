# Put flags where you want to build traps.
# When you're not building traps, pick up coins!

while True:
    flag = hero.findFlag()
    if flag:
        # How do we get flagX and flagY from the flag's pos?
        # (Look below at how to get x and y from items.)
        flagPos = flag.pos
        flagX = flagPos.x
        flagY = flagPos.y 
        hero.moveXY(flagX, flagY)
        hero.buildXY("fire-trap", flagX, flagY)
        hero.pickUpFlag(flag)
    else:
        item = hero.findNearestItem()
        if item:
            itemPos = item.pos
            itemX = itemPos.x
            itemY = itemPos.y
            hero.moveXY(itemX, itemY)
