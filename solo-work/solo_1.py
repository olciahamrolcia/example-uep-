#zadanie1.1

txt = "{hello} {student}"

print(txt.format(hello = "Hello", student = "Ola"))

print(txt.format(hello = "Hi", student = "Kasia"))


#zadanie1.2

# student = input("Wpisz swoje imie")
# print('Hello ' + student)


#zadanie1.3

students = ["Ania", "Kuba", "Piotr", "Jan"]

x = len(students)

print("Liczba studentów wynosi " + str(x))


#zadanie1.4

students = ["Ania", "Kasia", "Piotr", "Tomek"]

for name in students:
    print("Hello " + name)


#zadanie1.5

n = 3
p = 4

w = n**p

print("wynik wynosi " + str(w))


#zadanie1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"

x = ciag_znakow.count("(")
print("Liczba nawiasow otwierajacych wynosi: " + str(x))


#zadanie1.7

students = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

sorted_students = sorted(students)

print("Alfabetyczna lista studentow wynosi: ")
for student in sorted_students:
    print(student)


# zadanie 1.8

# posortuj alfabetycznie (od nazwiska) studentow
students = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

students.sort(key=lambda s: s.split()[1])
print("Alfabetyczna lista studentow wynosi: ")
for student in students:
    print(student)
