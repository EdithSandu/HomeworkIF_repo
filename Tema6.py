''''#1
class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare= culoare
        self.PI=3.14
    def descriere_cerc(self):
        print(f'Raza are lungimea de {self.raza}')
        print(f'Culoarea este {self.culoare}')
    def arie(self):
        self.arie= self.PI*self.raza*self.raza
        return self.arie
    def diametru(self):
        self.diametru=self.raza *2
        return self.diametru()
    def circumferinta(self):
        self.circum=2*self.PI * self.raza
        return self.circum

#2.
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
    def descriere_dreptunghi(self):
        print(f'Lungimea dreptunghiului este {self.lungime}')
        print(f'Latimea dreptunghiului este {self.latime}')
        print(f'Culoarea dreptunghiului este {self.culoare}')
    def ariedr(self):
        self.ariedr= self.lungime * self.latime
        return self.ariedr
    def perimetrudr(self):
        self.perimetrudr=2*(self.lungime+self.latime)
        return self.perimetrudr
    def schimba_culoarea(self, noua_culoare):
        self.culoare= noua_culoare

#3.
class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
    def descrie(self):
        print(f'Numele angajatului este {self.nume}')
        print(f'Prenumele angajatului este {self.prenume}')
        print(f'Salariul angajatului este {self.salariu}')
    def nume_complet(self):
        return self.nume+' '+self.prenume
    def salariu_lunar(self):
        return self.salariu
    def salariu_anual(self):
        return self.salariu*12
    def marire_salariu(self, marire):
        self.salariu= self.salariu+(marire/100* self.salariu)
        return self.salariu

#4.
class Cont:
    def __init__(self, IBAN, titular_cont, sold):
        self.IBAN=IBAN
        self.titular_cont= titular_cont
        self.sold= sold
    def descrierecont(self):
        print(f'IBAN-ul este {self.IBAN}.')
        print(f'Titularul contului este {self.titular_cont}.')
        print(f'Soldul contului este {self.sold}')
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.IBAN} suma de {self.sold} lei.')
    def debitare_cont(self, suma):
        if suma>=self.sold:
            self.sold-=suma
        else:
            print('Fonduri insuficiente')
    def crediatre_cont(self, suma):
        self.sold+=suma'''
#5.
from datetime import date
from tabulate import tabulate
class Factura:
    seria= 585698
    def __init__(self, numar, nume_produs, cantitate, pret_bucata):
        self.numar=numar
        self.nume_produs=nume_produs
        self.cantitate=cantitate
        self.pret_bucata=pret_bucata
    def schimba_cantitatea(self, cantitate):
        self.cantitate=cantitate
    def schimba_pretul(self, pret):
        self.pret=pret
    def schimba_nume_produs(self,nume):
        self.nume_produs=nume
    def total(self):
        return self.pret_bucata*self.cantitate
    def genereaza_factura(self):
        print(tabulate([[self.nume_produs,self.cantitate,self.pret_bucata,self.total(),date.today()]],headers=['Produs', 'Cantitate','Pret', 'Total', 'Data']))

