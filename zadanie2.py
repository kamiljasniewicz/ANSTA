# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE


def jakichElementowBrakuje(lista_wejsciowa, n):
	lista_wejsciowa  = lista_wejsciowa.split(",")
	lista_wejsciowa = [int(x) for x in lista_wejsciowa]
	
	lista_n = list(range(1, int(n) + 1))

	for element in lista_wejsciowa:
		if element in lista_n:
			lista_n.remove(element)

	return lista_n

print(jakichElementowBrakuje(input("Podaj liczby (po przecinkach): "), input("Podaj n: ")))