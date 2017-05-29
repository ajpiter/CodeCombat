# Walk through the minefield

# This function returns the number multiplied by the times
def mult(number, times):
    total = 0
    while times > 0:
        total += number
        times -= 1
    return total

# This function returns the number to the exponent power.
def power(number, exponent):
    total = 1
    # Complete the function.
    while exponent > 0:
        total = number * total
        exponent = exponent - 1
   
    return total

# Don't change the following code
# You can find coefficients for the equation on the tower
tower = hero.findFriends()[0]
a = tower.a
b = tower.b
c = tower.c
d = tower.d
x = hero.pos.x

while True:
    # To find the path use a cubic equation
    y = a * power(x, 3) + b * power(x, 2) + c * power(x, 1) + d * power(x, 0)
    hero.moveXY(x, y)
    x = x + 5
