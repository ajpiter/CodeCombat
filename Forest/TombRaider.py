# A forgotten tomb in the forest!
# But the ogres are hot on your heels.
# Break open the tomb, while defending yourself from the munchkins.

# This function should attack an enemy if it exists, otherwise attack the door!
def checkToDefend(target):
    # Check if the target exists
    enemy = hero.findNearestEnemy()
    if enemy:
        # If so, attack the target
        hero.attack(enemy)
    # Use an else to do something if there is no target
    else:
        hero.attack("Door")
        # Otherwise attack the "Door"
    pass

while True:
    enemy = hero.findNearestEnemy()
    checkToDefend(enemy)
