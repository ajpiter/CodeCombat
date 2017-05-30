# You have one arrow. Make it count!

# This should return the enemy with the most health.
def findStrongestEnemy(enemies):
    strongest = None
    strongestHealth = 0
    enemyIndex = 0
    # While enemyIndex is less than the length of enemies:
    while enemyIndex < len(enemies):
        # Set an enemy variable to enemies[enemyIndex]
        enemy = enemies[enemyIndex]
        # If enemy.health is greater than strongestHealth
        if enemy.health > strongestHealth:
            # Set strongest to enemy
            # Set strongestHealth to enemy.health
            strongest = enemy
            strongestHealth = enemy.health 
        # Increment enemyIndex
        enemyIndex += 1 

    return strongest

enemies = hero.findEnemies()
leader = findStrongestEnemy(enemies)
if leader:
    hero.say(leader)
