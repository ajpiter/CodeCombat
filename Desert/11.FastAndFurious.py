# Use an event handler so pet and hero will both run!

def petMove():
    pet.moveXY(50, 21)

# Use pet.on("spawn", petMove) instead of petMove().
# This way your hero and pet will run at the same time.
# ∆ Replace this with pet.on("spawn", petMove)
pet.on("spawn", petMove)
hero.moveXY(50, 12)
