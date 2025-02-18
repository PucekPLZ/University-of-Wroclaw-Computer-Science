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

def usunOstPar(L):
    L2 = L
    pom = None
    while L2.next != None:
        L2 = L2.next

        if L2.val % 2 == 0:
            pom = L2

    print(L.val, end=" ")
    while L.next != None:
        L = L.next
        if L == pom:
            L = pom.next

        if L.next != None:
            print(L.val, end=" ")
        else:
            print(L.val)
    
def parzyste(L):
    suma = 0

    while L.next != None:
        if L.val % 2 == 0:
            suma += L.val

        L = L.next

    return suma

lista1 = ListItem(1)
dodaj_element(lista1, 2)
dodaj_element(lista1, 3)
dodaj_element(lista1, 6)
dodaj_element(lista1, 5)
dodaj_element(lista1, 8)
dodaj_element(lista1, 7)
print_list(lista1)
usunOstPar(lista1)

print(parzyste(lista1))
