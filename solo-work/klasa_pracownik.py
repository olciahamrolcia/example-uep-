class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def __str__(self):
        return "Pracownik {self.imie} {self.nazwisko}"

    def policz_netto(self):
        skladka_emerytalna = self.wynagrodzenie_brutto * 0.0976  # 9,76% składki emerytalnej
        skladka_rentowa = self.wynagrodzenie_brutto * 0.015  # 1,5% składki rentowej
        skladka_chorobowa = self.wynagrodzenie_brutto * 0.0245  # 2,45% składki chorobowej

        suma_skladek = skladka_emerytalna + skladka_rentowa + skladka_chorobowa

        skladka_zdrowotna = (self.wynagrodzenie_brutto - suma_skladek)* 0.09 # 9% składki zdrowotnej po odliczeniu innych składek

        wynagrodzenie_netto = self.wynagrodzenie_brutto - suma_skladek - skladka_zdrowotna

        return wynagrodzenie_netto

    def oblicz_koszty(self):
        wynagrodzenie = self.wynagrodzenie_brutto


pracownicy = []  # z csv
for pracownik in pracownicy:
    print("Pracownik Jan Kowalski: ")
    print("- pensja brutto: ")
    print("- pensja netto: ")
    print("- koszt pracodawcy: ")
    print("- koszt całkowity: ")

print("Suma kosztów wynosi: xxx")