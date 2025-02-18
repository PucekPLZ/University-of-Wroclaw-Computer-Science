class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None


def add_element(L, element):
    while L.next != None:
        L = L.next
    L.next = ListItem(element)

def remove_elements(L, n):
    previous = L
    X = L

    while L.next != None:
        L = L.next
        if L.val == n:
            previous.next = L.next
        else:
            previous = L
    
    if X.val == n:
        pop_first_element(X)
        

def pop_first_element(L):
    L.val = L.next.val
    L.next = L.next.next

def print_list(L):
    while L.next != None:
        print(L.val, end=" ")
        L = L.next
    print(L.val)


lista1 = ListItem(6)
add_element(lista1, 6)
add_element(lista1, 5)
add_element(lista1, 6)
add_element(lista1, 6)
add_element(lista1, 6)
add_element(lista1, 6)
add_element(lista1, 6)
print_list(lista1)
remove_elements(lista1, 6)
print("")
print_list(lista1)
