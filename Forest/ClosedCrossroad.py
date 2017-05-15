# Only build if you see an enemy.

# The function defines THREE parameters.
def maybeBuildSomething(buildType, x, y):
    # Move to the position specified by x and y parameters.
    hero.moveXY(x, y)
    # Find the nearest enemy.
    enemy = hero.findNearestEnemy()
    
    # If there is an enemy
    if enemy:
        # then use buildXY with buildType, x, and y
        hero.buildXY(buildType, x, y)
    pass
    
while True:
    # Call maybeBuildSomething with "fire-trap" and the coordinates of the bottom X.
    maybeBuildSomething("fire-trap", 40, 20)
    # Call maybeBuildSomething, with "fence" at the left X!
    maybeBuildSomething("fence", 26, 34)
    # Call maybeBuildSomething with "fire-trap" at the top X!
    maybeBuildSomething("fire-trap", 40, 50)
    # Call maybeBuildSomething with "fence" at the right X!
    maybeBuildSomething("fence", 54, 34)
