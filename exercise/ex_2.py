# trojkat

a = 10
b = 20
c = 15
h = 12

obwod = a + b + c
pole = int((h * a) / 2)

print("Obwod trojkata wynosi " + str(obwod) + ", zas pole wynisi " + str(pole) + ".")

#square

a = 10
obwod = a*4

pole = a**2

print("Obwod kwadratu wynosi " + str(obwod) + ", a pole wynosi " + str(pole) + ".")


#rectangle

a = 10
b = 20

obwod = a*2 + b*2

pole = a*b

print("Obwod prostokata wynosi " + str(obwod) + ", a pole wynosi " + str(pole) + ".")


#circle
#importing math library
import math

r = 10

obwod = 2*math.pi*r
pole = math.pi*(r**2)

print("Obwod kola wynosi " + str(obwod) + ", a pole wynosi " + str(pole) + ".")

#trapeze

# didn't check if dimensions are possible
a = 10
b = 20
c = 15
d = 17

h = 8

obwod = a+b+c+d
pole = (a+b)*h/2

print("Obwod trapezu wynosi " + str(obwod) + ", a pole wynosi " + str(pole) + ".")
