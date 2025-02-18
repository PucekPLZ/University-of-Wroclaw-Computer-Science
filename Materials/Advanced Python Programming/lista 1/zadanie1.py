from decimal import Decimal

def vat_faktura(lista):
    result = 0

    result = sum(lista) * 23 / 100

    return result

def vat_paragon(lista):
    result = 0

    for i in range(len(lista)):
        lista[i] = lista[i] * 23 / 100

    result = sum(lista)

    return result

# lista zakupow dla której rownosc jest falszywa
zakupy = [0.000000000000000000000000001 , 0.3333333333, 0.00000000213312 , 20.123123]
print(vat_faktura(zakupy) == vat_paragon(zakupy))

zakupy = [Decimal(i) for i in zakupy]
print(vat_faktura(zakupy) == vat_paragon(zakupy))