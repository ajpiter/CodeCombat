# Your pet should run back and forth on the X marks.
# The hero should cheer the whole time!

# Write the event function onSpawn for the pet.
# This function should make the wolf run back and forth:
# First, run to the right mark, then the left one:
def onSpawn(event): 
    while True:
        pet.moveXY(48, 8)
        pet.moveXY(12, 8)

pet.on("spawn", onSpawn)
# Cheer up your pet. Don't remove this:
while True:
    hero.say("Run!!!")
    hero.say("Faster!")
