from math import ceil


def oblicz(fl, fw, pl, pw, x):
    ff = fl * fw * 1.1
    pf = pl * pw
    return ceil((ff / pf) / x)


fl = float(input("dlugosc podlogi: "))
fw = float(input("szerokosc podlogi: "))
pl = float(input("dlugosc panela: "))
pw = float(input("szerokosc panela: "))
x = int(input("ilosc paneli w paczce: "))
ans = oblicz(fl, fw, pl, pw, x)
print(f"potrzeba {ans} opakowan")
