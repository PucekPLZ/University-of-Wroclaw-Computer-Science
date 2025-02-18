import sys

class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None


def dodaj_element(L, element):
    while L.next != None:
        L = L.next
    L.next = ListItem(element)

def usun_element(L):
    poprzedni = None
    while L.next != None:
        poprzedni = L
        L = L.next
    del L
    poprzedni.next = None

def print_list(L):
    while L.next != None:
        print(L.val, end=" ")
        L = L.next
    print(L.val)


lista1 = ListItem(1)
dodaj_element(lista1, 2)
dodaj_element(lista1, 3)
dodaj_element(lista1, 4)
dodaj_element(lista1, 5)
dodaj_element(lista1, 6)
dodaj_element(lista1, 7)
dodaj_element(lista1, 10)
print_list(lista1)
usun_element(lista1)
print_list(lista1)
