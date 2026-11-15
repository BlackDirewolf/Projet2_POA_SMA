class Pavlov_strat():
    def __init__(self):
        self.move1 = 'C'
        self.move2 = 'D'
        self.prev_move = None
        self.opponent_prev_move = None

    def play_move(self):
        if(self.prev_move is None):
            self.prev_move = self.move1
            return self.move1
        elif(self.prev_move == 'C' and self.opponent_prev_move == 'C'):
            self.prev_move = self.move1
            return self.move1
        elif(self.prev_move == 'D' and self.opponent_prev_move == 'C'):
            self.prev_move = self.move2
            return self.move2
        elif(self.prev_move == 'D' and self.opponent_prev_move == 'D'):
            self.prev_move = self.move1
            return self.move1
        elif(self.prev_move == 'C' and self.opponent_prev_move == 'D'):
            self.prev_move = self.move2
            return self.move2

    def reset(self):
        self.prev_move = None
        self.opponent_prev_move = None
        