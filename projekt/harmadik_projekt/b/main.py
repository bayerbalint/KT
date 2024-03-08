import inspect
import webbrowser

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
        return (1+1/n)**n - self.Euler(n-1) # Kiírásnál hozzáadom az egyel kisebb elem értékét
        
    
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
        for i in range(n):
            print(self.Fibonacci(i))

    def Binom_ki(self, n):
        k = 0
        while k < n+1:
            print(self.Binomialis(n,k), end=' ')
            k+=1

main = Main()

fuggvenyek = {'sz':[main.Szorzas, 'Kérem a szorzót: ', 'Kérem a szorzandót: '], 'h':[main.Hatvanyozas, 'Kérem a hatvány alapot: ', 'Kérem a kitevőt: '], 'E':[main.Euler, 'Kérem a sorozat elemének sorszámát: '], 'F':[main.Fibonacci, 'Kérem a sorozat hosszát: '], 'B':[main.Binomialis, 'Kérem a fokszámot: ']}

fut = True
while fut:
    tevekenyseg = input('Mit szeretne tenni? \nFüggvények használata: h \nFüggvények megtekintése: m \nWeboldal megtekintése: w\nKilépés: e\n')
    if tevekenyseg == 'h':
        fuggveny = input('\nMelyik függvényt szeretné használni? (sz, h, E, F, B): ')
        if fuggveny in fuggvenyek.keys():
            if fuggveny == 'sz' or fuggveny == 'h':
                print(f'Eredmény: {fuggvenyek[fuggveny][0](int(input(fuggvenyek[fuggveny][1])),int(input(fuggvenyek[fuggveny][2])))}')
            elif fuggveny == 'E':
                adat = int(input(fuggvenyek[fuggveny][1]))
                print(f'Eredmény: {fuggvenyek[fuggveny][0](adat)+fuggvenyek[fuggveny][0](adat-1)}')
            elif fuggveny == 'F':
                n = int(input(fuggvenyek[fuggveny][1]))
                print('Eredmény:')
                for i in range(n):
                    print(fuggvenyek[fuggveny][0](i))
            elif fuggveny == 'B':
                m = int(input(fuggvenyek[fuggveny][1]))
                print('Eredmény:')
                k = 0
                while k < m + 1:
                    print(fuggvenyek[fuggveny][0](m, k), end=' ')
                    k+=1
        print('\n')
    elif tevekenyseg == 'm': # Jónak tűnik
        fuggveny = input('\nMelyik függvényt szeretné megtekinteni? (sz, h, E, F, B): ')
        if fuggveny in fuggvenyek.keys():
            print(f'\nA(z) "{fuggvenyek[fuggveny][0].__name__}" függvény source kódja:\n',inspect.getsource(fuggvenyek[fuggveny][0]))
    elif tevekenyseg == 'w':
        webbrowser.open('file:///H:/ikt/harmadik_projekt/b/index.html')
    elif tevekenyseg == 'e':
        fut = False