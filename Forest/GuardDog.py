# You can't help the peasants across the river.
# But, your pet can!
# Teach your wolf to be a guard dog.

def onSpawn(event):
    while True:
        # Pets can find enemies, too.
        enemy = pet.findNearestEnemy()
        # If there is an enemy:
        if enemy:
            
            # Then have the pet say something:
            pet.say("Enemy")

pet.on("spawn", onSpawn);
