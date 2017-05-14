# Use different colored flags to perform different tasks.

while True:
    flagGreen = hero.findFlag("green")
    flagBlack = hero.findFlag("black")
    
    # If there's a flagGreen...
    if flagGreen:
        # Build a "fence" at flagGreen's position.
        hero.buildXY("fence", flagGreen.pos.x, flagGreen.pos.y)
        # Pick up the flag!
        hero.pickUpFlag(flagGreen)
    # If there's a flagBlack...
    if flagBlack:
        # Build a "fire-trap" at flagBlack's position.
        hero.buildXY("fire-trap", flagBlack.pos.x, flagBlack.pos.y)
        # Pick up the flag!
        hero.pickUpFlag(flagBlack)
    # Move back to the center.
    hero.moveXY(43, 31)
