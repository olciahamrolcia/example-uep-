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