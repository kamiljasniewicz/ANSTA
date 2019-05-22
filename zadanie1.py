# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH


def generatorKodow(kod1, kod2):
    for x in range(int(kod1[0:2]+kod1[3:6]), int(kod2[0:2]+kod2[3:6]) + 1):
        print(str(x)[0:2], "-", str(x)[2:6])

generatorKodow("79-900", "80-155")