# Wait for ogres, defeat them and collect gold.

while True:
    enemies = hero.findEnemies()
    # enemyIndex is used to iterate the enemies array.
    enemyIndex = 0
    # While enemyIndex is less than len(enemies)
    while enemyIndex < len(enemies):
        # Attack the enemy at enemyIndex
        enemy = enemies[enemyIndex]
        hero.attack(enemy)
        # Increase enemyIndex by one.
        enemyIndex += 1
    coins = hero.findItems()
    # coinIndex is used to iterate the coins array.
    coinIndex = 0
    while coinIndex < len(coins):
        # Get a coin from the coins array using coinIndex
        coin = coins[coinIndex]
        # Collect that coin.
        hero.moveXY(coin.pos.x, coin.pos.y)
        # Increase coinIndex by one.
        coinIndex += 1
