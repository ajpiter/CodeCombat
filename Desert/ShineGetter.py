# To grab the most gold quickly, just go after gold coins.

while True:
    coins = hero.findItems()
    coinIndex = 0
    # Wrap this into a loop that iterates over all coins.
    # Gold coins are worth 3.
    # Only pick up gold coins.
    while coinIndex < len(coins):
        coin = coins[coinIndex]
        if coin.value == 3:
            hero.moveXY(coin.pos.x, coin.pos.y)
        coinIndex += 1
pass
