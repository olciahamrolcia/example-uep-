class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def __str__(self):
        return "Pracownik {self.imie} {self.nazwisko}"

    def policz_netto(self):
        skladki_spoleczne = self.wynagrodzenie_brutto * 0.0976 + self.wynagrodzenie_brutto * 0.015 + self.wynagrodzenie_brutto * 0.0245
        # 9.76% składki emerytalnej, 1.5% składki rentowej, 2.45% ubezpieczenie chorobowe
        skladka_zdrowotna = (self.wynagrodzenie_brutto - skladki_spoleczne) * 0.09  # 9% składki zdrowotnej
        koszty_uzyskania_przychodu = 250
        podstawa_podatku = self.wynagrodzenie_brutto - skladki_spoleczne - skladka_zdrowotna - koszty_uzyskania_przychodu
        zaliczka_na_podatek = (podstawa_podatku * 0.12) - 300 if podstawa_podatku > 3000 else 0
        wynagrodzenie_netto = self.wynagrodzenie_brutto - skladki_spoleczne - skladka_zdrowotna - zaliczka_na_podatek

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


import csv

pracownicy = []
with open('pracownicy.csv') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        pracownicy.append(Pracownik(row[0], row[1], float(row[2])))

pracownicy_koszt = 0

# Wyświetlanie informacji dla każdego pracownika
for pracownik in pracownicy:
    print(f"Pracownik {pracownik.imie} {pracownik.nazwisko}:")
    print("- pensja brutto:", pracownik.wynagrodzenie_brutto)
    print("- pensja netto:", pracownik.policz_netto())
    print("- koszt pracodawcy:", pracownik.oblicz_koszty())
    print("- koszt całkowity:", pracownik.wynagrodzenie_brutto + pracownik.oblicz_koszty())

    pracownicy_koszt += pracownik.wynagrodzenie_brutto + pracownik.oblicz_koszty()

print("Suma kosztów wynosi:", pracownicy_koszt)