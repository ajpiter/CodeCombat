# You now have a pet!

def speak(event):
    # Your pet should respond with pet.say()
    pet.say("meow")
    pass

# This tells your pet to run the speak() function when she hears something
pet.on("hear", speak)

# Talk to your pet!
hero.say("Hello Kitty")
