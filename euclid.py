e1 = []
e2 = []
e2z = []
e3 = []
e3z = []
e4 = []
e4z = []



a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
b = [100, 200, 300, 400, 500, 600, 700, 800]


def erstelleListenFuerEineEbene(listeGrund, listeZahnrad):
    rueckgabe = []
    for i in range(len(listeGrund)):

        temp = []        
        for e, lg in enumerate(listeGrund):

            if not e % 2:
                temp.append(listeZahnrad[e // 2])
            else:
                temp.append(lg)

        rueckgabe.append(temp)

        listeGrund.append(listeGrund[0])
        listeGrund.pop(0)

    return rueckgabe



l = erstelleListenFuerEineEbene(a, b)
u = 1
for i in l:
    for j in l:
        for m in i:
            for n in j:
                if u == 1:
                    if m + n == 11:
                        print(m, n)
                        print(i)
                        print(j)
                        u = 0