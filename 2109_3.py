import random
class Game():
    def __init__(self):
       pass

    def play(self):
        p = random.randrange(0, 10)
        new_n1 = self.n1 + p
        new_n2 = self.n2 + u
        new_n3 = self.n3 + k
        return new_n1, new_n2, new_n3

    def play2(self, cards):
        cable_card = random.randrange(10)
        winners = []
        i = 0
        for card in cards:
            if(card + cable_card) % 2 == 0:
                winners.append(i)
            i += 1
        if len(winners) > 0:
            print('The winner is ', winners)
        else:
            print('Everyone has lost')

f = Game()
i = 0
randomlist = []
for i in range (0, 10):
    n = random.randint(1, 30)
    randomlist.append(n)
while i < 13:
    f.play2(randomlist)
    i += 1
