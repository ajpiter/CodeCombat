# The pet should greet the hero and peasant.

# Use this function as a handler for "hear" events:
def sayHello(event):
    # The pet says hello:
    pet.say("Salutations.")

# Use the pet's .on("eventType", functionName) method.
# In this level the pet should run sayHello when "hear"ing something.
pet.on("hear", sayHello)

# Then greet the pet and wait for a response.
hero.say("Hello, Kitty!")
