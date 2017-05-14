while True:
    hero.moveRight()
    hero.moveUp()
    pass
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.attack(enemy)
    hero.moveRight()
    hero.moveDown()
    hero.moveDown()
    hero.moveUp()
