from strategys.all_D import All_D_strat
from strategys.random_strat import Random_strat
from strategys.tit_for_tat import Tit_for_tat_strat
from strategys.tester import Tester_strat
from strategys.joss import Joss_strat
from strategys.avidity import Avidity_strat
from strategys.pavlov import Pavlov_strat

class Duelist():
    def __init__(self,name,strategy_name):
        self.name = name
        self.victory = 0
        self.lose = 0
        self.draw = 0
        self.score = 0
        self.final_score = 0
        if(strategy_name == 'all_D'):
            self.strategy = All_D_strat()
        elif(strategy_name == 'random'):
            self.strategy = Random_strat()
        elif(strategy_name == 'tit_for_tat'):
            self.strategy = Tit_for_tat_strat()
        elif(strategy_name == 'tester'):
            self.strategy = Tester_strat()
        elif(strategy_name == 'joss'):
            self.strategy = Joss_strat()
        elif(strategy_name == 'avidity'):
            self.strategy = Avidity_strat()
        elif(strategy_name == 'pavlov'):
            self.strategy = Pavlov_strat()
        else:
            print("Aucune stratégie n'a était reconnu")

            
    def play_move(self):
        return self.strategy.play_move()

    
    def clear(self):
        self.score = 0
        self.strategy.reset()


