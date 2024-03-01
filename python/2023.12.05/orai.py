import math

class haromszog: # ez az ősosztály
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def szabalyos(self):
        if self.a == self.b == self.c:
            return True
        return False
    
    def egyenloszaru(self):
        if self.a == self.b or self.b == self.c or self.a == self.c:
            return True
        return False
    
class szogek(haromszog):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def derekszogu(self):
        an = math.pow(self.a,2)
        bn = math.pow(self.b,2)
        cn = math.pow(self.c,2); print(an,bn,cn)
        if an + bn == cn or an + cn == bn or bn + cn == an:
            return True
        return False
    
    def hegyesszogu(self):
        an = math.pow(self.a,2)
        bn = math.pow(self.b,2)
        cn = math.pow(self.c,2); print(an,bn,cn)
        if an + bn > cn and an + cn > bn and bn + cn > an:
            return True
        return False
    
    def tompaszogu(self):
        if not self.derekszogu() and not self.hegyesszogu():
            return True
        return False
    
# Főprogram:
h = szogek(10,10,18)
print("Szabályos: ",h.szabalyos())
print("Egyenlőszárú: ",h.egyenloszaru())
print("Derékszögű: ",h.derekszogu())
print("Hegyesszögű: ",h.hegyesszogu())
print("Tompaszögű: ",h.tompaszogu())
