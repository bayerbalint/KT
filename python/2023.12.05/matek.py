class hatvany:
    def __init__(self, alap=int, kitevo=int):
        self.alap = alap # nem negatív
        self.kitevo = kitevo # bármilyen
        if self.kitevo % 0.5 != 0:
            self.kerekites()

    def kerekites(self):
        self.kitevo = round(self.kitevo)
        print(self.kitevo)

    def hatvanyozas(self):
        if self.kitevo == 0: return 1
        return hatvany(self.alap,self.kitevo-1).hatvanyozas()*self.alap

class gyok(hatvany):
    pass

print(hatvany(3,3.5).hatvanyozas())