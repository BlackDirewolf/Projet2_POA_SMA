class All_D_strat():
    def __init__(self):
        self.move = 'D'
        self.opponent_prev_move = None
        
    def play_move(self):
        return self.move

    def reset(self):
        self.opponent_prev_move = None