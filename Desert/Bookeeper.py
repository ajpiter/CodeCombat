""" If you are running into problems on this level, watch what Naria is saying when you run the code. Does the amount of gold collected match to what you are telling Naria? If not modify the code based on the items you have equiped and the commands they provide."""

# Fight enemies for 15 seconds.
# Keep count whenever an enemy is defeated.
defeated = 0
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        if enemy.health <= 0:
            defeated += 1
    if hero.time > 15:
        break

# Tell Naria how many enemies you defeated.
hero.moveXY(59, 33)
hero.say(defeated)

# Collect coins until the clock reaches 30 seconds.
while True:
    coin = hero.findNearestItem()
    if coin:
        hero.moveXY(coin.pos.x, coin.pos.y)
    if hero.time >30: 
        break

# Tell Naria how much gold you collected.
hero.moveXY(59, 33)
hero.say(hero.gold)

# Fight enemies until the clock reaches 45 seconds.
# Remember to reset the count of defeated enemies!
defeated = 0 
while True:
    enemy = hero.findNearestEnemy()
    if enemy: 
        hero.attack(enemy)
        if enemy.health <= 0:
            defeated = defeated + 1
    if hero.time > 45:
        break
# Tell Naria how many enemies you defeated.
hero.moveXY(59, 33)
hero.say(defeated)
