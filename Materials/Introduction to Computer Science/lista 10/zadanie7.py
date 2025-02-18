class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.last = self # tylko pierwszy przechowuje

def add_last_element(L, element):
    item = ListItem(element)
    L.last.next = item
    L.last = item

def reverse_list(L):
    def reverse_part(a, n):
        first = a
        for i in range(n-1):
            a = a.next
        last = a
        first.val, last.val = last.val, first.val
    f = L
    l = 1
    while L.next != None:
        L = L.next
        l += 1
    for i in range(0,l,2):
        reverse_part(f, l - i)
        f = f.next

def print_list(L):
    while L.next != None:
        print(L.val, end=" ")
        L = L.next
    print(L.val)

lista1 = ListItem(5)
add_last_element(lista1, 6)
add_last_element(lista1, 7)
add_last_element(lista1, 8)
add_last_element(lista1, 3)
add_last_element(lista1, 3)
print_list(lista1)
reverse_list(lista1)
print_list(lista1)
