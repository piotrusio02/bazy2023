def cw1():
    names = ['michal', 'nela', 'ola', 'przemek']

    cw1a = [i.capitalize() for i in names]
    print(cw1a)

    cw1b = [i for i in names if "l" in i]
    print(cw1b)

    cw1c = ([i.capitalize() for i in names if i[-1] == 'a'])
    print(cw1c)

    cw1d = len([j for i in names for j in i])
    print(cw1d)

def cw2():
    slownik = {'0':'zero', '1':'jeden', '2':'dwa', '3':'trzy', '4':'cztery', '5':'piec', '6':'szesc', '7':'siedem', '8':'osiem', '9':'dziewiec'}
    while True:
        print('PODAJ ZESTAW ZNAKOW:')
        lista = []
        x = input()

        if x == '':
            break

        for i in x:
            for j in i:
                lista.append(j)
        for x in lista:
            if x in slownik:
                print(slownik.get(x))

def cw3a():
    iloczyn = 1
    while True:
        x = input('PODAJ LICZBE LUB KLIKNIJ ENTER ABY ZAKONCZYC: ')

        if x == '':
            print(f"iloczyn podanych liczb to: {iloczyn}")
            break
        iloczyn = iloczyn * int(x)

def cw3b():
    n = input("podaj potege: ")
    suma = 0
    while True:
        x = input("PODAJ LICZBE LUB KLIKNIJ ENTER ABY ZAKONCZYC: ")
        if x == '':
            print(f"iloczyn podanych liczb to: {suma}")
            break
        suma = suma + (int(x)**int(n))

def mean():
    licznik = 0
    suma = 0
    wynik = 0
    while True:
        x = input('PODAJ LICZBE LUB KLIKNIJ ENTER ABY ZAKONCZYC: ')

        if x == '':
            print(f"srednia arytmetyczna podanych liczb to: {wynik}")
            break
        suma = suma + int(x)
        licznik += 1
        wynik = suma / licznik

def gmean():
    licznik = 0
    iloczyn = 1
    wynik = 0
    while True:
        x = input('PODAJ LICZBE LUB KLIKNIJ ENTER ABY ZAKONCZYC: ')

        if x == '':
            print(f"srednia geometryczna podanych liczb to: {wynik}")
            break
        iloczyn = iloczyn * int(x)
        licznik += 1
        wynik = iloczyn ** (1/licznik)

def cw3d():
    lista = []
    nowa = []
    while True:
        x = input('PODAJ LICZBE LUB KLIKNIJ ENTER ABY ZAKONCZYC: ')
        lista.append(x)
        if x == '':
            break
    for i in lista:
        if i == '':
            lista.remove(i)
    for i in lista:
        for j in i:
            nowa.append(j)
    print(len(nowa))

def cw3e():
    lista = []
    nowe = []
    while True:
        x = input('PODAJ LICZBE LUB KLIKNIJ ENTER ABY ZAKONCZYC: ')
        lista.append(x)
        if x == '':
            break

    for i in lista:
        if i == '':
            lista.remove(i)
    return (min(lista),max(lista))

def cw4a(**kwargs):
    for key, value in kwargs.items():
        print("{0} ma numer {1}".format(key, value))

def cw4b(**kwargs):
    suma = 0
    licznik = 0
    wynik = 0
    for value in kwargs.values():
        suma += value
        licznik += 1
    wynik = suma / licznik
    print(wynik)

def cw5():

    while True:
        pesel = input("podaj swoj pesel: ")
        lista = []

        if len(pesel) != 11:
            print("sprobuj jeszcze raz")
            continue
        else:
            try:
                int(pesel)
            except:
                print("ciąg nie składa się tylko z cyfr")
                continue
            for i in pesel:
                for j in i:
                    lista.append(j)
            r = lista[0:2]
            m = lista[2:4]
            d = lista[4:6]
            # sprawdzamy plec
            if p == 1:
                plec = "Mezczyzna"
            else:
                plec = "Kobieta"
            # sprawdzamy rok urodzenia
            if r < 99 and r > 10:
                pr = 1900
            else:
                pr = 2000
            # sprawdzamy miesiac
            if m == '01':
                mies = "Stycznia"
            elif m == '02':
                mies = "Lutego"
            elif m == '03':
                mies = "Marca"
            elif m == '04':
                mies = "Kwietnia"
            elif m == '05':
                mies = "Maja"
            elif m == '06':
                mies = "Czerwca"
            elif m == '07':
                mies = "Lipca"
            elif m == '08':
                mies = "Siperpnia"
            elif m == '09':
                mies = "Wrzesnia"
            elif m == '10':
                mies = "Pazdzierniaka"
            elif m == '11':
                mies = "Listopada"
            elif m == '12':
                mies = "Grudnia"
            print
            "Twoja data urodzenia to: ", pr + r, m, d
            print
            "Twoja plec to: ", plec
def main():
    # cw1()
    # cw2()
    # cw3a()
    # cw3b()
    # mean()
    # gmean()
    # cw3d()
    # print(cw3e())
    # cw4a(Kasia=123456789, Tomek=987654321, Kacper=981276345)
    # cw4b(styczen=2000, luty=1940, marzec=2000, kwiecien=1500, maj=2050, czerwiec=1500, lipiec=2400, sierpien=2100, wrzesien=1800, pazdziernik=3000, listopad=2300, grudzien=2100)
    # cw4b(styczen=6500, luty=5900, marzec=6200, kwiecien=6300, maj=6450, czerwiec=6600, lipiec=7010, sierpien=5999, wrzesien=5001, pazdziernik=7000, listopad=6200, grudzien=4900)
    cw5()

main()
