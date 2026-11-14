class Tournament_report:
    def __init__(self):
        self.encounters = []

    def add_encounter(self, duelist1, duelist2, wins1, wins2, draws, total1, total2):
        self.encounters.append((duelist1.name, duelist2.name, wins1, wins2, draws, total1, total2))

    def display_report(self):
        width = max(len(f"{e[0]} vs {e[1]}") for e in self.encounters)
        header = f"{'Rencontre':<{width}} | {'Scores totaux':^15} | {'Victoires':^15}"
        print(header)
        print("-" * len(header))
        for name1, name2, wins1, wins2, draws, total1, total2 in self.encounters:
            match = f"{name1} vs {name2}"
            scores = f"{total1} - {total2}"
            results = f"{wins1} / {draws} / {wins2}"
            print(f"{match:<{width}} | {scores:^15} | {results:^15}")
        print()
        print("Victoires : joueur 1 / égalités / joueur 2\n")