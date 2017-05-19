""" The power of your sword and the speed of your boots makes all the difference. """

# Ogres are attacking a nearby outpost!
# Command the hero to defend the tiny settlement.
# Time your patrol with a watch so no ogres can get through.

while True:
    polarPos = hero.time / 4
    # Number between 20 and 60.
    xPos = 40 + Math.cos(polarPos) * 20
    # Number between 14 and 54.
    yPos = 34 + Math.sin(polarPos) * 20
    hero.moveXY(xPos, yPos)
    # Check for ogres and defeat them!
    # Make sure to attack while their health is above 0.
    enemy = hero.findNearestEnemy()
    if enemy: 
        if hero.canCast("chain-lightning", enemy):
            hero.cast("chain-lightning", enemy)
        else:
            hero.attack(enemy)
