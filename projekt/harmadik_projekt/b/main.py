class Main:
    def __init__(self):
        pass

    def Szorzas(self, szorzo, szorzando):
        if szorzando == 0:
            return 0
        return self.Szorzas(szorzo, szorzando-1) + szorzo
    
    def Hatvanyozas(self, alap, kitevo):
        if kitevo < 0:
            return self.Hatvanyozas(alap, kitevo+1)*(1/alap)
        if kitevo == 0:
            return 1
        return self.Hatvanyozas(alap,kitevo-1)*alap # vagy self.Szorzas(self.Hatvanyozas(alap,kitevo-1),alap)
    
    def Euler(self, n):
        if n == 0: 
            return 1
        return self.Hatvanyozas(1 + 1/n,n) # csak így tudtam rekurzívan
    
    def Fibonacci(self, n):
        if n <= 1:
            return n
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)
    
    def Binomialis(self, n, k):
        if k == 0 or k == n:
            return 1
        return self.Binomialis(n-1,k-1) + self.Binomialis(n-1,k)
    
    def SzHE(self, *kwargs):
        print(f'{kwargs[0].__name__}: {kwargs[0](*kwargs[1:])}')

    def Fibon_ki(self, n):
        print(n)
        for i in range(n):
            print(self.Fibonacci(i))



main = Main()

print(main.Fibon_ki(10))
print(main.Fibonacci(10))