# Use a while to loop until you have counted 10 attacks.

attacks = 0
while attacks < 10:
    # Attack the nearest enemy!
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    # Incrementing means to increase by 1.
    # Increment the attacks variable.
    attacks += 1

# When you're done, retreat to the ambush point.
hero.say("I should retreat!") #∆ Don't just stand there blabbering!
hero.moveXY(79, 33)
