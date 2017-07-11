# Coins here disappear after a few seconds!
# Get all the gold coins before they vanish.

while True:
    closestGold = None
    minGoldDist = 9001
    coinIndex = 0
    coins = hero.findItems()
    # Find the closest coin that is gold.
    # Remember that gold coins have a value of 3.
    for coin in coins:
        dist = hero.distanceTo(coin)
        if minGoldDist > dist and coin.value ==3:
            closestGold = coin
            minGoldDist = dist
    if closestGold:
        #Now go to the closest gold coin and get it!
        hero.moveXY(closestGold.pos.x, closestGold.pos.y)
        pass
