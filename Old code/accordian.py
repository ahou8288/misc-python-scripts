#accordian

import random

deck=[[i2+1,i+1] for i2 in range(4) for i in range(13)]
for card in deck:
    print card

random.shuffle(deck)

#travel along deck looking at each card.
#as soon as a branch is discovered generate it and recursion.
#to test use small deck (4x4?)
