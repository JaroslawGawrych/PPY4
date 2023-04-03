def find(dane):
    pierwsze = []
    for i in range(max(dane) + 1):
        pierwsze.append(True)
    pierwsze[0] = False
    pierwsze[1] = False
    for i in range(len(pierwsze)):
        if pierwsze[i]:
            x = i * i
            while x < len(pierwsze):
                pierwsze[x] = False
                x += i
    for i in dane:
        print(f"{i} - {pierwsze[i]}")


lista = []
a = input("podaj liczbe (exit aby zakonczyc podawanie liczb): ")
while a != "exit":
    lista.append(int(a))
    a = input("podaj liczbe (exit aby zakonczyc podawanie liczb): ")
find(lista)
