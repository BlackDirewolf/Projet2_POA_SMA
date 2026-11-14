class Tester_strat():
    def __init__(self):
        self.move1 = 'C'
        self.move2 = 'D'
        self.opponent_prev_move = None
        self.turn = 0
        self.vengeance_phase = False

    def play_move(self):
        if(self.turn == 0):
            self.turn += 1
            return self.move2
        elif(self.vengeance_phase):
            self.turn += 1
            return self.opponent_prev_move
        elif(self.opponent_prev_move == 'D'):
            self.vengeance_phase = True
            self.turn += 1
            return self.move2
        elif(self.turn % 3 == 0):
            self.turn += 1
            return self.move2
        else:
            self.turn += 1 
            return self.move1

    def reset(self):
        self.opponent_prev_move = None
        self.vengeance_phase = False
        self.turn = 0
