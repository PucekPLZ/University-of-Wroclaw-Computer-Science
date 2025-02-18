class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None

def usun(lis, uval):
    pom = lis
    while pom != None and pom.val != uval:
    #poszukiwanie elementu uval
        poprz = pom
        pom = pom.next
    if pom != None: # na liscie wystapil uval
        if pom == lis: #do usuniecia pierwszy
            lis=lis.next
        else: #tworzymy powiąz. omijajace
            poprz.next = pom.next
    return lis

def dodaj_element(L, element):
    while L.next != None:
        L = L.next
    L.next = ListItem(element)


def print_list(L):
    while L.next != None:
        print(L.val, end=" ")
        L = L.next
    print(L.val)


lista1 = ListItem(10)
dodaj_element(lista1, 12)
dodaj_element(lista1, 3)
dodaj_element(lista1, 12)
dodaj_element(lista1, 5)
dodaj_element(lista1, 8)
dodaj_element(lista1, 11)
print_list(lista1)

print_list(usun(lista1, 12))