# Escape from Death Valley!
# Move by with a zigzag pattern using real modulo functions.

# This function returns a value from 0 to 15:
def mod15(n):
    while n >= 15:
        n -= 15
    return n

# This function should return a value from 0 to 9:
def mod9(n):
    # While n is greater or equal to 9, subtract 9 from n:
    while n >= 9: 
        n = n-9
    return n

# Don't change the following code:
while True:
    time = hero.time
    if time < 30:
        y = 10 + 3 * mod15(time)
    else:
        y = 20 + 3 * mod9(time)
    x = 10 + time
    hero.moveXY(x, y)
