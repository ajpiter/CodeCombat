# Move to the right.

# Complete this function:
def onSpawn():
    pass
    # Inside a while-true loop:
    while True:
        # Use hero.findNearestItem()
        item = hero.findNearestItem()
        # If there's an item:
        if item:
            # Use pet.fetch(item) to fetch the item.
            pet.fetch(item)
        else:
            hero.moveXY(76, 35)
    # Use pet.on() to assign onSpawn to the "spawn" event
pet.on("spawn", onSpawn)
hero.moveXY(78, 35)
