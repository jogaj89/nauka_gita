#imie = 'Asia'
#nazwisko = "G"
#print ("Hello world! lalalal, {0}!".format(imie) +" "+ nazwisko)

#zwierzeta = 4
#cena = 40 / 4
#print (cena)

def wypisz_osobe(imie, nazwisko):
    print ("{0} {1}".format(imie, nazwisko))

def  czy_emeryt(wiek):
    MAX = 68
    if wiek < MAX:
        return True
    else:
        return  False

if __name__ == "__main__":
    imie = 'asia'
    nazwisko = 'G'
    wiek = 85
    print (imie)

    wypisz_osobe(imie, nazwisko)
    if czy_emeryt(wiek):
        print('nie emeryt')
    else:
        print ('emeryt')
