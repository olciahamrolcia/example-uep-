class Triangle:
    def __init__ (self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a
        # self.obwod = a+b+c
    def obwod(self):
        return self.a + self.b + self.c

    def pole(self):
        return self.a * self.h_a/2

trojkat_rownoboczny = Triangle(10, 10, 10, 8)
# print(trojkat_rownoboczny.obwod())
# print(trojkat_rownoboczny.pole())

### kolo
import math
# print(math.pi)

class Kolo:
    def __init__(self, r):
        self.r = r

    def obwod(self):
        return 2*math.pi*self.r

    def pole(self):
        return math.pi*self.r**2

kolo = Kolo(5)
# print(kolo.obwod())
# print(kolo.pole())


### student

class Student:
    def __init__(self, name, surname, index_number):
        self.name = name
        self.surname = surname
        self.index_number = index_number
        self.oceny = []

    def __str__(self):
        # return self.name + " " + self.surname
        return f"{self.name} {self.surname} {self.index_number}"

    def __int__(self):
        return 0

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny) / len(self.oceny)

student_ola = Student("Ola", "Hamrol", "123456")
student_ola.dodaj_ocene(4.5)
student_ola.dodaj_ocene(4.5)

# print(student_ola.oceny)


###car
class Car:
    def __init__(self, brand, year, model, engine, horsepower, price, drivetrain, transmission):
        self.brand = brand
        self.year = year
        self.model = model
        self.engine = engine
        self.horsepower = horsepower
        self.price = price
        self.drivetrain = drivetrain
        self.transmission = transmission

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} {self.price}"

    def policz_moc(self):
        return self.horsepower * 1.36 #z koni mechanicznych na kW

    def wartosc_za5lat(self):
        return self.price * 0.7

    def brake(self):
        print(f"{self.brand} {self.model}: Braking...")

    def policz_zużyciePaliwa(self):
        if self.engine == "diesel" and self.transmission == "manual":
            return "7.5l/100km"
        elif self.engine == "diesel" and self.transmission == "automatic":
            return "6.5l/100km"
        elif self.engine == "petrol" and self.transmission == "manual":
            return "9.5l/100km"
        elif self.engine == "petrol" and self.transmission == "automatic":
            return "8.5l/100km"
        else:
            return "N/A"

car_mercedes = Car("Mercedes AMG", "2023", "GT 63s", "petrol", 680, 170000, "all-wheel", "automatic")

print(car_mercedes)
print("Moc:", car_mercedes.policz_moc(), "kW")
print("Wartość za 5 lat:", car_mercedes.wartosc_za5lat(), "$")
print("Zużycie paliwa:", car_mercedes.policz_zużyciePaliwa())



