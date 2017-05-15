while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Replace this with your own code.
        # Find the distance to the enemy with distanceTo.
        if hero.distanceTo(enemy) <5: 
            if hero.isReady("cleave"):
                hero.cleave(enemy)
            else:
                hero.attack(enemy)
        # If the distance is less than 5 meters...
        
            # ... if "cleave" is ready, cleave!
            
            # ... else, just attack.
