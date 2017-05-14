# Lead the peasants and healer through the minefield.

while True:
    coin = hero.findNearestItem()
    healingThreshold = hero.maxHealth / 2
    # Check to see if you are critically injured.
    if hero.health < healingThreshold:
        # Move left 10m.
        x = hero.pos.x -10 
        y = hero.pos.y 
        hero.moveXY(x, y)
        # Ask for a heal.
        hero.say("Can I get a heal?")
        pass
    # Else, move to the next coin.
    elif coin:
        hero.moveXY(coin.pos.x, coin.pos.y)
