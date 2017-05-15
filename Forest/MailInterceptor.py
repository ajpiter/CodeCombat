# Intercept all ogre messengers from ambush. 

def ambushAttack(target):
    #  Attack the target if it exists and return to the mark.
    # Write the function:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        hero.moveXY(52, 37)
    pass

while True:
    ogre = hero.findNearestEnemy()
    ambushAttack(ogre)
