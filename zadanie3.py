# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL


def generatorLiczb(od, do, co_ile):
    lista = []
    for x in range(int(od * 10), int(do * 10 + 1), int(co_ile * 10)):
        lista.append(x / 10)

    return lista

print(generatorLiczb(2, 5.5, 0.5))