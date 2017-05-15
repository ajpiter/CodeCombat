# The ogres are holed up in their camp
# Break through their defenses with a calculated strike!

hero.moveXY(55, 14)
hero.moveXY(92, 9)

# Build a "fire-trap" on the red X.
hero.buildXY("fire-trap", 94, 19)
# Move back to the wooden X to avoid the blast.
hero.moveXY(70, 7)
# Wait for the peon to investigate the shiny fire trap.
# Enter the camp and lay fire traps on each red X.
hero.buildXY("fire-trap", 60, 62)
hero.buildXY("fire-trap", 90, 53)
# Use the say method to tell your troops to "retreat".
hero.say("retreat")
# Flee back to the far left wooden X rally point.
hero.moveXY(11, 28)
