import sys
import random
from duelist import Duelist
from tournament_report import Tournament_report

def table_score(move1,move2):
    if(move1 == 'C' and move2 == 'C'):
        return [3,'C'],[3,'C']
    elif(move1 == 'D' and move2 == 'D'):
        return [2,'D'],[2,'D']
    elif(move1 == 'C' and move2 == 'D'):
            return [0,'D'],[5,'C']
    elif(move1 == 'D' and move2 == 'C'):
            return [5,'C'],[0,'D']
    else:
         print("Erreur dans les coups")

def game(duelist1,duelist2):
    result1,result2 = table_score(duelist1.play_move(),duelist2.play_move())
    duelist1.score += result1[0]
    duelist2.score += result2[0]

    duelist1.strategy.opponent_prev_move = result1[1]
    duelist2.strategy.opponent_prev_move = result2[1]


def switch_duelist(duelists,i):
    temp  = duelists[i]
    duelists[i] = duelists[i+1]
    duelists[i+1] = temp
    return duelists
     
def ranking(duelists):
    i = 0
    while(i < len(duelists)-1):
        if(duelists[i].final_score < duelists[i+1].final_score):
            switch_duelist(duelists,i)
            i=0
        elif(duelists[i].final_score == duelists[i+1].final_score):
            if(duelists[i].victory < duelists[i+1].victory):
                switch_duelist(duelists,i)
                i = 0
            else: i += 1
        else: i+=1
    print()
    for i in range(len(duelists)):
         print(f"{duelists[i].name} termine en position {i+1} avec un score final de {duelists[i].final_score}, {duelists[i].victory} victoires, {duelists[i].draw} égalités, et {duelists[i].lose} défaites")
         print()
            

          


     
def tournament(duelists, nbr_match, nbr_turn, report):
    phase = 1
    for duelist in duelists:
        for i in range(phase, len(duelists)):
            opponent = duelists[i]
            victory1 = victory2 = draws = 0
            total1 = total2 = 0
            for j in range(nbr_match):
                for k in range(nbr_turn):
                    game(duelist, opponent)
                if(duelist.score > opponent.score):
                    duelist.victory += 1
                    opponent.lose += 1
                    victory1 += 1
                elif (duelist.score < opponent.score):
                    duelist.lose += 1
                    opponent.victory += 1
                    victory2 += 1
                else:
                    duelist.draw += 1
                    opponent.draw += 1
                    draws += 1
                total1 += duelist.score
                total2 += opponent.score
                duelist.final_score += duelist.score
                opponent.final_score += opponent.score
                duelist.clear()
                opponent.clear()
            report.add_encounter(duelist, opponent, victory1, victory2, draws, total1, total2)

        phase += 1
        
        
                             
                        
                     

def main(argv):
    random.seed(42)

    duelist1 = Duelist("all_D","all_D")
    duelist2 = Duelist("random","random")
    duelist3 = Duelist("tit_for_tat","tit_for_tat")
    duelist4 = Duelist("tester","tester")
    duelist5 = Duelist("joss","joss")
    duelist6 = Duelist("avidity","avidity")
    duelist7 = Duelist("pavlov","pavlov")


  
    report = Tournament_report()
    tournament([duelist1,duelist2,duelist3,duelist4,duelist5,duelist6,duelist7],5,200,report)
    ranking([duelist1,duelist2,duelist3,duelist4,duelist5,duelist6,duelist7])
    report.display_report()

    
    

    return 0



if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
