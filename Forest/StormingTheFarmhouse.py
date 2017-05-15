# Soldiers will slowly arrive, but the ogres will overwhelm them.
# A basic attack loop isn't going to be enough to keep you alive.
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag:
        hero.say("Maybe I should do something with that flag?")
        hero.pickUpFlag(flag)
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        else:
            if enemy:
                hero.attack(enemy)
    else:
        hero.say("I'm bored.")
