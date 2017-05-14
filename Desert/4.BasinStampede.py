# Keep moving right, but adjust up and down as you go.

while True:
    enemy = hero.findNearestEnemy()
    xPos = hero.pos.x + 5
    yPos = 17
    if enemy:
        # Adjust y up or down to get away from yaks.
        if enemy.pos.y > hero.pos.y:
            # If the Yak is above you, subtract 3 from yPos
            yPos = yPos - 3
            pass
        elif enemy.pos.y < hero.pos.y:
            # If the Yak is below you, add 3 to yPos.
            yPos = yPos +3
            pass
    hero.moveXY(xPos, yPos)
