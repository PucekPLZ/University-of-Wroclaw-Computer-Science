class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None

def merge_list(L1,L2):
    first = None
    actual = None
    end_of_list = False

    while not end_of_list:
        if L1.val <= L2.val:
            if first == None:
                first = L1
            else:
                actual.next = L1
            actual = L1
            if L1.next == None:
                end_of_list = True
                actual.next = L2
            else:
                L1 = L1.next
        else:
            if first == None:
                first = L2
            else:
                actual.next = L2
            actual = L2
            if L2.next == None:
                end_of_list = True
                actual.next = L1
            else:
                L2 = L2.next

    return first

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
dodaj_element(lista1, 2)
dodaj_element(lista1, 3)
dodaj_element(lista1, 4)
dodaj_element(lista1, 5)
dodaj_element(lista1, 6)
dodaj_element(lista1, 7)
dodaj_element(lista1, 8)
print_list(lista1)

lista2 = ListItem(1)
dodaj_element(lista2, 2)
dodaj_element(lista2, 3)
dodaj_element(lista2, 4)
dodaj_element(lista2, 5)
dodaj_element(lista2, 6)
dodaj_element(lista2, 7)
dodaj_element(lista2, 8)
print_list(lista2)

merge_list(lista1, lista2)
print_list(lista1)