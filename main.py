def sonlar_royxati(sonlar):
    natija = []
    for son in sonlar:
        raqamlar_yigindisi = sum(int(raqam) for raqam in str(son))
        if raqamlar_yigindisi % 2 == 0:
            natija.append("Juft sum")
        else:
            natija.append("Toq sum")
    return natija

sonlar = [12, 34, 56, 78, 90]
print(sonlar_royxati(sonlar))
