import random

print('2. feladat')
def felhasznalonev(vezeteknev, keresztnev):
    return f'Felhasználónév: {vezeteknev.upper()[:3]}_{keresztnev[len(keresztnev)-2:len(keresztnev)]}{random.randint(10,99)}'
print(felhasznalonev(input('Kérem adja meg a vezetéknevét:\n'), input('Kérem adja meg a keresztnevét:\n')),'\n')