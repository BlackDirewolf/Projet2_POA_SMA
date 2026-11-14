import random
class Joss_strat():
    def __init__(self):
        self.move = 'C'
        self.turn = 0
        self.opponent_prev_move = None

    def play_move(self):
        if(self.turn == 0): 
            self.turn += 1
            return self.move
        elif(random.randint(1,10) == 1):
            self.turn += 1 
            return 'D'
        elif (self.opponent_prev_move is not None):
            self.turn += 1 
            return self.opponent_prev_move
        else:
            self.turn += 1  
            return self.move
        

    def reset(self):
        self.opponent_prev_move = None
        self.turn = 0