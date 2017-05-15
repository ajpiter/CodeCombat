# Teach your pet to answer questions!

# Luckily, all the answers are "2"
def sayTwo(event):
    # Use pet.say() to answer "2"
    pet.say("2")
    pass

# Use pet.on() to handle "hear" events with sayTwo
pet.on("hear", sayTwo)
# Now relax and watch the show.
hero.say("One plus one is...?")
hero.say("x^3 - 6x^2 + 12x - 8 = 0. What is x...?")
hero.say("How many moons does Mars have...?")
