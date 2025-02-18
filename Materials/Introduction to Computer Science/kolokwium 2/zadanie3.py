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

def znajdzMax(L):
    maxi = L

    while L.next != None:

        if L.val > maxi.val:
            maxi = L

        L = L.next

    if L.val > maxi.val:
            maxi = L

    return maxi.val

def usun(lis, uval):
    pom = lis

    while pom != None and pom.val != uval:
    #poszukiwanie elementu uval
        poprz = pom
        pom = pom.next
    if pom == lis: #do usuniecia pierwszy
        lis=lis.next
    else: #tworzymy powiąz. omijajace
        poprz.next = pom.next

    return lis


lista1 = ListItem(13)
dodaj_element(lista1, 2)
dodaj_element(lista1, 15)
dodaj_element(lista1, 6)
dodaj_element(lista1, 5)
dodaj_element(lista1, 8)
dodaj_element(lista1, 14)

#print_list(lista1)

#print(znajdzMax(lista1))
print_list(usun(lista1, znajdzMax(lista1)))
#print_list(lista1)

