#
# Lucjan Pucelak
# zadanie 2
# python3 zadanie2.py
#

from math import gcd

class Ulamek:
    # pierwszy podpunkt
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    # drugi podpunkt
    def uprosc(self, other):
        dzielnik = gcd(self.licznik * other.licznik, self.mianownik * other.mianownik)
        L = self.licznik * other.licznik // dzielnik
        M = self.mianownik * other.mianownik // dzielnik
        return Ulamek(L, M)

    # trzeci podpunkt
    def show(self):
        return print(f'{self.licznik}/{self.mianownik}')

    # czwarty podpunkt 
    # nowoutworzony element
    def __add__(self, other):
        L = self.licznik * other.mianownik + other.licznik * self.mianownik
        M = self.mianownik * other.mianownik
        return Ulamek(L, M)

    def __sub__(self, other):
        L = self.licznik * other.mianownik - other.licznik * self.mianownik
        M = self.mianownik * other.mianownik
        return Ulamek(L, M)

    def __mul__(self, other):
        L = self.licznik * other.licznik
        M = self.mianownik * other.mianownik
        return Ulamek(L, M)

    def __truediv__(self, other):
        L = self.licznik * other.mianownik
        M = self.mianownik * other.licznik
        return Ulamek(L, M)

    # modifikowanie drugiego elementu
    def __add__(self, other):
        other.licznik = self.licznik * other.mianownik + other.licznik * self.mianownik
        other.mianownik = self.mianownik * other.mianownik
        return other

    def __sub__(self, other):
        other.licznik = self.licznik * other.mianownik - other.licznik * self.mianownik
        other.mianownik = self.mianownik * other.mianownik
        return other

    def __mul__(self, other):
        other.licznik = self.licznik * other.licznik
        other.mianownik = self.mianownik * other.mianownik
        return other

    def __truediv__(self, other):
        other.licznik = self.licznik * other.mianownik
        other.mianownik = self.mianownik * other.licznik
        return other


ulamek1 = Ulamek(4, 7)
ulamek2 = Ulamek(2, 4)

x = Ulamek.uprosc(ulamek1, ulamek2)
x.show()

wynik = ulamek1 + ulamek2
wynik.show()

wynik = ulamek1 - ulamek2
wynik.show()

wynik = ulamek1 * ulamek2
wynik.show()

wynik = ulamek1 / ulamek2
wynik.show()