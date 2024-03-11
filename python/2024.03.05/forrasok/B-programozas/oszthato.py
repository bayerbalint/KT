print('1. feladat')
kiiras = ''
for i in range(50,197):
    if i % 7 == 0 and i % 4 == 0:
        kiiras += f'{i},'
        
print(kiiras[:len(kiiras)-1],'\n')