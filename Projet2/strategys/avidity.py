import random
class Avidity_strat():
    def __init__(self):
        self.move1 = 'C'
        self.move2 = 'D'
        self.avidity = 0.2
        self.pre_move = None
        self.opponent_prev_move = None
        self.nbr_betrayal = 0


    def play_move(self):
        if(self.pre_move is not None):
            if(self.pre_move == 'C' and self.opponent_prev_move == 'C'):
                self.avidity = min(1, self.avidity * 1.1)
            elif(self.pre_move == 'D' and self.opponent_prev_move == 'C'):
                self.avidity = min(1, self.avidity * 1.3)
            elif(self.pre_move == 'D' and self.opponent_prev_move == 'D'):
                self.avidity *= 0.8
                self.nbr_betrayal += 1
            elif(self.pre_move == 'C' and self.opponent_prev_move == 'D'):
                self.avidity *= 0.6
                self.nbr_betrayal += 1

            
            if(self.opponent_prev_move == 'C' and self.nbr_betrayal < 3):
                self.nbr_betrayal = 0

    
        if(self.nbr_betrayal >= 3):
            self.pre_move = 'D'
            return self.move2
        
        elif(random.random() < self.avidity):
            self.pre_move = 'D'
            return self.move2
        else:
            self.pre_move = 'C'
            return self.move1

        

    def reset(self):
        self.avidity = 0.2
        self.pre_move = None
        self.opponent_prev_move = None
        self.nbr_betrayal = 0
