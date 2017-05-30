"""Watch your indentions"""
# Use while loops to pick out the ogre

while True:
    enemies = hero.findEnemies()
    enemyIndex = 0
    # Wrap this logic in a while loop to attack all enemies.
    # Find the array's length with:  len(enemies)
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
    # "!=" means "not equal to."
        if enemy.type != "sand-yak":
            # While the enemy's health is greater than 0, attack it!
            while enemy.health > 0:
                hero.attack(enemy)
        enemyIndex += 1
    pass
    # Between waves, move back to the center.
    hero.moveXY(40, 32)
