#mapa myśli_sumOfList
#if list is emoty[]
#return 0 -> pusta lista, zwróć zero
#else
#return pierwszy przypadek z listy + f[rest of the list]
def sumOfList(lista):
    if not lista:
        return 0
    else:
        return lista[0] + sumOfList(lista[1:])

#example:
lista1 = [1, 2, 3, 2, 6]
suma = sumOfList(lista1)
print(suma)


#mapa myśli_silnia
#if number is 0 or 1
#return 1 (silnia dla 0 i 1 to 1)
#else
#return number * f(n-1)

def silnia(n):
    if n <= 1:
        return 1
    else:
        return n * silnia(n - 1)

#example:
liczba = 8
wynik = silnia(liczba)
print(wynik)


#mapa myśli_maxOfList
#if list has only one element:
#return that element
#else
#maximum of the list = var
#if first element > var:
#return first element
#else
#return var
def maxOfList(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_list= maxOfList(lista[1:])
        if lista[0] > max_list:
            return lista[0]
        else:
            return max_list

#example
lista2 = [1, 5, 3, 9, 2, 11, 67, 3, 8]
maks = maxOfList(lista2)
print(maks)


#mapa myśli_fibonacci
#if number is 0 or 1
#return number (fibonacci od 0 = 0, fibonacci od 1 = 1)
#else
#return sum of f(n-1) i f(n-2)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#example
term = 3
wynik = fibonacci(term)
print(wynik)


# sudoku 4

puzzle = [[0, 2, 0, 4],
          [0, 4, 0, 0],
          [2, 0, 4, 0],
          [0, 0, 2, 3]]

#przykładowe sudoku, lista list

def valid(row, col, value):
    # sprawdza czy można umieścić daną wartość numeryczną w wierszu, kolumnie i kwadracie 2x2, przechodzi przez wszystkie
    # wartości w wierszu i sprawdza czy coś jest równe "value", to samo w kolumnie i w kwadracie, jeśli wartość się
    # powtarza to zwraca False bo nie może zostać użyta, jeśli nie zwraca True
    global puzzle  # oznaczenie że zmienna jest poza funkcją
    for i in range(0, 4): #4 iteracje - od 0 do 3
        if puzzle[row][i] == value:
            return False
    for i in range(0, 4):
        if puzzle[i][col] == value:
            return False
    #określenie wartości początkowej dla kwadratu 2x2
    row_start = (row // 2) * 2 # dzielenie całkowitoliczbowe, zaokrągla do najbliższej liczby całkowitej potem mnożone
                               # przez 2 i uzyskiwana jest wartość początkowa, ktora wynosi albo 0 albo 2
                               # dla sprawdzenia duplikatów i rozwiazania sudoku, określa w której komórce 2x2
                               # algorytm się znajduje
    col_start = (col // 2) * 2
    for i in range(0, 2): # sprawdzanie po wartosciach wierszy dla 0 i 1 w kwadracie 2x2
        for j in range (0, 2): # sprawdzanie po wartosciach kolumn dla 0 i 1 w kwadracie 2x2
            if puzzle[row_start + i][col_start + j] == value:
                return False
                # wszystkie możliwości które mogły być nieudane są wykorzystane

    return True #nie ma danej wartosci w kolumnie ani wierszu, ani kwadracie

def sudoku(): #rozwiazuje sudoku
    global puzzle #oznaczenie że zmienna jest poza funkcją
    for i in range (0, 4):
        for j in range (0, 4):
            if puzzle[i][j] == 0:  # sprawdza czy wartosc pola jest rowna 0 i jesli tak to musi zostac wypelnione
                                   # zidoentyfikowane są wszystkie pola 0 na planszy
                for num in range(1,5):  # uzywana do przechodzenia od 1 do 4, sprawdza jaka wartość może zostać wpisana
                    if valid(i, j, num):  # sprawdza czy warosc nie powodoje powtórzen w wierszu, kolumnie, kwadracie
                        puzzle[i][j] = num
                        sudoku()  # znalezienie dlaszego rozwiązanie (rekurencja)
                        puzzle[i][j] = 0  # pole wraca do wartosci 0 z poprzedniego pola jesli zadna z wartosci nie pasuje
                                          # do obecnego tego pola

                return #konczy działanie funkcji i powraca do kolejnego sprawdzania innych możliwosci dla pół 0 na planszy

    print(puzzle)
    # print(np.array(puzzle))

sudoku()


# sudoku 9 -> tak samo jak sudoku 4 ze zmianami liczbowymi

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def valid(row, col, value):
    global puzzle
    for i in range(0, 9): #zmiana 4 na 9
        if puzzle[row][i] == value:
            return False
    for i in range(0, 9):
        if puzzle[i][col] == value:
            return False
    row_start = (row // 3) * 3  # zmiana z 2 na 3 bo kwadraty w sudoku są wielkości 3x3
    col_start = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[row_start + i][col_start + j] == value:
                return False

    return True

def sudoku():
    global puzzle
    for i in range(0, 9):  #zmiana z 4 na 9
        for j in range(0, 9):
            if puzzle[i][j] == 0:
                for num in range(1, 10):  # zmiana z 5 na 10
                    if valid(i, j, num):
                        puzzle[i][j] = num
                        sudoku()
                        puzzle[i][j] = 0

                return

    print(puzzle)
    # print(np.array(puzzle))

sudoku()



