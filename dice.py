import random
import sys

def rollDice(sides):
    return random.choice(range(1,sides+1))



def countDoubles(rolls, dWhat):
    if rolls == 0:
        return 0

    else:
        d1 = rollDice(dWhat)
        d2 = rollDice(dWhat)

        if d1 == d2:
            return 1 + countDoubles(rolls-1, dWhat)

        else:
            return countDoubles(rolls-1, dWhat)

sys.setrecursionlimit(15000)
print(countDoubles(1000, 6))
