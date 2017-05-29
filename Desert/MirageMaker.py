# Lure the ogres into an ambush!
# While your gold is less than 25, collect coins.
totalGold = 0 
while hero.gold <25:
    coin = hero.findNearestItem()
    if coin:
        hero.moveXY(coin.pos.x, coin.pos.y)
        totalGold = totalGold + coin.value
 

hero.buildXY("decoy", 72, 69)

# After the while loop, build a "decoy" at the white X.
# While your health equals maxHealth, say insults
while hero.health == hero.maxHealth:
    hero.say("insults")

# Then move back to the red X.
hero.moveXY(22, 16)
