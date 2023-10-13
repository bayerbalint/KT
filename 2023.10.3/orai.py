class Osztaly:
    valtozo = 1 # public változó
    _valtozo = 2 # protected változó
    __valtozo = 3 # private változó
    def __init__(self, valtozo):
        self.valtozo = valtozo # ez a sor override a változó attributumhoz!!
        
    def metodus(self):
        #self.valtozo = 'Anyu'
        #return valtozo
        return self.valtozo

    def privatProba(self):
        return self.__valtozo * 10


class Orokos(Osztaly):
    pass
    # def __init__(self, vvv):
    #     self.V = vvv
    def nyomtat(self):
        # return self.V
        #self.A = self.__valtozo # erre hibát kapunk!!!
        return self.valtozo
        #return self.A
    

Or = Orokos('ˇˇˇˇ')
print(Or.valtozo)
print(Or._valtozo)
print(Or.metodus())
print(Or.nyomtat())
print(Or.privatProba())

# Oszt = Osztaly('hahó')
# print(Oszt.valtozo)
# print(Oszt._valtozo)
# # print(Oszt.__valtozo)
#print(Oszt.metodus())
