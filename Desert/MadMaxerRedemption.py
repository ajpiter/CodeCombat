# You can't reach your friends to defend them!
# Tell them to go home where the archer can help.

while True:
    weakestFriend = None
    leastHealth = 9999
    friendIndex = 0
    # Find which friend has the lowest health.
    friends = hero.findFriends()
    for friend in friends:
        health = friend.health 
        if leastHealth > friend.health and friend.type == 'peasant':
            weakestFriend = friend 
            leastHealth = friend.health 
    # Tell the weakest friends to go home first.
    if weakestFriend:
        hero.say('Hey ' + weakestFriend.id + ', go home!')
