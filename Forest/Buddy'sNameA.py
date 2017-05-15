# The peasant wants to know Kitty's name.

# Use this function as the handler for "hear" events.
def sayName(event):
    # The pet will say these in order when this function is called.
    pet.say("My name is Kitten.")
    pet.say("But my friends call me Kitty.")
    
# Use pet.on("eventName", functionName) to add an event listener to your pet.
# In this case use "hear" and sayName with pet.on()!
pet.on("hear", sayName)

# You don't need to say anything this time!
# The peasant will do the talking.
