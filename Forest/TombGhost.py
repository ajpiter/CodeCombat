# The only exit is blocked by ogres.
# Hide from the skeletons and defeat the ogres one by one.

# This function should attack an enemy and hide.
def hitOrHide(target):
    # If 'target' exists:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Attack 'target'.
        hero.attack(enemy)
        # Then move to the red mark.
        hero.moveXY(32, 17)
    pass

while True:
    enemy = hero.findNearestEnemy()
    hitOrHide(enemy)
