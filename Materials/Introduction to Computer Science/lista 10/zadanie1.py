class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None


def dodaj_element(L, element):
    while L.next != None:
        L = L.next
    L.next = ListItem(element)


def print_list(L):
    while L.next != None:
        print(L.val, end=" ")
        L = L.next
    print(L.val)


lista1 = ListItem(1)
print_list(lista1)
dodaj_element(lista1, 2)
print_list(lista1)
dodaj_element(lista1, 3)
dodaj_element(lista1, 4)
dodaj_element(lista1, 5)
dodaj_element(lista1, 6)
dodaj_element(lista1, 7)
dodaj_element(lista1, 8)
print_list(lista1)

