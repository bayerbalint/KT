def szorzas_rekurzio(szorzo,szorzando):
    if szorzando == 0:
        return 0
    else: return szorzas_rekurzio(szorzo, szorzando-1) + szorzo


def hatvanyozas_rekurzio(alap,kitevo):
    if kitevo == 0:
        return 1
    else:
        return szorzas_rekurzio(hatvanyozas_rekurzio(alap,kitevo-1),alap)

# főprogram

print(szorzas_rekurzio(4,5))
print(hatvanyozas_rekurzio(3,983))
