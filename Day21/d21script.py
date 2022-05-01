import time,random,sys

clock = [1,2,3,4,5,6,7,8,9,10]

class Dice100:
    def __init__(self):
        self.value = 1
        self.rolled = 0
    def roll(self):
        res = self.value
        self.update()
        return res
    def update(self):
        self.value += 1
        self.rolled += 1
        if self.value > 100:
            self.value = 1



class Player:
    def __init__(self,pos):
        self.pos = pos
        self.score = 0
    def getposscore(self):
        return clock[self.pos]


def main(p1,p2):
    Dice = Dice100()
    player1 = Player(p1-1)
    player2 = Player(p2-1)
    playerturn = player1
    while player1.score < 1000 and player2.score < 1000:
        rollofturn = sum([Dice.roll(),Dice.roll(),Dice.roll()])
        playerturn.pos = (playerturn.pos + rollofturn) % 10
        playerturn.score += playerturn.getposscore()
        if playerturn == player1:
            playerturn = player2
        else:
            playerturn = player1
    print('Dice Rolled : %s'%(Dice.rolled))
    print('Player 1: %s'%(player1.score))
    print('Player 2: %s'%(player2.score))


p1 = 6-1
p2 = 3-1
DP = {} # game state -> answer for that game state
def count_win(p1, p2, s1, s2):
  # Given that A is at position p1 with score s1, and B is at position p2 with score s2, and A is to move,
  # return (# of universes where player A wins, # of universes where player B wins)
  if s1 >= 21:
    return (1,0)
  if s2 >= 21:
    return (0, 1)
  if (p1, p2, s1, s2) in DP:
    return DP[(p1, p2, s1, s2)]
  ans = (0,0)
  for d1 in [1,2,3]:
    for d2 in [1,2,3]:
      for d3 in [1,2,3]:
        new_p1 = (p1+d1+d2+d3)%10
        new_s1 = s1 + new_p1 + 1

        x1, y1 = count_win(p2, new_p1, s2, new_s1)
        ans = (ans[0]+y1, ans[1]+x1)
  DP[(p1, p2, s1, s2)] = ans
  return ans



if __name__ == "__main__":
    print(count_win(p1,p2,0,0))
