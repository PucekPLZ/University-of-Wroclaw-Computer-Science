class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None


def dodaj_element(L, element):
    while L.next != None:
        L = L.next
    L.next = ListItem(element)

def polacz(L1, L2):
    while L1.next != None:
        L1 = L1.next
    L1.next = L2

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
dodaj_element(lista1, 8)
print_list(lista1)

lista2 = ListItem(100)
dodaj_element(lista2, 101)
dodaj_element(lista2, 102)
print_list(lista2)

polacz(lista1, lista2)
print_list(lista1)