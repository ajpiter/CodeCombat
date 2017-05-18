# Get three keys and free the paladin.

def onSpawn(event):
    # The pet should find and fetch three keys.
    # You need items with the next types:
    # "bronze-key", "silver-key" and "gold-key".
    bronzekey = pet.findNearestByType('bronze-key')
    silverkey = pet.findNearestByType('silver-key')
    goldkey = pet.findNearestByType('gold-key')
    if bronzekey or silverkey or goldkey:
        pet.fetch(bronzekey)
        pet.fetch(silverkey)
        pet.fetch(goldkey)

pet.on("spawn", onSpawn)

while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.team == "ogres":
        hero.attack(enemy)
    if hero.health < 300:
        # You can use pets in the main thread too.
        potion = pet.findNearestByType("potion")
        if potion:
            hero.moveXY(potion.pos.x, potion.pos.y)
