# Your pet can use pet.moveXY()

def onSpawn(event):
    while True:
        # First, move to the left X mark:
        pet.moveXY(9, 24)
        # Next, move to the top X mark:
        pet.moveXY(30, 43)
        # Move your pet to the right X mark:
        pet.moveXY(51,24)
        # Move your pet to the bottom X mark:
        pet.moveXY(30,5)

# Use pet.on() to handle the "spawn" event with onSpawn
pet.on("spawn", onSpawn)

# Cheer on your pet!
# Don't remove the commands below.
while True:
    hero.say("Good dog!")
    hero.say("You can do it!")
    hero.say("Run Run Run!")
    hero.say("Almost!")
    hero.say("One more lap!")
