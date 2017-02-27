# -*- coding: UTF-8 -*-

class Vozila:
    def __init__(self, znamka, model, stevilo_prevozenih_km, datum_zadnjega_servisa):
        self.znamka = znamka
        self.model = model
        self.stevilo_prevozenih_km = stevilo_prevozenih_km
        self.datum_zadnjega_servisa = datum_zadnjega_servisa

    def dodaj_km(self, novi_km):
        self.stevilo_prevozenih_km += novi_km

    def posodobi_zadnji_datum(self, nov_datum):
        self.datum_zadnjega_servisa = nov_datum

def vsa_vozila(vozila):
    for i, vozilo in enumerate(vozila):
        print "%s) %s %s s prevozenimi %s km. Zadnji datum servisa: %s" % (i+1, vozilo.znamka, vozilo.model, vozilo.stevilo_prevozenih_km, vozilo.datum_zadnjega_servisa)


def dodaj_novo_vozilo(vozila):
    znamka = raw_input("Prosim vpišite znamko vozila: ")
    model = raw_input("Prosim vpišite model vozila: ")
    stevilo_prevozenih_km = raw_input("Prosim vpišite število prevoženih kilometrov: ")
    datum_zadnjega_servisa = raw_input("Prosim vpišite datum zadnjega servisa (DD.MM.YYYY): ")

    rezultat = Vozila(znamka=znamka, model=model, stevilo_prevozenih_km=stevilo_prevozenih_km, datum_zadnjega_servisa=datum_zadnjega_servisa)
    vozila.append(rezultat)
    print ""
    print "Dodali ste: %s %s" % (rezultat.znamka, rezultat.model)


def izberi_vozilo(vozila):
    print("Prosim izberite številko vozila ki ga hočete spremeniti.")
    print ""
    vsa_vozila(vozila)
    print ""
    izbira = raw_input("Katero številko vozila bi radi spremenili? ")
    return vozila[int(izbira) -1]

def dodaj_nove_kilometre(vozila):
    sel_vozila = izberi_vozilo(vozila)

    print "Izbrano vozilo: %s %s s prevoženimi %s km." % (sel_vozila.znamka, sel_vozila.model, sel_vozila.stevilo_prevozenih_km)
    print ""
    novi_kilometri = raw_input("Koliko km bi želeli dodati? ")
    print ""

    novi_kilometri = novi_kilometri.replace(",", ".")
    novi_km = (novi_kilometri)

    sel_vozila.dodaj_km(novi_km)
    print "Novi kilometri za %s %s so zdaj: %s." % (sel_vozila.znamka, sel_vozila.model, sel_vozila.stevilo_prevozenih_km)


def sprememba_datuma_servisa(vozila):
        sel_vozila = izberi_vozilo(vozila)

        print "Izbrano vozilo: %s %s, zadnji datum servisa: %s." % (sel_vozila.znamka, sel_vozila.model, sel_vozila.datum_zadnjega_servisa)
        print ""
        nov_datum_servisa = raw_input("Vpišite nov datum zadnjega servisa: ")
        print ""
        sel_vozila.posodobi_zadnji_datum(nov_datum=nov_datum_servisa)
        print("Servisni datum je posodobljen!")

def shrani_na_disk(vozila):
        with open("vozila.txt", "w+") as voz_file:
            for vozilo in vozila:
                voz_file.write("%s,%s,%s,%s\n" % (vozilo.znamka, vozilo.model, vozilo.stevilo_prevozenih_km, vozilo.datum_zadnjega_servisa))


def main():
    print("Dobrodošli v programu Maneger vozila.")

    bmw = Vozila(znamka="Bmw", model="serija 3", stevilo_prevozenih_km="30.000", datum_zadnjega_servisa="1.12.2015")
    audi = Vozila(znamka="Audi", model="A7", stevilo_prevozenih_km="60.120", datum_zadnjega_servisa="8.10.2013")
    opel = Vozila(znamka="Opel", model="Astra", stevilo_prevozenih_km="47.230", datum_zadnjega_servisa="25.3.2016")
    vozila = [bmw, audi, opel]

    while True:
        print "" # prazna vrstica
        print "Prosim izberite eno od naslednjih možnosti:"
        print "a) Oglejte si seznam vseh vozil v podjetju."
        print "b) Dodaj novo vozilo."
        print "c) Urejanje kilometrov za izbrano vozilo."
        print "d) Uredite zadnji datum za izbrano vozilo."
        print "e) Zaprite program."
        print ""

        izbira = raw_input("Katero možnost bi radi izbrali? (a, b, c, d, e): ")
        print ""

        if izbira.lower() == "a":
            vsa_vozila(vozila)
        elif izbira.lower() == "b":
            dodaj_novo_vozilo(vozila)
        elif izbira.lower() == "c":
            dodaj_nove_kilometre(vozila)
        elif izbira.lower() == "d":
            sprememba_datuma_servisa(vozila)
        elif izbira.lower() == "e":
            print("Zahvaljujemo se vam za uporabo Manager vozil. Lep dan še naprej!")
            shrani_na_disk(vozila)
            break
        else:
            print"Žal nisem razumel vaše izbire. Vnesite samo črko a, b, c ali d."

if __name__ == '__main__':
    main()
