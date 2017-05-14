# Don't step on fire traps!
hero.moveUp();
hero.moveRight(2);
hero.moveUp()
# ∆ Remove this line.
# Some ogres are stronger than others!
# Only defeat the ogres you can easily handle.
# Attack doors by name and ogres with findNearestEnemy.
hero.attack("Door B")
hero.moveUp(2)
enemy = hero.findNearestEnemy()
hero.attack(enemy)
hero.attack(enemy)
hero.moveDown(2)
hero.moveRight(4)
enemy = hero.findNearestEnemy()
hero.attack(enemy)
hero.attack(enemy)
enemy = hero.findNearestEnemy()
hero.attack(enemy)
hero.attack(enemy)
hero.moveUp(3)
hero.moveRight()
# When you're done, escape (move to the x-mark).
hero.moveDown(4)
hero.moveLeft(3)
hero.moveDown()
hero.moveLeft(2)
