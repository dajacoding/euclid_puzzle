e1 = []
e2 = []
e2z = []
e3 = []
e3z = []
e4 = []
e4z = []


def hauptfunktion():
    l1 = e1
    l2 = erstelleListenFuerEineEbene(e2, e2z)
    l3 = erstelleListenFuerEineEbene(e3, e3z)
    l4 = erstelleListenFuerEineEbene(e4, e4z)
    abgleichen(l1, l2, l3, l4)


def abgleichen(l1, l2, l3, l4):
    a = 0
    b = 0
    c = 0

    while True:
        temp1 = l1
        temp2 = l2[a]
        temp3 = l3[b]
        temp4 = l4[c]

        if segmentSummenVergleich(temp1, temp2, temp3, temp4):
            print(temp1)
            print(temp2)
            print(temp3)
            print(temp4)
            break

        a += 1
        if a == len(temp2):
            a = 0
            b += 1
        if b == len(temp3):
            b = 0
            c += 1
        if c == len(temp4):
            print("something went wrong")
            break


def listenReduktion(listeInnen):
    reduzierteListe = []
    for li in listeInnen:
        temp = 0
        for i in range(li):
            if e2[i] == li[i]:
                temp += 1
        if temp == 8:
            reduzierteListe.append(li)
    return reduzierteListe    

    
def segmentSummenVergleich(list1, list2, list3, list4):
    temp = list1[0] + list2[0] + list3[0] + list4[0]
    for i in range(len(list1)):
        if list1[i] + list2[i] + list3[i] + list4[i] != temp:
            return False
        if i + 1 == len(list1):
            return True
    return False


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

