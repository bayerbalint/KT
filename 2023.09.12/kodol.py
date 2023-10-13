fajl =  open('Vtabla.dat','r',encoding='utf-8')
tarolo = []
for adat in fajl:
    tarolo.append(adat.strip())

class Main:

    def __init__(self):
        # bekérem és átalakítom a nyílt szöveget
        self.nyilt_szoveg = input('Kérek egy szöveget! (min:1, max:255 karakter) ')
        self.atalakitott_szoveg = ''
        self.nyilt_szoveg = self.vizsgal(self.nyilt_szoveg)
        self.atalakitott_szoveg = self.atalakit(self.atalakitott_szoveg)
        print(self.atalakitott_szoveg)

        # bekérem a kulcsszót
        self.kulcsszo = input('Kérek egy kulcsszót! (min:1, max:5 karakter) ')
        self.kulcsszo = self.vizsgal(self.kulcsszo)
        self.kulcsszo = self.kulcsszo.upper()

        # minden betűt az "atalkitott_szoveg"-ből és a "kulcsszo"-ból külön-külön berakok egy-egy listába
        self.szoveg_lista = []
        self.kulcsszo_lista = []
        # átalakítom a "kulcsszo_lista"-t, hogy olyan hosszú legyen, mint a "szoveg_lista"
        self.kulcsszoalakitas()
        print(self.szoveg_lista)
        print(self.kulcsszo_lista)
        # átkódolom a "szoveg_lista" és a "kulcsszo_lista" alapján a szöveget
        self.kodolt_szoveg = ''
        self.kodolas()
        print(self.kodolt_szoveg)

    def vizsgal(self, string):
        while len(string) == 0 or len(string) > 255:
            string = input('Kérek egy szöveget! (min:1, max:255 karakter) ')
        return string

    def atalakit(self, sztring):
        ekezetesek = {'á':'a','é':'e','í':'i','ó':'o','ő':'o','ö':'o','ü':'u','ű':'u'}
        sztring = ''.join(karakter for karakter in self.nyilt_szoveg if karakter.isalnum())
        masolat = sztring
        for char in masolat:
            for kulcs in ekezetesek.keys():
                if char == kulcs:
                    masolat = sztring.replace(char,ekezetesek[char]) 
                    sztring = masolat
        sztring = sztring.upper()
        return sztring
    
    def kulcsszoalakitas(self):
        for i in self.atalakitott_szoveg:
            self.szoveg_lista.append(i)
        for index, j in enumerate(self.szoveg_lista):
            self.kulcsszo_lista.append(self.kulcsszo[index % len(self.kulcsszo)])

    def kodolas(self):
        for i in range(len(self.szoveg_lista)):
            for ind, j in enumerate(tarolo[0]):
                if j == self.szoveg_lista[i]:
                    index = ind
            for k in tarolo:
                if k[0] == self.kulcsszo_lista[i]:
                    self.kodolt_szoveg += k[index]

        
main = Main()