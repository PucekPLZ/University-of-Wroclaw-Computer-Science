class R:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def __add__(self, other):
        L = self.licznik * other.mianownik + other.licznik * self.mianownik
        M = self.mianownik * other.mianownik
        return R(L, M)

    def __sub__(self, other):
        L = self.licznik * other.mianownik - other.licznik * self.mianownik
        M = self.mianownik * other.mianownik
        return R(L, M)

    def __mul__(self, other):
        L = self.licznik * other.licznik
        M = self.mianownik * other.mianownik
        return R(L, M)

    def __truediv__(self, other):
        L = self.licznik * other.mianownik
        M = self.mianownik * other.licznik
        return R(L, M)

    def __eq__(self, other):
        return self.licznik * other.mianownik == other.licznik * self.mianownik

    def __gt__(self, other):
        return self.licznik * other.mianownik > other.licznik * self.mianownik
    
    def __lt__(self, other):
        return self.licznik * other.mianownik < other.licznik * self.mianownik

    def __ge__(self, other):
        return self.licznik * other.mianownik >= other.licznik * self.mianownik

    def __le__(self, other):
        return self.licznik * other.mianownik <= other.licznik * self.mianownik

    def __str__(self):
        return f'{self.licznik}/{self.mianownik}'

    def __repr__(self):
        return f'R({self.licznik}, {self.mianownik})'



ulamek1 = R(1, 2)
ulamek2 = R(3, 4)

wynik = ulamek1 + ulamek2
print(wynik) 


wynik = ulamek1 - ulamek2
print(wynik) 

wynik = ulamek1 * ulamek2
print(wynik) 


wynik = ulamek1 / ulamek2
print(wynik) 

print(ulamek1 == ulamek2) 
print(R(1, 2) == R(2, 4)) 
print(ulamek1 > ulamek2)
print(ulamek1 < ulamek2)
print(ulamek1 >= ulamek2)
print(ulamek1 <= ulamek2)

print(ulamek1) 
print(ulamek2) 
print(ulamek1, ulamek2) 
