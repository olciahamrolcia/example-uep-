class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto, student=False, wiek=0, zamezny=False):
        # default values are used when class is created without these values
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto
        self.student = student
        self.wiek = wiek
        self.zamezny = zamezny

    def __str__(self):
        return "Pracownik {self.imie} {self.nazwisko}"

    def policz_netto(self):
        skladka_emerytalna = self.wynagrodzenie_brutto * 0.0976  # 9,76% składki emerytalnej
        skladka_rentowa = self.wynagrodzenie_brutto * 0.015  # 1,5% składki rentowej
        skladka_chorobowa = self.wynagrodzenie_brutto * 0.0245  # 2,45% składki chorobowej

        suma_skladek = skladka_emerytalna + skladka_rentowa + skladka_chorobowa

        skladka_zdrowotna = (self.wynagrodzenie_brutto - suma_skladek)* 0.09  # 9% składki zdrowotnej po odliczeniu innych składek

        zaliczka_na_podatek = (self.wynagrodzenie_brutto - suma_skladek - skladka_zdrowotna) * 0.12 - ((self.wynagrodzenie_brutto - suma_skladek - skladka_zdrowotna) * 0.12/24)  # 12% zaliczki na podatek pomniejszony o 1/24

        wynagrodzenie_netto = self.wynagrodzenie_brutto - suma_skladek - skladka_zdrowotna - zaliczka_na_podatek

        return wynagrodzenie_netto


    def oblicz_koszty(self):
        skladka_emerytalna = self.wynagrodzenie_brutto * 0.0976  # 9.76% składki emerytalnej
        skladka_rentowa = self.wynagrodzenie_brutto * 0.015  # 1.5% składki rentowej
        skladka_wypadkowa = self.wynagrodzenie_brutto * 0.0167  # 2% składki wypadkowej (średnia pomiędzy 0,67 a 3,33)
        fundusz_pracy = self.wynagrodzenie_brutto * 0.0245  # 2.45% składki na fundusz pracy
        fgsp = self.wynagrodzenie_brutto * 0.1  # 10% składki FGŚP

        suma_skladek = skladka_emerytalna + skladka_rentowa + skladka_wypadkowa + fundusz_pracy + fgsp

        koszt_pracodawcy = self.wynagrodzenie_brutto + suma_skladek

        return koszt_pracodawcy

    def czy_student(self):
        return self.student

    def czy_ponizej_26(self):
        return self.wiek < 26

    def czy_zamezny(self):
        return self.zamezny

    def wplyw_na_wynagrodzenie(self):
        netto = self.policz_netto()

        if self.czy_student():
            netto += 400

        if self.czy_ponizej_26():
            netto += 300  # Dodatkowa kwota dla osób poniżej 26 roku życia

        if self.czy_zamezny():
            netto += 100
import csv
pracownicy = []  # z csv
for pracownik in pracownicy:
    print("Pracownik Jan Kowalski: ")
    print("- pensja brutto: ")
    print("- pensja netto: ")
    print("- koszt pracodawcy: ")
    print("- koszt całkowity: ")

print("Suma kosztów wynosi: xxx")