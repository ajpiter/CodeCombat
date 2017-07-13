# Collect more coins than your doppelganger.
# You only have a few seconds to collect coins. Choose your path wisely!
while True:
    bestCoin = None
    maxRating = 0
    coinIndex = 0
    coins = hero.findItems()
    # Try calculating "value / distance" to decide which coins to get.
    for coin in coins:
        dist = hero.distanceTo(coin)
        if (coin.value / dist) > maxRating:
            bestCoin = coin
            maxRating = coin.value/dist
    if bestCoin:
        #Now go to the closest gold coin and get it!
        hero.moveXY(bestCoin.pos.x, bestCoin.pos.y)
        pass
