# Protect brandy from incoming thirsty yaks!
# Gather gold to build decoys to distract the yaks.
# Use flags to decide when and where to build decoys.

while True:
    flag = hero.findFlag()
    if flag and hero.gold >= 25:
        hero.buildXY("decoy", flag.pos.x, flag.pos.y)
        hero.pickUpFlag(flag)
    else:
        coin = hero.findNearestItem()
        hero.moveXY(coin.pos.x, coin.pos.y)
