class Tit_for_tat_strat():
    def __init__(self):
        self.move = 'C'
        self.opponent_prev_move = None

    def play_move(self):
        if (self.opponent_prev_move is not None):
            return self.opponent_prev_move
        else: return self.move 

    def reset(self):
        self.opponent_prev_move = None