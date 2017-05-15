# We need to know the name of our new pet.

# Use this function as a handler for "hear" events on pet.
def onHear(event):
    # Don't change this function.
    pet.say("Meow Purr Meow")
    pet.say("Purr Purr")
    pet.say("Meow")
    pet.say("Meow")
    pet.say("Meow Purr Meow Meow")

# Use the pet.on(eventType, eventHandler) method
# Assign the onHear function to handle "hear" events.
pet.on("hear", onHear)

# It must be after "pet.on".
hero.say("What's you name, buddy?")
hero.say("Could you repeat it?")
