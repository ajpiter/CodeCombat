# Use what you've learned to defeat the ogres.
# Remember: it takes two attacks to defeat an ogre munchkin!
while True:
    hero.moveUp()
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.attack(enemy)
