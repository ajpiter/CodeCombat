# Figure out which direction the ogres are coming from.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Left: enemy.pos.x is less than hero.pos.x
        isLeft = hero.pos.x  > enemy.pos.x
        # Above: enemy.pos.y is greater than hero.pos.y
        isAbove = hero.pos.y < enemy.pos.y
        # Right: enemy.pos.x is greater than hero.pos.x
        isRight = enemy.pos.x > hero.pos.x
        # Below: enemy.pos.y is less than hero.pos.y
        isBelow = enemy.pos.y < hero.pos.y
        # If enemy isAbove and isLeft:
        # buildXY() a "fire-trap" at the X mark.
        if isLeft and isAbove:
            hero.buildXY("fire-trap", 40 - 20, 34 + 17)
        # If enemy isAbove and isRight:
        # buildXY() a "fire-trap" at the X mark.
        if isAbove and isRight:
            hero.buildXY("fire-trap", 60, 51)
        # If enemy isBelow and isLeft:
        # buildXY() a "fire-trap" at the X mark.
        if isBelow and isLeft:
            hero.buildXY("fire-trap", 20, 17)
        # If enemy isBelow and isRight:
        # buildXY() a "fire-trap" at the X mark.
        if isBelow and isRight:
            hero.buildXY("fire-trap", 60, 17)
        hero.moveXY(40, 34)
    else:
        hero.moveXY(40, 34)
