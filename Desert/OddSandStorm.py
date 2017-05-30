# This array contains friends and ogres.
# The even elements are ogres, but the odds are friends.
everybody = ['Yetu', 'Tabitha', 'Rasha', 'Max', 'Yazul',  'Todd']
enemyIndex = 0

while enemyIndex < len(everybody):
    # Use square brackets to get the ogre name from the array.
    ogreName = everybody[enemyIndex]
    # Attack using the variable holding the ogre name.
    hero.attack(ogreName)
    # Increment by 2 to skip over friends.
    enemyIndex += 2

# After defeating ogres, move to the oasis.
hero.moveXY(35, 53)
