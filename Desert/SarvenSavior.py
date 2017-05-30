"""My pet gets left behind everytime :( """

# An ARRAY is a list of items.

# This array is a list of your friends' names.
friendNames = ['Joan', 'Ronan', 'Nikita', 'Augustus']

# Array indices start at 0, not 1!
friendIndex = 0

# Loop over each name in the array.
# The len() function gets the length of the list.
while friendIndex < len(friendNames):
    # Use square brackets to get a name from the array.
    friendName = friendNames[friendIndex]
    
    # Tell your friend to go home.
    # Use + to connect two strings.
    hero.say(friendName + ', go home!')
    
    # Increment friendIndex to get the next name.
    friendIndex += 1
    
# Retreat to the oasis and build a "fence" on the X.
hero.moveXY(22, 29)
hero.buildXY("fence", 30, 30)
