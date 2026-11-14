import random
class Random_strat():
    def __init__(self):
        self.move1 = 'C'
        self.move2 = 'D'
        self.opponent_prev_move = None


    def play_move(self):
        coup = random.randint(1,2)
        if(coup == 1):
            return self.move1
        else: return self.move2

    def reset(self):
        self.opponent_prev_move = None