# alap rekurziok
# Fibonacci sorozat. a1 = 0, a2 = 1, an = an-2 + an-1
def Fibonacci(n): # n - hanyadik fibonacci számot keressük
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        k = Fibonacci(n-1) + Fibonacci(n-2)
        return k

# főprogram
N = int(input('Hanyadik Fibonacci számot keressük? '))
print(Fibonacci(N-1))

# F(n) = |n = 0, akkor 0
#        |n = 1, akkor 1
#        |n>1 akkor F(n-1) + F(n-2)

# Algoritmus Fibonacci(egész: n): egész
# Algoritmus kezdete
#   Ha n = 0 akkor Fibonacci = 0
#   Különben Ha n = 1 akkor Fibonacci = 1
#   Különben Fibonacci = Fibonacc(n-1) + Fibonacci(n-2)
#   Elágazás vége
# Algoritmus vége

#______________________________________________________________________________________________________________________________

# FAKTORIÁLIS
# n! = n*(n-1)*n(n-2)*...*1
# Definíció szerint 0! = 1

# Fakt(n) =  |n = 0 akkor 1
#            |n > 0 akkor n*Fakt(n-1)

# Algoritmus Fakt(egész:n): egész
# Algoritmus kezdete
#   Ha n = 0 akkor Fakt = 1
#   Különben Fakt = n*Fakt(n-1)
# Algoritmus vége

def Faktorialis(n):
    if n == 0: return 1
    f = Faktorialis(n-1)*n
    return f

F = int(input("Fakt: "))
print(Faktorialis(F))


#________________________________________________________________________________________________________________________________

# Binaris valto

# Bin(n) = |n = 0, akkor üres string
#          |n > 0, akkor Bin(csonk(n % 2)) + (n % 2) 



def binaris_valtas(n):
    if n == 0:
        return ""
    return binaris_valtas(n//2) + str(n % 2)
    #math.trunc(szam/2)
    

szam = int(input('Kérek egy számot! '))
# print(f"rekurzivan: {bin(szam)[2:]}")
print(binaris_valtas(szam))

#__________________________________________________________________________________________________________________________________

# (a+b)^0                     1
# (a+b)^1                    1 1
# (a+b)^2                   1 2 1
# (a+b)^3            n-1   1 3 3 1
# (a3B)^4            n    1 4 6 4 1

# Binomiális eggyüthatók

# Binom(k,n) =  |k=0, vagy k=n, akkor 1
#               |0<k<n, akkor Binom(k-1,n-1) + Binom(k,n-1)
# 
# Algoritmus Binomialis(egész:k, egész:n): egész
# Algoritmus kezdete
#   Ha k = 0 vagy k = n akkor Binominalis = 1
#   Különben Binominalis = Binominalis(k-1,n-1) + Binominalis(k,n-1)
#   elágazás vége
# Algoritmus vége


def Binom(k,n):
    if k == 0 or k == n: return 1
    return Binom(k-1,n-1) + Binom(k,n-1)

M = int(input("kérem a fokszámot! ")) 
K = 0
while K < M + 1:
    print(Binom(K,M), end=" ")
    K += 1

# HF:
# 1. A Fibonacci solrozatot oldd meg NEM rekurív módon, ciklus(ok) használatával
# 2. A Binomiális együtthatók feladatot dolgozd át úgy, hogy a változók is ki legyenek írva!
# (a+b)^3 = 1a^3b^0 + 3a^2b^1 + 3a^1b^2 + 1a^0b^3


def Fibon(n):
    e = 0
    m = 1
    u = 0
    if n <= 1: return n
    for i in range(2,n):
        u = e + m
        e = m
        m = u
    return u

L = int(input("Hanyadik Fibonacci számot keressük? "))
print(f"\n{Fibon(L)}")
